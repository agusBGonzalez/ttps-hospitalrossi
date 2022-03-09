from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import text
from datetime import date
from app.models.historia import Historia, Sexo
import sys

dba = SQLAlchemy()

def estadGen1(datos, tablaEvento, tablaRef, totalEvento, desde, hasta, labelRef, labelTotal, postLabelRef=""):
    #Calculo para estadisticas de la forma: 
    # % de cada posible para un atributo sobre la cantidad de eventos que afectados por ese atributo (es decir, que el atributo tiene un valor)
    # % de eventos afectados por el atributo sobre el total de eventos
    # la relacion entre el evento y la tabla de referencia para el atributo es uno a N

    #calculo la cantidad total del evento afectado por el atributo de referencia
    #Sobre este universo se calcula el % de cada posibilidad dentro de la tabla de referencia
    sql = text("select count(1) cant from " + tablaEvento + " v "+
                    "inner join " + tablaRef + " ref on v.id_" + tablaRef + " = ref.id " +
                    "where (v.fecha >=:desde ) and (v.fecha <=:hasta ) "
              )
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )
    fila = result.fetchone()
    cantRef = fila["cant"]
    
    sql = text("select count(1) cant, ref.descripcion descri from " + tablaEvento + " v "+
                    "inner join " + tablaRef + " ref on v.id_" + tablaRef + " = ref.id " +
                    "where (v.fecha >=:desde ) and (v.fecha <=:hasta ) "+
                    "group by ref.descripcion"
              )

    result = dba.engine.execute(sql, desde=desde, hasta=hasta )
    for fila in result:
        cant = fila["cant"]
        descri = fila["descri"]
        estadistica =  {
                        "label": labelRef + descri + postLabelRef,
                        "data": round(cant * 100 / cantRef,2)
                        }
        #agrego la estaditistica correspondiente al elemento de la tabla de referencia
        datos.append(estadistica) 

    #el % total es el la cantidad total afectada por el atributo de referencia, sobre la cantidad total del evento
    estadistica =  {
                    "label": labelTotal,
                    "data": round(cantRef * 100 / totalEvento,2)
                    }
    datos.append(estadistica) 

#####################################################################################################################################################

def estadGen2(datos, tablaEvento, tablaRef, tablaRel, totalEvento, desde, hasta, labelRef, labelTotal):
    #Calculo para estadisticas de la forma: 
    # % de cada posible para un atributo sobre la cantidad de eventos que afectados por ese atributo (es decir, que el atributo tiene un valor)
    # % de eventos afectados por el atributo sobre el total de eventos
    # la relacion entre el evento y la tabla de referencia para el atributo es N a N
    
    #calculo la cantidad total del evento afectado por el atributo de referencia
    #Sobre este universo se calcula el % de cada posibilidad dentro de la tabla de referencia

    sql = text("select count(1) cant from " + tablaEvento + " v "+
                    "inner join " + tablaRel + " rel on v.id =  rel.id_" + tablaEvento + 
                    " inner join " + tablaRef + " ref on rel.id_" + tablaRef + " = ref.id " +
                    "where (v.fecha >=:desde ) and (v.fecha <=:hasta ) "
              )
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )
    fila = result.fetchone()
    cantRef = fila["cant"]
    
    sql = text("select count(1) cant, ref.descripcion descri from " + tablaEvento + " v "+
                    "inner join " + tablaRel + " rel on v.id =  rel.id_" + tablaEvento + 
                    " inner join " + tablaRef + " ref on rel.id_" + tablaRef + " = ref.id " +
                    "where (v.fecha >=:desde ) and (v.fecha <=:hasta ) " +
                    "group by ref.descripcion"
              )

    result = dba.engine.execute(sql, desde=desde, hasta=hasta )
    for fila in result:
        cant = fila["cant"]
        descri = fila["descri"]
        estadistica =  {
                        "label": labelRef + descri,
                        "data": round(cant * 100 / cantRef,2)
                        }
        #agrego la estaditistica correspondiente al elemento de la tabla de referencia
        datos.append(estadistica) 

    #el % total es el la cantidad total afectada por el atributo de referencia, sobre la cantidad total del evento
    estadistica =  {
                    "label": labelTotal,
                    "data": round(cantRef * 100 / totalEvento,2)
                    }
    datos.append(estadistica) 

def reporteEstadisticoVCC(desde, hasta):
    estadisticas = []

    s = text("SELECT count(1) cant FROM vcc where (vcc.fecha >=:desde) and  (vcc.fecha <=:hasta)")
    result = dba.engine.execute(s, desde=desde, hasta=hasta)

    cantVCC = 0
    
    fila = result.fetchone()
    cantVCC = fila["cant"]

    #for fila in result:
    #    cantVCC = fila["cant"]

    sql = text("""
                select  sum( TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) ) as sumaEdad, count(1) as cant
                from  historia h
                where id in 
                ( select id_historia
                from vcc
                where (vcc.fecha >=:desde ) and  (vcc.fecha <=:hasta )
                )
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta)
    
    fila = result.fetchone()
    edadTotal = fila["sumaEdad"]
    cantPac = fila["cant"]

    estadistica =  {
                    "label": "Edad promedio",
                    "data": round(edadTotal / cantPac,1)
                    }

    estadisticas.append(estadistica)

    ############################################################################################################################################

    sql = text("select count(1) cant from vcc where (vcc.id_vcc_polipos_cant is not null) and (vcc.fecha >=:desde ) and  (vcc.fecha <=:hasta )")
    result = dba.engine.execute(sql, desde=desde, hasta=hasta)
    for fila in result:
        cantConPolipos = fila["cant"]

    estadistica =  {
                "label": "% de pacientes con pólipos",
                "data": round(cantConPolipos * 100 / cantVCC,2)
                }

    estadisticas.append(estadistica)

    ############################################################################################################################################

    sql = text("""
                select count(1) cant, vpc.descripcion rango
                from 
                vcc
                    inner join vcc_polipos_cant vpc on vcc.id_VCC_polipos_cant = vpc.id
                where (vcc.fecha >=:desde ) and  (vcc.fecha <=:hasta )
                group by vpc.descripcion 
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta)
    for fila in result:
        cant = fila["cant"]
        rango = fila["rango"]
        estadistica =  {
                    "label": "% de pacientes con "+ rango + " pólipos (dentro de los pacientes con pólipos)",
                    "data": round(cant * 100 / cantConPolipos,2)
                    }
        estadisticas.append(estadistica)

    ############################################################################################################################################

    sql = text("""
                                select count(1) cant, h.id_sexo, s.descripcion sexo 
                                from vcc v  
                                inner join historia h on h.id = v.id_historia
                                    inner join sexo s on h.id_sexo = s.id
                                where (v.fecha >=:desde ) and (v.fecha <=:hasta )
                                group by h.id_sexo, s.descripcion
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta) 

    total = 0
    temps = []
    for fila in result:
        cant = fila["cant"]
        sexo = fila["sexo"]
        total += cant
        temp = {
                "cant": cant,
                "sexo": sexo,
                "porcentaje": 0
                }
        temps.append(temp)        
    
    for  fila in temps:
        estadistica =  {
                    "label": "% de VCC para pacientes de sexo " + fila["sexo"],
                    "data": round(fila["cant"] * 100 / total,2)
                    }
        estadisticas.append(estadistica)
    
    ############################################################################################################################################

    sql = text ("""select count(1) cant, vm.descripcion as motivo
                                from vcc v  
                                inner join vcc_vcc_motivo vvm  on vvm.id_VCC = v.id 
                                    inner join vcc_motivo vm on vvm.id_VCC_motivo = vm.id 
                                where (v.fecha >=:desde ) and (v.fecha <=:hasta )
                                group by vm.descripcion
                                order by count(1)
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )

    maximo = 0
    for fila in result:
        if fila["cant"] >= maximo :
            maximo = fila["cant"]
            # si hay más de un máximo agrego varias filas por cada uno
            estadistica =  {
                        "label": "Motivo más habitual",
                        "data": fila["motivo"]
                        }
            estadisticas.append(estadistica)

    ############################################################################################################################################

    sql = text("""
                select count(1) cant, vh.descripcion as hallazgo
                from vcc v  
                inner join vcc_vcc_hallazgos vvh on vvh.id_VCC = v.id 
                    inner join vcc_hallazgos vh on vvh.id_VCC_hallazgos = vh.id 
                where (v.fecha >=:desde ) and (v.fecha <=:hasta )
                group by vh.descripcion
                order by count(1)
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )

    maximo = 0
    for fila in result:
        if fila["cant"] >= maximo :
            maximo = fila["cant"]
            # si hay más de un máximo agrego varias filas por cada uno
            estadistica =  {
                        "label": "Hallazgo más habitual",
                        "data": fila["hallazgo"]
                        }
            estadisticas.append(estadistica)       

    ############################################################################################################################################

    sql = text("""
                select u.first_name, u.last_name, count(1) cant
                from 
                vcc v 
                    inner join usuario u
                    on v.id_operador = u.id 
                where (v.fecha >=:desde ) and (v.fecha <=:hasta )
                group by u.first_name, u.last_name
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )
    for fila in result:
        cant = fila["cant"]
        operador = fila["first_name"] +" "+ fila["last_name"]
        estadistica =  {
                    "label": "% del operador "+ operador,
                    "data": round(cant * 100 / cantVCC,2)
                    }
        estadisticas.append(estadistica)

    ############################################################################################################################################

    estadGen1(estadisticas, 'VCC', 'vcc_preparacion', cantVCC, desde, hasta, "% de la preparación - ", "% de VCC con preparaciones")
    #borro el dato general porque al ser campo obligatorio siempre es el 100%
    del estadisticas[-1]

    ############################################################################################################################################

    sql = text("""
                select count(1) cant, vm.descripcion motivo
                from 
                vcc v 
                inner join vcc_vcc_motivo vvm on v.id = vvm.id_VCC 
                    inner join vcc_motivo vm on vvm.id_VCC_motivo = vm.id
                where (v.fecha >=:desde ) and (v.fecha <=:hasta )
                group by vm.descripcion 
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )

    for fila in result:
        cant = fila["cant"]
        motivo = fila["motivo"]
        #motivo es obligatorio, por lo tanto puedo dividir la cantidad por cantVCC (cant total de VCC)
        estadistica =  {
                        "label": "% del motivo "+ motivo,
                        "data": round(cant * 100 / cantVCC,2)
                        }
        estadisticas.append(estadistica) 

    ############################################################################################################################################
#
    #sql = text("""
    #            select count(1) cant
    #            from 
    #            vcc v 
    #            where (v.id_VCC_incompleta_hasta is not null) or (v.id_VCC_incompleta_motivo is not null)
    #            and (v.fecha >=:desde ) and (v.fecha <=:hasta )
    #            """)
    #result = dba.engine.execute(sql, desde=desde, hasta=hasta )
#
    #
    #fila = result.fetchone()
    #cantInc = fila["cant"]
    #estadistica =  {
    #                "label": "% de estudios incompletos",
    #                "data": round(cantInc * 100 / cantVCC,2)
    #                }
    #estadisticas.append(estadistica) 
#
#
    #sql = text("""
    #            select  count(1) cant, vim.descripcion motivo
    #            from 
    #            vcc v
    #            inner join vcc_incompleta_motivo vim on v.id_VCC_incompleta_motivo = vim.id
    #            where (v.fecha >=:desde ) and (v.fecha <=:hasta )
    #            group by vim.descripcion 
    #            """)
    #result = dba.engine.execute(sql, desde=desde, hasta=hasta )
#
    #for fila in result:
    #    cant = fila["cant"]
    #    motivo = fila["motivo"]
    #    estadistica =  {
    #                    "label": "% del motivo para estudio incompleto "+ motivo,
    #                    "data": round(cant * 100 / cantInc,2)
    #                    }
    #    estadisticas.append(estadistica) 
    
    estadGen1(estadisticas, 'VCC', 'vcc_incompleta_motivo', cantVCC, desde, hasta, "% del motivo ", "% de estudios incompletos", " para estudio incompleto")
    ############################################################################################################################################

    estadGen2(estadisticas, 'VCC', 'vcc_hallazgos', 'vcc_vcc_hallazgos', cantVCC, desde, hasta, "% del hallazgo (sobre VCC con hallazgos) de tipo ", "% de hallazgos sobre total VCC")

    estadGen2(estadisticas, 'VCC', 'vcc_terapeutica', 'vcc_vcc_terapeutica', cantVCC, desde, hasta, "% de terapéutica (sobre VCC con terapéuticas) de tipo ", "% terapéutica sobre total VCC ")

    estadGen1(estadisticas, 'VCC', 'vcc_lesion_sospechosa', cantVCC, desde, hasta, "% de lesión (sobre VCC con lesiones sospechosas) sospechosa tipo ", "% de lesión sospechosa sobre total VCC")

    estadGen1(estadisticas, 'VCC', 'vcc_polipos_cant', cantVCC, desde, hasta, "% con pólipos  (sobre VCC con pólipos) con cantidad en el rango: ", "% de VCC con pólipos")
    #borro el dato general porque hay varias secciones de polipectomia, y el % sobre el total de VCC deberia ser igual para todas las secciones
    del estadisticas[-1]

    estadGen1(estadisticas, 'VCC', 'vcc_polipectomia_tam', cantVCC, desde, hasta, "% con pólipos  (sobre VCC con pólipos) con tamaño en el rango: ", "% de VCC con pólipos")
    #borro el dato general porque hay varias secciones de polipectomia, y el % sobre el total de VCC deberia ser igual para todas las secciones
    del estadisticas[-1]

    estadGen1(estadisticas, 'VCC', 'vcc_polipectomia_paris', cantVCC, desde, hasta, "% con pólipos Paris  (sobre VCC con pólipos) - ", "% de VCC con pólipos")
    #borro el dato general porque hay varias secciones de polipectomia, y el % sobre el total de VCC deberia ser igual para todas las secciones
    del estadisticas[-1]

    estadGen1(estadisticas, 'VCC', 'vcc_polipectomia_material', cantVCC, desde, hasta, "% polipectomia material  (sobre VCC con pólipos) - ", "% de VCC con pólipos")
    
    ############################################################################################################################################
    sql = text("""
                select count(1) cant
                from 
                vcc v 
                where (v.ileoscopia )
                and (v.fecha >=:desde ) and (v.fecha <=:hasta )
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )    
    fila = result.fetchone()
    cant = fila["cant"]
    estadistica =  {
                    "label": "% de VCC con ileoscopia",
                    "data": round(cant * 100 / cantVCC,2)
                    }
    estadisticas.append(estadistica) 

    ############################################################################################################################################

    estadGen1(estadisticas, 'VCC', 'vcc_de_guardia', cantVCC, desde, hasta, "% de guardia - ", "% de guardia sobre total VCC")

    estadGen2(estadisticas, 'VCC', 'vcc_complicaciones', 'vcc_vcc_complicaciones', cantVCC, desde, hasta, "% de complicaciones (sobre VCC con terapéuticas) de tipo ", "% complicaciones sobre total VCC ")

    estadGen1(estadisticas, 'VCC', 'vcc_tiempo_ingreso', cantVCC, desde, hasta, "% tiempo de ingreso ", "% de tiempo sobre total VCC")
    #borro el dato general porque al ser campo obligatorio siempre es el 100%
    del estadisticas[-1]

    estadGen1(estadisticas, 'VCC', 'vcc_tiempo_retirada', cantVCC, desde, hasta, "% tiempo de retirada ", "% de tiempo sobre total VCC")
    #borro el dato general porque al ser campo obligatorio siempre es el 100%
    del estadisticas[-1]
    
    return estadisticas

    ############################################################################################################################################
    ############################################################################################################################################
def concatRefMultiple(id_evento, tablaEvento, tableRefMultiple, tablaRef):
    sql = text("select " + tablaRef + ".descripcion descri "
                "from  "+
                    tableRefMultiple +
                    " inner join " + tablaRef +" on "+tableRefMultiple+".id_"+tablaRef+" = "+tablaRef+".id "+
                "where " + tableRefMultiple+".id_"+tablaEvento+" = :id_evento"
                )
    result = dba.engine.execute(sql, id_evento=id_evento)    

    referencia = ""
    for fila in result:
        referencia += fila["descri"]+ ", "

    #elimino ultimos 2 caracteres : ", "
    referencia = referencia[:-2]
    return referencia    

def reporteCompletoVCC(desde, hasta, id_historia=0):
    if (id_historia==0):
        filtroHistoria = ""
    else: 
        filtroHistoria = " and v.id_historia = :id_historia "

    sql = text("""
                select 
                    v.id, 
                    v.fecha fechaSF,
                    date_format(v.fecha, "%d/%m/%Y") fecha, h.nombre, date_format(h.nacimiento, "%d/%m/%Y") nacimiento, TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) edad,
                    v.comentarios,
                    ifnull(vcc_de_guardia.descripcion,'') vcc_de_guardia,
                    ifnull(vcc_incompleta_hasta.descripcion,'') vcc_incompleta_hasta,
                    ifnull(vcc_incompleta_motivo.descripcion,'') vcc_incompleta_motivo,
                    ifnull(vcc_lesion_sospechosa.descripcion,'') vcc_lesion_sospechosa,
                    ifnull(vcc_polipectomia_material.descripcion,'') vcc_polipectomia_material,
                    ifnull(vcc_polipectomia_paris.descripcion,'') vcc_polipectomia_paris,
                    ifnull(vcc_polipectomia_tam.descripcion,'') vcc_polipectomia_tam,
                    ifnull(vcc_polipectomia_tecnica.descripcion,'') vcc_polipectomia_tecnica,
                    ifnull(vcc_polipos_cant.descripcion,'') vcc_polipos_cant,
                    ifnull(vcc_preparacion.descripcion,'') vcc_preparacion,
                    ifnull(vcc_tiempo_ingreso.descripcion,'') vcc_tiempo_ingreso,
                    ifnull(vcc_tiempo_retirada.descripcion,'') vcc_tiempo_retirada
                from 
                vcc v
                inner join historia h on h.id = v.id_historia 
                left outer join vcc_de_guardia on vcc_de_guardia.id = v.id_vcc_de_guardia
                left outer join vcc_incompleta_hasta on vcc_incompleta_hasta.id = v.id_vcc_incompleta_hasta
                left outer join vcc_incompleta_motivo on vcc_incompleta_motivo.id = v.id_vcc_incompleta_motivo
                left outer join vcc_lesion_sospechosa on vcc_lesion_sospechosa.id = v.id_vcc_lesion_sospechosa
                left outer join vcc_polipectomia_material on vcc_polipectomia_material.id = v.id_vcc_polipectomia_material
                left outer join vcc_polipectomia_paris on vcc_polipectomia_paris.id = v.id_vcc_polipectomia_paris
                left outer join vcc_polipectomia_tam on vcc_polipectomia_tam.id = v.id_vcc_polipectomia_tam
                left outer join vcc_polipectomia_tecnica on vcc_polipectomia_tecnica.id = v.id_vcc_polipectomia_tecnica
                left outer join vcc_polipos_cant on vcc_polipos_cant.id = v.id_vcc_polipos_cant
                left outer join vcc_preparacion on vcc_preparacion.id = v.id_vcc_preparacion
                inner join vcc_tiempo_ingreso on vcc_tiempo_ingreso.id = v.id_vcc_tiempo_ingreso
                inner join vcc_tiempo_retirada on vcc_tiempo_retirada.id = v.id_vcc_tiempo_retirada
                WHERE (v.fecha >=:desde ) and (v.fecha <=:hasta )
                """ + filtroHistoria + " Order by v.fecha ")
    
    if (id_historia==0):                
        result = dba.engine.execute(sql, desde=desde, hasta=hasta )    
    else:
        result = dba.engine.execute(sql, desde=desde, hasta=hasta, id_historia=id_historia )

    datos = []
    for fila in result:
        dato =  {       
                        "fecha": fila["fecha"],
                        "fechaSF": fila["fechaSF"],
                        "nombre": fila["nombre"],
                        "nacimiento": fila["nacimiento"],
                        "edad": fila["edad"],
                        "comentarios": fila["comentarios"],
                        "vcc_de_guardia": fila["vcc_de_guardia"],
                        "vcc_incompleta_hasta": fila["vcc_incompleta_hasta"],
                        "vcc_incompleta_motivo": fila["vcc_incompleta_motivo"],
                        "vcc_lesion_sospechosa": fila["vcc_lesion_sospechosa"],
                        "vcc_polipectomia_material": fila["vcc_polipectomia_material"],
                        "vcc_polipectomia_paris": fila["vcc_polipectomia_paris"],
                        "vcc_polipectomia_tam": fila["vcc_polipectomia_tam"],
                        "vcc_polipectomia_tecnica": fila["vcc_polipectomia_tecnica"],
                        "vcc_polipos_cant": fila["vcc_polipos_cant"],
                        "vcc_preparacion": fila["vcc_preparacion"],
                        "vcc_tiempo_ingreso": fila["vcc_tiempo_ingreso"],
                        "vcc_tiempo_retirad": fila["vcc_tiempo_retirada"],
                        "complicaciones": concatRefMultiple(fila['id'], "VCC", "vcc_vcc_complicaciones", "vcc_complicaciones"),
                        "biopsias": concatRefMultiple(fila['id'], "VCC", "vcc_vcc_biopsias", "vcc_biopsias"),
                        "hallazgos": concatRefMultiple(fila['id'], "VCC", "vcc_vcc_hallazgos", "vcc_hallazgos"),
                        "motivo": concatRefMultiple(fila['id'], "VCC", "vcc_vcc_motivo", "vcc_motivo"),
                        "terapeutica": concatRefMultiple(fila['id'], "VCC", "vcc_vcc_terapeutica", "vcc_terapeutica")
                        }
        
        datos.append(dato) 

    return datos

def reporteBostonVCC(desde, hasta, valorRef):
    sql = text("""
                select v.id, 
                    date_format(v.fecha, "%d/%m/%Y") fecha, h.nombre, h.nacimiento, TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) edad,
                    v.comentarios,
                    v.boston_izq , v.boston_trasv , v.boston_der ,
                    (v.boston_izq + v.boston_trasv + v.boston_der) boston
                from 
                vcc v
                inner join historia h on h.id = v.id_historia 
                where
                ( (v.boston_izq + v.boston_trasv + v.boston_der) >=:valorRef )
                and (v.fecha >=:desde ) and (v.fecha <=:hasta )
                order by v.fecha
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta, valorRef=valorRef )             
    datos = []
    return result

def reportePoliposVCC(desde, hasta):
    sql = text("""
                    select v.id, 
                            date_format(v.fecha, "%d/%m/%Y") fecha, h.nombre, h.nacimiento, TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) edad,
                        v.comentarios, 
                        vpt.descripcion tam
                    from 
                    vcc v
                    inner join vcc_polipectomia_tam vpt 
                    on v.id_VCC_polipectomia_tam = vpt.id 
                    inner join historia h on h.id = v.id_historia 
                    WHERE
                    (v.fecha >=:desde ) and (v.fecha <=:hasta )
                    order by h.nombre, v.fecha
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta)             
    datos = []
    return result