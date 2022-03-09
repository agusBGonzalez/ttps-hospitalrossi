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

def reporteEstadisticoVEDA(desde, hasta):
    estadisticas = []

    sql = text("SELECT count(1) cant FROM veda v where (v.fecha >=:desde) and  (v.fecha <=:hasta)")
    result = dba.engine.execute(sql, desde=desde, hasta=hasta)

    fila = result.fetchone()
    cantVEDA = fila["cant"]

    ############################################################################################################################################
    sql = text("""
                select  sum( TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) ) as sumaEdad, count(1) as cant
                from  historia h
                where id in 
                ( select id_historia
                from veda v
                where (v.fecha >=:desde ) and  (v.fecha <=:hasta )
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
    sql = text("select count(1) cant from veda v where (v.id_veda_polipectomia_tam is not null) and (v.fecha >=:desde ) and  (v.fecha <=:hasta )")
    result = dba.engine.execute(sql, desde=desde, hasta=hasta)
    for fila in result:
        cantConPolipos = fila["cant"]

    estadistica =  {
                "label": "% de pacientes con pólipos",
                "data": round(cantConPolipos * 100 / cantVEDA,2)
                }

    estadisticas.append(estadistica)

    ############################################################################################################################################

    estadGen1(estadisticas, 'VEDA', 'veda_incompleto', cantVEDA, desde, hasta, "% del motivo ", "% de estudios incompletos", " para estudio incompleto")
    estadGen2(estadisticas, 'VEDA', 'veda_motivo', 'veda_veda_motivo', cantVEDA, desde, hasta, "% del motivo de tipo ", "% sobre total VEDA ")
    #borro el dato general porque hay varias secciones de polipectomia, y el % sobre el total de VCC deberia ser igual para todas las secciones
    del estadisticas[-1]

    estadGen1(estadisticas, 'VEDA', 'veda_terapeutica', cantVEDA, desde, hasta, "% de terapéutica ", "% terapéuticas  sobre total VEDA")
    estadGen1(estadisticas, 'VEDA', 'veda_polipectomia_material', cantVEDA, desde, hasta, "% de técnica de polipectomia ", "% pólipos sobre total VEDA")
    del estadisticas[-1]
    estadGen1(estadisticas, 'VEDA', 'veda_polipectomia_paris', cantVEDA, desde, hasta, "% de valor en escala Paris ", "% pólipos sobre total VEDA")
    del estadisticas[-1]
    estadGen1(estadisticas, 'VEDA', 'veda_polipectomia_tam', cantVEDA, desde, hasta, "% de polipos con tamaño en el rango ", "% pólipos sobre total VEDA")

    estadGen2(estadisticas, 'VEDA', 'veda_hallazgo', 'veda_veda_hallazgo', cantVEDA, desde, hasta, "% del hallazgo de tipo ", "% hallazgos sobre total VEDA ")
    estadGen1(estadisticas, 'VEDA', 'veda_biopsia', cantVEDA, desde, hasta, "% de biopsia de ", "% biopsias sobre total VEDA")
    estadGen1(estadisticas, 'VEDA', 'veda_protocolo', cantVEDA, desde, hasta, "% de protocolo ", "% con protocolos sobre total VEDA")
    estadGen1(estadisticas, 'VEDA', 'veda_de_guardia', cantVEDA, desde, hasta, "% de guardia por ", "% con guardia sobre total VEDA")
    estadGen1(estadisticas, 'VEDA', 'veda_tiempo', cantVEDA, desde, hasta, "% de tiempo ", "% con sobre total VEDA")
    del estadisticas[-1]

    ############################################################################################################################################

    sql = text("""
                select u.first_name, u.last_name, count(1) cant
                from 
                veda v 
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
                    "data": round(cant * 100 / cantVEDA,2)
                    }
        estadisticas.append(estadistica)
    
    ############################################################################################################################################

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

def reporteCompletoVEDA(desde, hasta, id_historia=0):
    if (id_historia==0):
        filtroHistoria = ""
    else: 
        filtroHistoria = " and v.id_historia = :id_historia "
    
    sql = text("""
                    select v.id,
                        v.fecha fechaSF,
                        date_format(v.fecha, "%d/%m/%Y") fecha, h.nombre, date_format(h.nacimiento, "%d/%m/%Y") nacimiento, TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) edad,
                        v.comentarios,
                        v.anestesia ,
                        ifnull(veda_biopsia.descripcion,'') veda_biopsia,
                        ifnull(veda_de_guardia.descripcion,'') veda_de_guardia,
                        ifnull(veda_incompleto.descripcion,'') veda_incompleto,
                        ifnull(veda_polipectomia_material.descripcion,'') veda_polipectomia_material,
                        ifnull(veda_polipectomia_paris.descripcion,'') veda_polipectomia_paris,
                        ifnull(veda_polipectomia_tam.descripcion,'') veda_polipectomia_tam,
                        ifnull(veda_protocolo.descripcion,'') veda_protocolo,
                        ifnull(veda_terapeutica.descripcion,'') veda_terapeutica,
                        ifnull(veda_tiempo.descripcion,'') veda_tiempo	
                    from 
                    veda v
                    inner join historia h on h.id = v.id_historia 
                    left outer join veda_biopsia on v.id_veda_biopsia = veda_biopsia.id
                    left outer join veda_de_guardia on v.id_veda_de_guardia = veda_de_guardia.id
                    left outer join veda_incompleto on v.id_veda_incompleto = veda_incompleto.id
                    left outer join veda_polipectomia_material on v.id_veda_polipectomia_material = veda_polipectomia_material.id
                    left outer join veda_polipectomia_paris on v.id_veda_polipectomia_paris = veda_polipectomia_paris.id
                    left outer join veda_polipectomia_tam on v.id_veda_polipectomia_tam = veda_polipectomia_tam.id
                    left outer join veda_protocolo on v.id_veda_protocolo = veda_protocolo.id
                    left outer join veda_terapeutica on v.id_veda_terapeutica = veda_terapeutica.id
                    inner join veda_tiempo on v.id_veda_tiempo = veda_tiempo.id
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
                        "veda_biopsia" : fila["veda_biopsia"],
                        "veda_de_guardia" : fila["veda_de_guardia"],
                        "veda_incompleto" : fila["veda_incompleto"],
                        "veda_polipectomia_material" : fila["veda_polipectomia_material"],
                        "veda_polipectomia_paris" : fila["veda_polipectomia_paris"],
                        "veda_polipectomia_tam" : fila["veda_polipectomia_tam"],
                        "veda_protocolo" : fila["veda_protocolo"],
                        "veda_terapeutica" : fila["veda_terapeutica"],
                        "veda_tiempo" : fila["veda_tiempo"],
                        "hallazgos": concatRefMultiple(fila['id'], "VEDA", "veda_veda_hallazgo", "veda_hallazgo"),
                        "motivo": concatRefMultiple(fila['id'], "VEDA", "veda_veda_motivo", "veda_motivo"),
                        }
        #agrego la estaditistica correspondiente al elemento de la tabla de referencia
        datos.append(dato) 

    return datos

