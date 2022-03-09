from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from app.models.reporteVCC import *
from app.models.reporteVEDA import *
from app.models.reporteHEPA import *
from app.models.reporteCPRE import *
from app.models.reporteHistoria import *
from datetime import date, timedelta
from app.helpers.auth import authenticated, sess_has_perm
import sys

today = date.today()

def polipos():
    return render_template("reportes/polipos.html")

def vccCompleto_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 

    return render_template("reportes/vcccompleto.html", desde=desde, hasta=hasta, modo = "form")

def vccCompleto():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]

    datos = reporteCompletoVCC(desde, hasta)
    
    return render_template("reportes/vcccompleto.html", datos=datos, modo = "reporte")

def vedaCompleto_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 

    return render_template("reportes/vedacompleto.html", desde=desde, hasta=hasta, modo = "form")

def vedaCompleto():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]

    datos = reporteCompletoVEDA(desde, hasta)
    
    return render_template("reportes/vedacompleto.html", datos=datos, modo = "reporte")

def estadVCC_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    modo = "form"
    
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 
    
    return render_template("reportes/estadEvento.html", desde=desde, hasta=hasta, tipoEv='VCC', modo=modo)

def estadVCC():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]
    estadisticas = reporteEstadisticoVCC(desde, hasta)
    modo = "reporte"
    return render_template("reportes/estadEvento.html", estadisticas = estadisticas, desde=desde, hasta=hasta, tipoEv='VCC', modo=modo)

def estadVEDA_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    modo = "form"
    
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 
    
    return render_template("reportes/estadEvento.html", desde=desde, hasta=hasta, tipoEv='VEDA', modo=modo)

def estadVEDA():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]
    estadisticas = reporteEstadisticoVEDA(desde, hasta)
    modo = "reporte"
    return render_template("reportes/estadEvento.html", estadisticas = estadisticas, desde=desde, hasta=hasta, tipoEv='VEDA', modo=modo)

def vccBoston_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 

    return render_template("reportes/vcc_boston.html", desde=desde, hasta=hasta, modo = "form")

def vccBoston():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]
    valorRef = request.form["valorRef"]

    datos = reporteBostonVCC(desde, hasta, valorRef )
    
    return render_template("reportes/vcc_boston.html", datos=datos, modo = "reporte")

def vccPoliposPac_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 

    return render_template("reportes/vcc_polipos.html", desde=desde, hasta=hasta, modo = "form")

def vccPoliposPac():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]

    datos = reportePoliposVCC(desde, hasta)
    
    return render_template("reportes/vcc_polipos.html", datos=datos, modo = "reporte")

#REPORTE HEPA
def estadHEPA_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    modo = "form"
    
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 
    
    return render_template("reportes/estadEvento.html", desde=desde, hasta=hasta, tipoEv='HEPA', modo=modo)

def estadHEPA():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]
    estadisticas = reporteEstadisticoHEPA(desde, hasta)
    modo = "reporte"
    return render_template("reportes/estadEvento.html", estadisticas = estadisticas, desde=desde, hasta=hasta, tipoEv='HEPA', modo=modo)

def hepaCompleto_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 

    return render_template("reportes/HEPAcompleto.html", desde=desde, hasta=hasta, modo = "form")

def hepaCompleto():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]

    datos = reporteCompletoHEPA(desde, hasta)
    
    return render_template("reportes/HEPAcompleto.html", datos=datos, modo = "reporte")


#reporte cpre
def estadCPRE_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    modo = "form"
    
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 
    
    return render_template("reportes/estadEvento.html", desde=desde, hasta=hasta, tipoEv='CPRE', modo=modo)

def estadCPRE():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]
    estadisticas = reporteEstadisticoCPRE(desde, hasta)
    modo = "reporte"
    return render_template("reportes/estadEvento.html", estadisticas = estadisticas, desde=desde, hasta=hasta, tipoEv='CPRE', modo=modo)

def cpreCompleto_form():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 

    return render_template("reportes/cprecompleto.html", desde=desde, hasta=hasta, modo = "form")

def cpreCompleto():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]

    datos = reporteCompletoCPRE(desde, hasta)
    
    return render_template("reportes/cprecompleto.html", datos=datos, modo = "reporte")

def historiaPeriodo_form(id):
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        flash ("No posee permisos para emitir reportes. Utilice una cuenta con permisos")
    desde = (today - datetime.timedelta(days=90)).strftime("%Y-%m-%d") 
    hasta = today.strftime("%Y-%m-%d") 
    
    historia = Historia.find_by_id(id)

    return render_template("reportes/historia_periodo.html", historia=historia, desde=desde, hasta=hasta, modo = "form")

def historiaPeriodo():
    if ( (not authenticated(session)) or (not sess_has_perm('user_issue_report')) ):
        abort (401)
    desde = request.form["desde"]
    hasta = request.form["hasta"]
    id_historia = request.form["id_historia"]

    historia = Historia.find_by_id(id_historia)
    eventos = reporteHistoriaPeriodo(id_historia, desde, hasta)
    
    return render_template("reportes/historia_periodo.html", historia=historia, eventos=eventos, modo = "reporte")
