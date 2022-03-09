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

############################################################################################################################################
def estadGen3(datos, tablaEvento, campoBool, totalEvento, desde, hasta, label_T, label_F):
    # funcion generica de % para campos booleanos

    sql = text("select count(1) cant from " + tablaEvento + " v " +
                "where (v.fecha >=:desde ) and (v.fecha <=:hasta ) " +
                " and v."+campoBool
                )
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )
    fila = result.fetchone()
    cant = fila["cant"]

    resto = totalEvento - cant
    estadistica =  {
                    "label": label_T,
                    "data": round(cant * 100 / totalEvento,2)
                    }
    datos.append(estadistica)

    estadistica =  {
                    "label": label_F,
                    "data": round(resto * 100 / totalEvento,2)
                    }
    datos.append(estadistica)

############################################################################################################################################
############################################################################################################################################

def reporteEstadisticoCPRE(desde, hasta):
    estadisticas = []

    s = text("SELECT count(1) cant FROM cpre v where (v.fecha >=:desde) and  (v.fecha <=:hasta)")
    result = dba.engine.execute(s, desde=desde, hasta=hasta)

    cantCPRE = 0
    
    fila = result.fetchone()
    cantCPRE = fila["cant"]

    sql = text("""
                select  sum( TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) ) as sumaEdad, count(1) as cant
                from  historia h
                where id in 
                ( select id_historia
                from cpre v
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

    sql = text("""
                                select count(1) cant, h.id_sexo, s.descripcion sexo 
                                from cpre v  
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
                    "label": "% de CPRE para pacientes de sexo " + fila["sexo"],
                    "data": round(fila["cant"] * 100 / total,2)
                    }
        estadisticas.append(estadistica)
    

    ############################################################################################################################################

    sql = text("""
                select u.first_name, u.last_name, count(1) cant
                from 
                cpre v 
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
                    "data": round(cant * 100 / cantCPRE,2)
                    }
        estadisticas.append(estadistica)

    ############################################################################################################################################
    sql = text("""
            select u.first_name, u.last_name, count(1) cant
            from 
            cpre v 
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
                    "data": round(cant * 100 / cantCPRE,2)
                    }
        estadisticas.append(estadistica)

    ############################################################################################################################################


    #estadGen1(estadisticas, 'VCC', 'vcc_preparacion', cantCPRE, desde, hasta, "% de la preparación - ", "% de VCC con preparaciones")
    #borro el dato general porque al ser campo obligatorio siempre es el 100%
    #del estadisticas[-1]

    ############################################################################################################################################

    #estadGen2(estadisticas, 'VCC', 'vcc_hallazgos', 'vcc_vcc_hallazgos', cantCPRE, desde, hasta, "% del hallazgo (sobre VCC con hallazgos) de tipo ", "% de hallazgos sobre total VCC")

    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="ambulatorio", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% Ambulatorio", label_F="% Internado")
    estadGen2(estadisticas, 'CPRE', 'cpre_indicacion_asge', 'cpre_cpre_indicacion_asge', cantCPRE, desde, hasta, "% de indicación ASGE (sobre CPRE con indic. ASGE) de tipo ", "% indicaciones ASGE sobre total CPRE")
    estadGen2(estadisticas, 'CPRE', 'cpre_indicacion', 'cpre_cpre_indicacion', cantCPRE, desde, hasta, "% de indicación (sobre CPRE con indicaciones) de tipo ", "% indicaciones sobre total CPRE")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="cpre_previa", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE Previa", label_F="% Sin CPRE Previa")
    del estadisticas[-1]
    estadGen2(estadisticas, 'CPRE', 'cpre_cirugia_prev','cpre_cpre_cirugia_prev', cantCPRE, desde, hasta, "% (sobre CPRE cirugía previa) de cirugia previa de tipo ", "% cirugía previa sobre total CPRE")

    estadGen2(estadisticas, 'cpre', 'cpre_coledocolitiasis', 'cpre_cpre_coledocolitiasis', cantCPRE, desde, hasta, '% (sobre CPRE con coledocolitiasis) de tipo ', '% coledocolitiasis sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_complicaciones', 'cpre_cpre_complicaciones', cantCPRE, desde, hasta, '% (sobre CPRE con complicaciones) de tipo ', '% complicaciones sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_diverticulo', 'cpre_cpre_diverticulo', cantCPRE, desde, hasta, '% (sobre CPRE con diverticulo) de tipo ', '% diverticulo sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_eco_abd', 'cpre_cpre_eco_abd', cantCPRE, desde, hasta, '% (sobre CPRE con eco_abd) de tipo ', '% eco_abd sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_estenosis_alta', 'cpre_cpre_estenosis_alta', cantCPRE, desde, hasta, '% (sobre CPRE con estenosis_alta) de tipo ', '% estenosis_alta sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_estenosis_baja', 'cpre_cpre_estenosis_baja', cantCPRE, desde, hasta, '% (sobre CPRE con estenosis_baja) de tipo ', '% estenosis_baja sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_eus', 'cpre_cpre_eus', cantCPRE, desde, hasta, '% (sobre CPRE con eus) de tipo ', '% eus sobre total CPRE')
    
    #estadGen2(estadisticas, 'cpre', 'cpre_grado_asge', 'cpre_cpre_grado_asge', cantCPRE, desde, hasta, '% (sobre CPRE con grado_asge) de tipo ', '% grado_asge sobre total CPRE')
    #estadGen2(estadisticas, 'cpre', 'cpre_grado_dif', 'cpre_cpre_grado_dif', cantCPRE, desde, hasta, '% (sobre CPRE con grado_dif) de tipo ', '% grado_dif sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_grado_asge', cantCPRE, desde, hasta, '% (sobre CPRE con grado_asge) de tipo ','% grado_asge sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_grado_dif', cantCPRE, desde, hasta, '% (sobre CPRE con grado_dif) de tipo','% grado_dif sobre total CPRE')
    
    estadGen2(estadisticas, 'cpre', 'cpre_indicacion', 'cpre_cpre_indicacion', cantCPRE, desde, hasta, '% (sobre CPRE con indicacion) de tipo ', '% indicacion sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_indicacion_asge', 'cpre_cpre_indicacion_asge', cantCPRE, desde, hasta, '% (sobre CPRE con indicacion_asge) de tipo ', '% indicacion_asge sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_indicacion_ept', 'cpre_cpre_indicacion_ept', cantCPRE, desde, hasta, '% (sobre CPRE con indicacion_ept) de tipo ', '% indicacion_ept sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_lpqvb', 'cpre_cpre_lpqvb', cantCPRE, desde, hasta, '% (sobre CPRE con lpqvb) de tipo ', '% lpqvb sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_miscelaneas', 'cpre_cpre_miscelaneas', cantCPRE, desde, hasta, '% (sobre CPRE con miscelaneas) de tipo ', '% miscelaneas sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_profilaxis_atb', 'cpre_cpre_profilaxis_atb', cantCPRE, desde, hasta, '% (sobre CPRE con profilaxis_atb) de tipo ', '% profilaxis_atb sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_resolucion_complica', 'cpre_cpre_resolucion_complica', cantCPRE, desde, hasta, '% (sobre CPRE con resolucion_complica) de tipo ', '% resolucion_complica sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_rnm', 'cpre_cpre_rnm', cantCPRE, desde, hasta, '% (sobre CPRE con rnm) de tipo ', '% rnm sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_tac', 'cpre_cpre_tac', cantCPRE, desde, hasta, '% (sobre CPRE con tac) de tipo ', '% tac sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_terap_pancreas', 'cpre_cpre_terap_pancreas', cantCPRE, desde, hasta, '% (sobre CPRE con terap_pancreas) de tipo ', '% terap_pancreas sobre total CPRE')
    estadGen2(estadisticas, 'cpre', 'cpre_transk', 'cpre_cpre_transk', cantCPRE, desde, hasta, '% (sobre CPRE con transk) de tipo ', '% transk sobre total CPRE')

    estadGen1(estadisticas, 'CPRE', 'cpre_ept', cantCPRE, desde, hasta, '% para cada cpre_ept ','% cpre_ept sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_wirsung', cantCPRE, desde, hasta, '% para cada cpre_wirsung ','% cpre_wirsung sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_precorte', cantCPRE, desde, hasta, '% para cada cpre_precorte ','% cpre_precorte sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_dilatacion_biliar', cantCPRE, desde, hasta, '% para cada cpre_dilatacion_biliar ','% cpre_dilatacion_biliar sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_litotripsia', cantCPRE, desde, hasta, '% para cada cpre_litotripsia ','% cpre_litotripsia sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_stent_plastico', cantCPRE, desde, hasta, '% para cada cpre_stent_plastico ','% cpre_stent_plastico sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_stent_autoexp', cantCPRE, desde, hasta, '% para cada cpre_stent_autoexp ','% cpre_stent_autoexp sobre total CPRE')
    estadGen1(estadisticas, 'CPRE', 'cpre_amilasemia_2hs', cantCPRE, desde, hasta, '% para cada cpre_amilasemia_2hs ','% cpre_amilasemia_2hs sobre total CPRE')

    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="cpre_previa", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE Previa", label_F="% Sin CPRE Previa")

    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="FR_DE_PA_SOD", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con FR_DE_PA_SOD ", label_F="% sin FR_DE_PA_SOD")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="FR_DE_PA_AUSENCIA_PC", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con FR_DE_PA_AUSENCIA_PC ", label_F="% sin FR_DE_PA_AUSENCIA_PC")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="FR_DE_PA_ANTEC_PA", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con FR_DE_PA_ANTEC_PA ", label_F="% sin FR_DE_PA_ANTEC_PA")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="CPRE_normal", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con CPRE_normal ", label_F="% sin CPRE_normal")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="ESFINTEROPLASTIA", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con ESFINTEROPLASTIA ", label_F="% sin ESFINTEROPLASTIA")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="stent_duodenal", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con stent_duodenal ", label_F="% sin stent_duodenal")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="resolucion_completa", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con resolucion_completa ", label_F="% sin resolucion_completa")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="canulacion", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con canulacion ", label_F="% sin canulacion")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="biopsias", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con biopsias ", label_F="% sin biopsias")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="fracaso", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con fracaso ", label_F="% sin fracaso")
    estadGen3(datos=estadisticas, tablaEvento="cpre", campoBool="embarazo", totalEvento=cantCPRE, desde=desde, hasta=hasta, label_T="% CPRE con embarazo ", label_F="% sin embarazo")

    return estadisticas
    
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


def reporteCompletoCPRE(desde, hasta, id_historia=0):
    
    if (id_historia==0):
        filtroHistoria = ""
    else: 
        filtroHistoria = " and v.id_historia = :id_historia "

    sql = text("""
                    select v.id, 
                        v.fecha fechaSF,    
                        date_format(v.fecha, "%d/%m/%Y") fecha, h.nombre, date_format(h.nacimiento, "%d/%m/%Y") nacimiento, TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) edad,
                        v.ASA,
                        If(v.ambulatorio,'Si','No') ambulatorio,
                        If(v.cpre_previa, 'Si','No') cpre_previa,
                        v.BILIRRUBINA,
                        v.FAL,
                        v.TGP,
                        v.TGO,
                        v.AMILASA,
                        v.GGT,
                        v.GB,
                        v.id_operador,
                        If(v.FR_DE_PA_SOD, 'Si','No') FR_DE_PA_SOD,
                        If(v.FR_DE_PA_AUSENCIA_PC, 'Si','No') FR_DE_PA_AUSENCIA_PC,
                        If(v.FR_DE_PA_ANTEC_PA, 'Si','No') FR_DE_PA_ANTEC_PA,
                        If(v.CPRE_normal, 'Si','No') CPRE_normal,
                        v.id_CPRE_EPT,
                        If(v.ESFINTEROPLASTIA, 'Si','No') ESFINTEROPLASTIA,
                        v.id_CPRE_WIRSUNG,
                        v.id_CPRE_PRECORTE,
                        v.id_CPRE_Dilatacion_biliar,
                        v.id_CPRE_Litotripsia,
                        v.id_CPRE_stent_plastico,
                        v.id_CPRE_stent_autoexp,
                        If(v.stent_duodenal,'Si','No') stent_duodenal,
                        v.RX_dosis,
                        v.DPA,
                        v.RX_tiempo,
                        v.nro_sesiones,
                        If(v.resolucion_completa, 'Si','No') resolucion_completa,
                        v.id_CPRE_AMILASEMIA_2HS,
                        If(v.canulacion, 'Si','No') canulacion,
                        If(v.biopsias, 'Si','No') biopsias,
                        v.citologia,
                        If(v.fracaso, 'Si','No') fracaso,
                        v.comentarios,
                        If(v.embarazo, 'Si','No') embarazo,
                        v.id_historia,
                        v.fecha,
                        v.hospital_derivacion,
                        ifnull(CPRE_WIRSUNG.descripcion,'') CPRE_WIRSUNG,
                        ifnull(CPRE_PRECORTE.descripcion, '') CPRE_PRECORTE,
                        ifnull(CPRE_Dilatacion_biliar.descripcion, '') CPRE_Dilatacion_biliar,
                        ifnull(CPRE_Litotripsia.descripcion, '') CPRE_Litotripsia,
                        ifnull(CPRE_stent_plastico.descripcion, '') CPRE_stent_plastico,
                        ifnull(CPRE_stent_autoexp.descripcion, '') CPRE_stent_autoexp,
                        ifnull(CPRE_Grado_Asge.descripcion, '') CPRE_grado_asge,
                        ifnull(CPRE_Grado_Dif.descripcion, '') CPRE_grado_dif
                    from 
                    cpre v
                        left outer join historia h on h.id = v.id_historia 
                        left outer join CPRE_EPT on v.id_CPRE_EPT = CPRE_EPT.id
                        left outer join CPRE_WIRSUNG on v.id_CPRE_WIRSUNG = CPRE_WIRSUNG.id
                        left outer join CPRE_PRECORTE on v.id_CPRE_PRECORTE = CPRE_PRECORTE.id
                        left outer join CPRE_Dilatacion_biliar on v.id_CPRE_Dilatacion_biliar = CPRE_Dilatacion_biliar.id
                        left outer join CPRE_Litotripsia on v.id_CPRE_Litotripsia = CPRE_Litotripsia.id
                        left outer join CPRE_stent_plastico on v.id_CPRE_stent_plastico = CPRE_stent_plastico.id
                        left outer join CPRE_stent_autoexp on v.id_CPRE_stent_autoexp = CPRE_stent_autoexp.id
                        left outer join CPRE_AMILASEMIA_2HS on v.id_CPRE_AMILASEMIA_2HS = CPRE_AMILASEMIA_2HS.id
                        left outer join CPRE_Grado_Asge on v.id_cpre_grado_asge = CPRE_Grado_Asge.id
                        left outer join CPRE_Grado_Dif on v.id_cpre_grado_dif = CPRE_Grado_Dif.id
                    WHERE (v.fecha >=:desde ) and (v.fecha <=:hasta )
                """ + filtroHistoria + " Order by v.fecha ")

    if (id_historia==0):
        result = dba.engine.execute(sql, desde=desde, hasta=hasta )
    else:
        result = dba.engine.execute(sql, desde=desde, hasta=hasta, id_historia=id_historia )
            
        
    datos = []
    for fila in result:
        dato =  {       
                        "fecha": (fila["fecha"]).strftime('%d/%m/%Y'),
                        "fechaSF": fila["fechaSF"],
                        "nombre": fila["nombre"],
                        "nacimiento": fila["nacimiento"],
                        "edad": fila["edad"],
                        "ASA": fila["ASA"],
                        "ambulatorio": fila["ambulatorio"],
                        "cpre_previa": fila["cpre_previa"],
                        "BILIRRUBINA": fila["BILIRRUBINA"],
                        "FAL": fila["FAL"],
                        "TGP": fila["TGP"],
                        "TGO": fila["TGO"],
                        "AMILASA": fila["AMILASA"],
                        "GGT": fila["GGT"],
                        "GB": fila["GB"],
                        "id_operador": fila["id_operador"],
                        "FR_DE_PA_SOD": fila["FR_DE_PA_SOD"],
                        "FR_DE_PA_AUSENCIA_PC": fila["FR_DE_PA_AUSENCIA_PC"],
                        "FR_DE_PA_ANTEC_PA": fila["FR_DE_PA_ANTEC_PA"],
                        "CPRE_normal": fila["CPRE_normal"],
                        "id_CPRE_EPT": fila["id_CPRE_EPT"],
                        "ESFINTEROPLASTIA": fila["ESFINTEROPLASTIA"],
                        "id_CPRE_WIRSUNG": fila["id_CPRE_WIRSUNG"],
                        "id_CPRE_PRECORTE": fila["id_CPRE_PRECORTE"],
                        "id_CPRE_Dilatacion_biliar": fila["id_CPRE_Dilatacion_biliar"],
                        "id_CPRE_Litotripsia": fila["id_CPRE_Litotripsia"],
                        "id_CPRE_stent_plastico": fila["id_CPRE_stent_plastico"],
                        "id_CPRE_stent_autoexp": fila["id_CPRE_stent_autoexp"],
                        "stent_duodenal": fila["stent_duodenal"],
                        "RX_dosis": fila["RX_dosis"],
                        "DPA": fila["DPA"],
                        "RX_tiempo": fila["RX_tiempo"],
                        "nro_sesiones": fila["nro_sesiones"],
                        "resolucion_completa": fila["resolucion_completa"],
                        "id_CPRE_AMILASEMIA_2HS": fila["id_CPRE_AMILASEMIA_2HS"],
                        "canulacion": fila["canulacion"],
                        "biopsias": fila["biopsias"],
                        "citologia": fila["citologia"],
                        "fracaso": fila["fracaso"],
                        "comentarios": fila["comentarios"],
                        "embarazo": fila["embarazo"],
                        "id_historia": fila["id_historia"],
                        "hospital_derivacion": fila["hospital_derivacion"],
                        "CPRE_WIRSUNG": fila["CPRE_WIRSUNG"],
                        "CPRE_PRECORTE": fila["CPRE_PRECORTE"],
                        "CPRE_Dilatacion_biliar": fila["CPRE_Dilatacion_biliar"],
                        "CPRE_Litotripsia": fila["CPRE_Litotripsia"],
                        "CPRE_stent_plastico": fila["CPRE_stent_plastico"],
                        "CPRE_stent_autoexp": fila["CPRE_stent_autoexp"],
                        "CPRE_grado_asge": fila["CPRE_grado_asge"],
                        "CPRE_grado_dif": fila["CPRE_grado_dif"],

                        "cirugia_prev": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_cirugia_prev", "cpre_cirugia_prev"), 
                        "coledocolitiasis": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_coledocolitiasis", "cpre_coledocolitiasis"), 
                        "complicaciones": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_complicaciones", "cpre_complicaciones"), 
                        "diverticulo": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_diverticulo", "cpre_diverticulo"), 
                        "eco_abd": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_eco_abd", "cpre_eco_abd"), 
                        "estenosis_alta": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_estenosis_alta", "cpre_estenosis_alta"), 
                        "estenosis_baja": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_estenosis_baja", "cpre_estenosis_baja"), 
                        "eus": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_eus", "cpre_eus"), 
                        #"grado_asge": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_grado_asge", "cpre_grado_asge"), 
                        #"grado_dif": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_grado_dif", "cpre_grado_dif"), 
                        "indicacion": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_indicacion", "cpre_indicacion"), 
                        "indicacion_asge": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_indicacion_asge", "cpre_indicacion_asge"), 
                        "indicacion_ept": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_indicacion_ept", "cpre_indicacion_ept"), 
                        "lpqvb": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_lpqvb", "cpre_lpqvb"), 
                        "miscelaneas": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_miscelaneas", "cpre_miscelaneas"), 
                        "profilaxis_atb": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_profilaxis_atb", "cpre_profilaxis_atb"), 
                        "resolucion_complica": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_resolucion_complica", "cpre_resolucion_complica"), 
                        "rnm": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_rnm", "cpre_rnm"), 
                        "tac": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_tac", "cpre_tac"), 
                        "terap_pancreas": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_terap_pancreas", "cpre_terap_pancreas"), 
                        "transk": concatRefMultiple(fila['id'], "CPRE", "cpre_cpre_transk", "cpre_transk")
                        }
        #agrego la estaditistica correspondiente al elemento de la tabla de referencia
        datos.append(dato) 

    return datos


