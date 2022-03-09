from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import text
from datetime import date
from app.models.historia import Historia, Sexo
from app.models.reporteCPRE import reporteCompletoCPRE
from app.models.reporteVEDA import reporteCompletoVEDA
from app.models.reporteVCC import reporteCompletoVCC
#from app.models.reporteHEPA import reporteCompletoHEPA

import sys

dba = SQLAlchemy()



def reporteHistoriaPeriodo(id_historia, desde, hasta):

    datosCPRE = reporteCompletoCPRE(desde, hasta, id_historia)
    datosVEDA = reporteCompletoVEDA(desde, hasta, id_historia)
    datosVCC = reporteCompletoVCC(desde, hasta, id_historia)

    datos = []

    size_CPRE = len(datosCPRE)
    size_VEDA = len(datosVEDA)
    size_VCC = len(datosVCC)

    
    i, j, k = 0, 0, 0

    while (i < size_CPRE) and (j < size_VEDA) and (k < size_VCC) :

        datoCPRE = datosCPRE[i]
        datoVEDA = datosVEDA[j]
        datoVCC = datosVCC[k]
        
        #print('paso', file=sys.stderr)    

        if (datoCPRE["fechaSF"] < datoVEDA["fechaSF"]) and (datoCPRE["fechaSF"] < datoVCC["fechaSF"]):
            datoCPRE["tipoEv"] = "CPRE"
            datos.append(datoCPRE)
            i += 1
        elif (datoVEDA["fechaSF"] < datoCPRE["fechaSF"]) and (datoVEDA["fechaSF"] < datoVCC["fechaSF"]):    
            datoVEDA["tipoEv"] = "VEDA"
            datos.append(datoVEDA)
            j += 1
        else:
            datoVCC["tipoEv"] = "VCC"
            datos.append(datoVCC)
            k += 1

 
    while (i < size_CPRE) and (j < size_VEDA):
        datoCPRE = datosCPRE[i]
        datoVEDA = datosVEDA[j]

        if (datoCPRE["fechaSF"] < datoVEDA["fechaSF"]) :
            datoCPRE["tipoEv"] = "CPRE"
            datos.append(datoCPRE)
            i += 1
        else:
            datoVEDA["tipoEv"] = "VEDA"
            datos.append(datoVEDA)
            j += 1

    while (j < size_VEDA) and (k < size_VCC) :
        
        datoVEDA = datosVEDA[j]
        datoVCC = datosVCC[k]

        if (datoVEDA["fechaSF"] < datoVCC["fechaSF"]):    
            datoVEDA["tipoEv"] = "VEDA"
            datos.append(datoVEDA)
            j += 1
        else:
            datoVCC["tipoEv"] = "VCC"
            datos.append(datoVCC)
            k += 1

    while (i < size_CPRE) and (k < size_VCC):
        datoCPRE = datosCPRE[i]
        datoVCC = datosVCC[k]

        print(datoCPRE["fechaSF"], file=sys.stderr) 
        print(datoVCC["fechaSF"], file=sys.stderr) 

        if (datoCPRE["fechaSF"] < datoVCC["fechaSF"]) :
            datoCPRE["tipoEv"] = "CPRE"
            datos.append(datoCPRE)
            i += 1
        else:
            datoVCC["tipoEv"] = "VCC"
            datos.append(datoVCC)
            k += 1

    while (i < size_CPRE):
        datoCPRE = datosCPRE[i]
        datoCPRE["tipoEv"] = "CPRE"
        datos.append(datoCPRE)
        i += 1

    while (j < size_VEDA):
        datoVEDA = datosVEDA[j]
        datoVEDA["tipoEv"] = "VEDA"
        datos.append(datoVEDA)
        j += 1

    while (k < size_VCC):
        datoVCC = datosVCC[k]
        datoVCC["tipoEv"] = "VCC"
        datos.append(datoVCC)
        k += 1


    print('Size datos', file=sys.stderr)
    print(len(datos), file=sys.stderr)

    return datos

