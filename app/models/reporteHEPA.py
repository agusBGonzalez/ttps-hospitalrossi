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

def reporteEstadisticoHEPA(desde, hasta):
    estadisticas = []

    sql = text("SELECT count(1) cant FROM hepa h where (h.fecha >=:desde) and  (h.fecha <=:hasta)")
    result = dba.engine.execute(sql, desde=desde, hasta=hasta)

    fila = result.fetchone()
    cantHEPA = fila["cant"]

    ############################################################################################################################################
    sql = text("""
                select count(1) cant
                from 
                hepa h 
                where (h.consultorio )
                and (h.fecha >=:desde ) and (h.fecha <=:hasta )
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )    
    fila = result.fetchone()
    cant = fila["cant"]
    estadistica =  {
                    "label": "% de eventos hepáticos por consultorio",
                    "data": round(cant * 100 / cantHEPA,2)
                    }
    estadisticas.append(estadistica) 

    ############################################################################################################################################
    sql = text("""
                select count(1) cant
                from 
                hepa h 
                where (h.hepatocarcinoma )
                and (h.fecha >=:desde ) and (h.fecha <=:hasta )
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )    
    fila = result.fetchone()
    cant = fila["cant"]
    estadistica =  {
                    "label": "% Hepatocarcinoma",
                    "data": round(cant * 100 / cantHEPA,2)
                    }
    estadisticas.append(estadistica) 

    ############################################################################################################################################
    sql = text("""
                select count(1) cant
                from 
                hepa h 
                where (h.lesion_focal_hepatica )
                and (h.fecha >=:desde ) and (h.fecha <=:hasta )
                """)
    result = dba.engine.execute(sql, desde=desde, hasta=hasta )    
    fila = result.fetchone()
    cant = fila["cant"]
    estadistica =  {
                    "label": "% lesion_focal_hepatica",
                    "data": round(cant * 100 / cantHEPA,2)
                    }
    estadisticas.append(estadistica) 

    estadGen1(estadisticas, 'HEPA', 'hepa_child_pugh', cantHEPA, desde, hasta, "% hepa_child_pugh de tipo ", "% hepa_child_pugh sobre total HEPA")
    estadGen2(estadisticas, 'HEPA', 'hepa_etiologia', 'hepa_hepa_etiologia', cantHEPA, desde, hasta, "% de etiologia de tipo ", "% etiologia sobre total HEPA ")
    estadGen1(estadisticas, 'HEPA', 'hepa_child_pugh', cantHEPA, desde, hasta, "% hepa_child_pugh de tipo ", "% hepa_child_pugh sobre total HEPA")
    estadGen2(estadisticas, 'HEPA', 'hepa_cirrosis_etiologia', 'hepa_hepa_cirrosis_etiologia', cantHEPA, desde, hasta, "% de etiologia (cirrosis) de tipo ", "% etiologia (cirrosis) sobre total HEPA ")
    estadGen1(estadisticas, 'HEPA', 'hepa_descompensacion', cantHEPA, desde, hasta, "% descompensacion de tipo ", "% descompensacion sobre total HEPA")




  
    return estadisticas

###########################################################################################################################################

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

def reporteCompletoHEPA(desde, hasta, id_historia=0):
    if (id_historia==0):
        filtroHistoria = ""
    else: 
        filtroHistoria = " and h.id_historia = :id_historia "

    sql = text("""
                select 
                    v.id,
                    v.fecha fechaSF,    
                    date_format(v.fecha, "%d/%m/%Y") fecha, h.nombre, date_format(h.nacimiento, "%d/%m/%Y") nacimiento, TIMESTAMPDIFF(YEAR,h.nacimiento,CURDATE()) edad,
                    If(h.activa, 'Si','No') activa,
                    If(v.consultorio, 'Si','No') consultorio,
                    ifnull(hepa_child_pugh.descripcion,'') hepa_child_pugh,
                    ifnull(hepa_descompensacion.descripcion,'') hepa_descompensacion,
                    if(v.hepatocarcinoma, 'Si','No') hepatocarcinoma, 
                    if(v.lesion_focal_hepatica, 'Si','No') lesion_focal_hepatica, 
                    v.meld 
                from 
                    hepa v
                    inner join historia h on h.id = v.id_historia 
                    left outer join hepa_child_pugh on v.id_HEPA_child_pugh = hepa_child_pugh.id
                    left outer join hepa_descompensacion on v.id_HEPA_descompensacion = hepa_descompensacion.id 
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
                        "activa": fila["activa"],
                        "consultorio": fila["consultorio"],
                        "hepa_child_pugh": fila["hepa_child_pugh"],
                        "hepa_descompensacion": fila["hepa_descompensacion"],
                        "hepatocarcinoma": fila["hepatocarcinoma"],
                        "lesion_focal_hepatica": fila["lesion_focal_hepatica"],
                        "meld": fila["meld"],
                        "cirrosis_etiologia": concatRefMultiple(fila['id'], "HEPA", "hepa_hepa_cirrosis_etiologia", "hepa_cirrosis_etiologia"),
                        "etiologia": concatRefMultiple(fila['id'], "HEPA", "hepa_hepa_etiologia", "hepa_etiologia"),
                        }
        #agrego la estaditistica correspondiente al elemento de la tabla de referencia
        datos.append(dato) 

    return datos