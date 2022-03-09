from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from app.models.historia import Historia
from app.models.historia import Sexo
from app.models.confsist import ConfSist
from app.models.user import User
from app.helpers.auth import authenticated, sess_has_perm
from sqlalchemy.orm import relationship
from app.helpers.validadores import analiza_atributos_requeridos
# from app.models.veda import Veda
from app.models.veda import *
from app.models.vcc import *
from app.models.hepatico import *
from app.models.cpre import *
# import app.models.veda
from datetime import date
import sys

today = date.today()


def index():
    return render_template("historialEventos/historialEventos.html")


def veda_new(id_historia):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para crear eventos. Utilice una cuenta con permisos")
      veda = {"id": 0,
                  "id_historia": id_historia,
                  "comentarios":  "",
                  "fecha":  today.strftime("%Y-%m-%d"),
                  "anestesia": False,
                  "id_VEDA_incompleto": 0,
                  "id_VEDA_terapeutica": 0,
                  "id_VEDA_polipectomia_tam": 0,
                  "id_VEDA_polipectomia_material": 0,
                  "id_VEDA_polipectomia_paris": 0,
                  "id_VEDA_biopsia": 0,
                  "id_VEDA_protocolo": 0,
                  "id_VEDA_de_guardia": 0,
                  "id_VEDA_tiempo": 1
                  }

      motivos = Veda_Motivo.all()
      hallazgos = Veda_Hallazgo.all()
      operadores = User.all()
      incompletos = Veda_Incompleto.all()
      terapeuticas = Veda_Terapeutica.all()
      polipectomia_tams = Veda_Polipectomia_Tam.all()
      polipectomia_materiales = Veda_Polipectomia_Material.all()
      polipectomia_paris = Veda_Polipectomia_Paris.all()
      biopsias = Veda_Biopsia.all()
      protocolos = Veda_Protocolo.all()
      de_guardias = Veda_de_Guardia.all()
      tiempos = Veda_Tiempo.all()

      return render_template("historialEventos/cargarVeda.html", veda=veda, motivos=motivos, hallazgos=hallazgos, operadores=operadores, incompletos=incompletos, terapeuticas=terapeuticas, polipectomia_tams=polipectomia_tams, polipectomia_materiales=polipectomia_materiales, polipectomia_paris=polipectomia_paris, biopsias=biopsias, protocolos=protocolos, de_guardias=de_guardias, tiempos=tiempos, form_action="new")


def veda_create():
      if ((not authenticated(session)) or (not sess_has_perm('historia_update'))):
            abort(401)

      errores = []

      data = request.form

      id_historia = data["id_historia"]
      atributos_validar = [("comentarios", "txt", "4000", "Comentarios")
                                    ]
      validacion_ok, errores = analiza_atributos_requeridos(
          atributos_validar, data)

      if (len(errores) == 0):
            result = Veda.create(request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores) == 0):
            return redirect(url_for('historia_edit', id=id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("veda_new", id_historia=id_historia))


def veda_edit(id):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para Editar. Utilice una cuenta con permisos")
      veda = Veda.find_by_id(id)

      motivos = Veda_Motivo.all()
      hallazgos = Veda_Hallazgo.all()

      operadores = User.all()
      incompletos = Veda_Incompleto.all()
      terapeuticas = Veda_Terapeutica.all()
      polipectomia_tams = Veda_Polipectomia_Tam.all()
      polipectomia_materiales = Veda_Polipectomia_Material.all()
      polipectomia_paris = Veda_Polipectomia_Paris.all()
      biopsias = Veda_Biopsia.all()
      protocolos = Veda_Protocolo.all()
      de_guardias = Veda_de_Guardia.all()
      tiempos = Veda_Tiempo.all()

      return render_template("historialEventos/cargarVeda.html", veda=veda, motivos=motivos, motivos_veda=veda.motivos, hallazgos=hallazgos, hallazgos_veda=veda.hallazgos, operadores=operadores, incompletos=incompletos, terapeuticas=terapeuticas, polipectomia_tams=polipectomia_tams, polipectomia_materiales=polipectomia_materiales, polipectomia_paris=polipectomia_paris, biopsias=biopsias, protocolos=protocolos, de_guardias=de_guardias, tiempos=tiempos, form_action="edit")


def veda_modify():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      errores = []

      data = request.form
      evento = Veda.find_by_id(data['id'])

      atributos_validar = [("comentarios", "txt", "4000", "Comentarios")
                        ]

      validacion_ok, errores = analiza_atributos_requeridos(
          atributos_validar, data)

      if (len(errores) == 0):
            result = Veda.modify(evento, request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores) == 0):
            return redirect(url_for("historia_edit", id=evento.id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("veda_edit", id=request.form['id']))


def vcc_new(id_historia):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para crear eventos. Utilice una cuenta con permisos")
      vcc = {"id": 0,
                  "id_historia": id_historia,
                  "comentarios":  "",
                  "fecha":  today.strftime("%Y-%m-%d"),
                  "id_operador": 0,
                  "id_vcc_preparacion": 1,
                  "boston_izq": 0,
                  "boston_trasv": 0,
                  "boston_der": 0,
                  "id_VCC_incompleta_hasta": 0,
                  "id_VCC_incompleta_motivo": 0,
                  "id_VCC_lesion_sospechosa": 0,
                  "id_VCC_polipos_cant": 0,
                  "id_VCC_polipectomia_tam": 0,
                  "id_VCC_polipectomia_material": 0,
                  "id_VCC_polipectomia_tecnica": 0,
                  "id_VCC_polipectomia_paris": 0,
                  "ileoscopia": False,
                  "id_VCC_de_guardia": 0,
                  "id_VCC_tiempo_ingreso": 1,
                  "id_VCC_tiempo_retirada": 1
                  }

      operadores = User.all()
      biopsias = Vcc_Biopsias.all()
      complicaciones = Vcc_Complicaciones.all()
      de_guardias = Vcc_De_Guardia.all()
      hallazgos = Vcc_Hallazgos.all()
      incompleta_hasta = Vcc_Incompleta_Hasta.all()
      incompleta_motivos = Vcc_Incompleta_Motivo.all()
      lesiones_sospechosas = Vcc_Lesion_Sospechosa.all()
      motivos = Vcc_Motivo.all()
      polipectomia_materiales = Vcc_Polipectomia_Material.all()
      polipectomia_paris = Vcc_Polipectomia_Paris.all()
      polipectomia_tams = Vcc_Polipectomia_Tam.all()
      polipectomia_tecnicas = Vcc_Polipectomia_Tecnica.all()
      polipos_cant = Vcc_Polipos_Cant.all()
      preparaciones = Vcc_Preparacion.all()
      terapeuticas = Vcc_Terapeutica.all()
      tiempos_ingreso = Vcc_Tiempo_Ingreso.all()
      tiempos_retirada = Vcc_Tiempo_Retirada.all()

      return render_template("historialEventos/cargarVcc.html", vcc=vcc,
                              biopsias=biopsias,
                              complicaciones=complicaciones,
                              de_guardias=de_guardias,
                              hallazgos=hallazgos,
                              incompleta_hasta=incompleta_hasta,
                              incompleta_motivos=incompleta_motivos,
                              lesiones_sospechosas=lesiones_sospechosas,
                              motivos=motivos,
                              polipectomia_materiales=polipectomia_materiales,
                              polipectomia_paris=polipectomia_paris,
                              polipectomia_tams=polipectomia_tams,
                              polipectomia_tecnicas=polipectomia_tecnicas,
                              polipos_cant=polipos_cant,
                              preparaciones=preparaciones,
                              terapeuticas=terapeuticas,
                              tiempos_ingreso=tiempos_ingreso,
                              tiempos_retirada=tiempos_retirada,
                              operadores=operadores,
                              form_action="new")


def vcc_create():
      if ((not authenticated(session)) or (not sess_has_perm('historia_update'))):
            abort(401)
      errores = []

      data = request.form

      id_historia = data["id_historia"]
      atributos_validar = [    ("comentarios", "txt", "4000", "Comentarios")
                                    ] 
      validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)

      if (len(errores)==0):
            result = Vcc.create(request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores)==0):
            return redirect(url_for('historia_edit',id=id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("vcc_new",id_historia=id_historia))



def vcc_edit(id):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para Editar. Utilice una cuenta con permisos")
      vcc = Vcc.find_by_id(id)
      
      operadores = User.all()
      biopsias = Vcc_Biopsias.all()
      complicaciones = Vcc_Complicaciones.all()
      de_guardias = Vcc_De_Guardia.all()
      hallazgos = Vcc_Hallazgos.all()
      incompleta_hasta = Vcc_Incompleta_Hasta.all()
      incompleta_motivos = Vcc_Incompleta_Motivo.all()
      lesiones_sospechosas = Vcc_Lesion_Sospechosa.all()
      motivos = Vcc_Motivo.all()
      polipectomia_materiales = Vcc_Polipectomia_Material.all()
      polipectomia_paris = Vcc_Polipectomia_Paris.all()
      polipectomia_tams = Vcc_Polipectomia_Tam.all()
      polipectomia_tecnicas = Vcc_Polipectomia_Tecnica.all()
      polipos_cant = Vcc_Polipos_Cant.all()
      preparaciones = Vcc_Preparacion.all()
      terapeuticas = Vcc_Terapeutica.all()
      tiempos_ingreso = Vcc_Tiempo_Ingreso.all()
      tiempos_retirada = Vcc_Tiempo_Retirada.all()

      return render_template("historialEventos/cargarVcc.html", vcc=vcc, 
                              biopsias = biopsias,
                              complicaciones = complicaciones,
                              de_guardias = de_guardias,
                              hallazgos = hallazgos,
                              incompleta_hasta = incompleta_hasta,
                              incompleta_motivos = incompleta_motivos,
                              lesiones_sospechosas = lesiones_sospechosas,
                              motivos = motivos,
                              polipectomia_materiales = polipectomia_materiales,
                              polipectomia_paris = polipectomia_paris,
                              polipectomia_tams = polipectomia_tams,
                              polipectomia_tecnicas = polipectomia_tecnicas,
                              polipos_cant = polipos_cant,
                              preparaciones = preparaciones,
                              terapeuticas = terapeuticas,
                              tiempos_ingreso = tiempos_ingreso,
                              tiempos_retirada = tiempos_retirada,
                              operadores = operadores,
                              biopsias_vcc = vcc.biopsias,
                              complicaciones_vcc = vcc.complicaciones,
                              hallazgos_vcc = vcc.hallazgos,
                              motivos_vcc = vcc.motivos,
                              terapeuticas_vcc = vcc.terapeuticas,
                              form_action="edit")

def vcc_modify():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      errores = []

      data = request.form
      evento = Vcc.find_by_id(data['id'])

      atributos_validar = [     ("comentarios", "txt", "4000", "Comentarios")
                        ]

      validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)
      
      if (len(errores)==0):
            result = Vcc.modify(evento, request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores)==0):
            return redirect(url_for("historia_edit",id=evento.id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("vcc_edit", id=request.form['id']))

def delete_veda_confirma(id):
    """
        Muestra la vista de confirmacion para la eliminacion de un evento
    """
    if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
          flash("No posee permisos para borarr el evento. Utilice una cuenta con permisos")


    evento = Veda.find_by_id(id)
    return render_template("historialEventos/cargarVeda.html", veda=evento, form_action="delete")

def delete_veda():
      """
            busca el evento indicado en un POST e invoca a la clase correspondiente al evento para elimninarlo
      """    
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)

      errores = []

      data = request.form

      evento = Veda.find_by_id(data['id'])
      id_historia = evento.id_historia

      if (evento is None):
            errores.append("El evento no existe")            
      else:
            status = Veda.delete(evento)

      if (not status):
            errores.append("Se produjo un error al eliminar el evento")

      for msg in errores:
            flash(msg)

      return redirect(url_for('historia_edit',id=id_historia))

def delete_vcc_confirma(id):
      """
          Muestra la vista de confirmacion para la eliminacion de un evento
      """
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
          flash("No posee permisos para borarr el evento. Utilice una cuenta con permisos")


      evento = Vcc.find_by_id(id)
      return render_template("historialEventos/cargarVcc.html", vcc=evento, form_action="delete")

def delete_vcc():
      """
            busca el evento indicado en un POST e invoca a la clase correspondiente al evento para elimninarlo
      """    
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
        abort(401)
    
      errores = []

      data = request.form

      evento = Vcc.find_by_id(data['id'])
      id_historia = evento.id_historia

      if (evento is None):
            errores.append("El evento no existe")            
      else:
            status = Vcc.delete(evento)

      if (not status):
            errores.append("Se produjo un error al eliminar el evento")

      for msg in errores:
            flash(msg)

      return redirect(url_for('historia_edit',id=id_historia))

def createCpre():
      return render_template("historialEventos/cargarCpre.html")

def createHepatico():
      return render_template("historialEventos/cargarHepatico.html")


#  eventos hepaticos
def hepa_new(id_historia):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para crear eventos. Utilice una cuenta con permisos")     
      hepa = {    "id": 0,
                  "id_historia": id_historia,
                  "fecha":  today.strftime("%Y-%m-%d"),
                  "id_HEPA_descompensacion": 0,
                  "id_HEPA_child_pugh": 0,
                  "id_operador" : 0,
                  "consultorio" : False, 
                  "hepatocarcinoma" : False ,
                  "lesion_focal_hepatica" : False
                  }
      etiologia = Hepa_Etiologia.all()
      cirrosis_etiologia = Hepa_Cirrosis_Etiologia.all()
      operadores = User.all()
      descompensacion = Hepa_Descompensacion.all()
      child_pugh = Hepa_child_pugh.all()
      return render_template("historialEventos/cargarHepatico.html",
            hepa=hepa, 
            etiologia=etiologia,
            cirrosis_etiologia = cirrosis_etiologia,
            operadores=operadores, 
            descompensacion= descompensacion, 
            child_pugh= child_pugh, 
            form_action="new")

def hepa_create():
      if ((not authenticated(session)) or (not sess_has_perm('historia_update'))):
            abort(401)

      errores = []

      data = request.form

      id_historia = data["id_historia"]
      
      # atributos_validar = [    ("comentarios", "txt", "4000", "Comentarios")
      #                               ] 
      # validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)

      if (len(errores)==0):
            result = Hepa.create(request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores)==0):
            return redirect(url_for('historia_edit',id=id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("hepa_new",id_historia=id_historia))


def hepa_edit(id):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para Editar. Utilice una cuenta con permisos")
      hepa = Hepa.find_by_id(id)
      print(hepa.id_HEPA_child_pugh, file=sys.stderr)

      descompensacion=Hepa_Descompensacion.all()
      child_pugh=Hepa_child_pugh.all()
      etiologia = Hepa_Etiologia.all()
      cirrosis_etiologia = Hepa_Cirrosis_Etiologia.all()
      operadores = User.all()

      return render_template("historialEventos/cargarHepatico.html", 
            hepa=hepa, 
            descompensacion=descompensacion, 
            child_pugh=child_pugh, 
            operadores=operadores,
            etiologia = etiologia,
            cirrosis_etiologia = cirrosis_etiologia,
            etiologia_hepa = hepa.etiologias,
            cirrosis_etiologia_hepa = hepa.cirrosis_etiologias, 
            form_action="edit")

def hepa_modify():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      errores = []

      data = request.form
      evento = Hepa.find_by_id(data['id'])

      # atributos_validar = [     ("comentarios", "txt", "4000", "Comentarios")
      #                   ]

      # validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)
      
      if (len(errores)==0):
            result = Hepa.modify(evento, request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores)==0):
            return redirect(url_for("historia_edit",id=evento.id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("hepa_edit", id=request.form['id']))

def delete_hepa_confirma(id):
      """
        Muestra la vista de confirmacion para la eliminacion de un evento
      """
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
          flash("No posee permisos para borarr el evento. Utilice una cuenta con permisos")


      evento = Hepa.find_by_id(id)
      return render_template("historialEventos/cargarHepatico.html", hepa=evento, form_action="delete")

def delete_hepa():
      """
            busca el evento indicado en un POST e invoca a la clase correspondiente al evento para elimninarlo
      """    
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
        abort(401)
    
      errores = []

      data = request.form

      evento = Hepa.find_by_id(data['id'])
      id_historia = evento.id_historia

      if (evento is None):
            errores.append("El evento no existe")            
      else:
            status = Hepa.delete(evento)

      if (not status):
            errores.append("Se produjo un error al eliminar el evento")

      for msg in errores:
            flash(msg)

      return redirect(url_for('historia_edit',id=id_historia))


def cpre_new(id_historia):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para crear eventos. Utilice una cuenta con permisos")
      operadores = User.all()
      amilasemia_2hs = Cpre_Amilasemia_2hs.all()
      asa = Cpre_Asa.all()
      cirugia_prev = Cpre_Cirugia_Prev.all()
      coledocolitiasis = Cpre_Coledocolitiasis.all()
      complicaciones = Cpre_Complicaciones.all()
      dilatacion_biliar = Cpre_Dilatacion_Biliar.all()
      diverticulo = Cpre_Diverticulo.all()
      eco_abd = Cpre_Eco_Abd.all()
      ept = Cpre_Ept.all()
      estenosis_alta = Cpre_Estenosis_Alta.all()
      estenosis_baja = Cpre_Estenosis_Baja.all()
      eus = Cpre_Eus.all()
      grado_asge = Cpre_Grado_Asge.all()
      grado_dif = Cpre_Grado_Dif.all()
      indicacion = Cpre_Indicacion.all()
      indicacion_asge = Cpre_Indicacion_Asge.all()
      indicacion_ept = Cpre_Indicacion_Ept.all()
      litotripsia = Cpre_Litotripsia.all()
      lpqvb = Cpre_Lpqvb.all()
      miscelaneas = Cpre_Miscelaneas.all()
      precorte = Cpre_Precorte.all()
      profilaxis_atb = Cpre_Profilaxis_Atb.all()
      resolucion_complica = Cpre_Resolucion_Complica.all()
      rnm = Cpre_Rnm.all()
      stent_autoexp = Cpre_Stent_Autoexp.all()
      stent_plastico = Cpre_Stent_Plastico.all()
      tac = Cpre_Tac.all()
      terap_pancreas = Cpre_Terap_Pancreas.all()
      transk = Cpre_Transk.all()
      wirsung = Cpre_Wirsung.all()


      cpre = {    "id": 0,
                  "id_historia": id_historia,
                  "comentarios":  "",
                  "fecha":  today.strftime("%Y-%m-%d"),
                  "ASA": 0,
                  "nro_sesiones": 0,
                  "id_cpre_grado_asge": 0,
                  "id_cpre_grado_dif": 0
            }

      return render_template("historialEventos/cargarCpre.html", 
                              cpre=cpre,
                              operadores=operadores,
                              amilasemia_2hs = amilasemia_2hs,
                              asa = asa,
                              cirugia_prev = cirugia_prev,
                              coledocolitiasis = coledocolitiasis,
                              complicaciones = complicaciones,
                              dilatacion_biliar = dilatacion_biliar,
                              diverticulo = diverticulo,
                              eco_abd = eco_abd,
                              ept = ept,
                              estenosis_alta = estenosis_alta,
                              estenosis_baja = estenosis_baja,
                              eus = eus,
                              grado_asge = grado_asge,
                              grado_dif = grado_dif,
                              indicacion = indicacion,
                              indicacion_asge = indicacion_asge,
                              indicacion_ept = indicacion_ept,
                              litotripsia = litotripsia,
                              lpqvb = lpqvb,
                              miscelaneas = miscelaneas,
                              precorte = precorte,
                              profilaxis_atb = profilaxis_atb,
                              resolucion_complica = resolucion_complica,
                              rnm = rnm,
                              stent_autoexp = stent_autoexp,
                              stent_plastico = stent_plastico,
                              tac = tac,
                              terap_pancreas = terap_pancreas,
                              transk = transk,
                              wirsung = wirsung,

                              form_action="new")

def cpre_create():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      errores = []

      data = request.form

      id_historia = data["id_historia"]
      atributos_validar = [    ("comentarios", "txt", "4000", "Comentarios")
                                    ] 
      validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)

      if (len(errores)==0):
            result = Cpre.create(request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores)==0):
            return redirect(url_for('historia_edit',id=id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("cpre_new",id_historia=id_historia))

def cpre_edit(id):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("No posee permisos para Editar. Utilice una cuenta con permisos")
      cpre = Cpre.find_by_id(id)

      operadores = User.all()
      amilasemia_2hs = Cpre_Amilasemia_2hs.all()
      asa = Cpre_Asa.all()
      cirugia_prev = Cpre_Cirugia_Prev.all()
      coledocolitiasis = Cpre_Coledocolitiasis.all()
      complicaciones = Cpre_Complicaciones.all()
      dilatacion_biliar = Cpre_Dilatacion_Biliar.all()
      diverticulo = Cpre_Diverticulo.all()
      eco_abd = Cpre_Eco_Abd.all()
      ept = Cpre_Ept.all()
      estenosis_alta = Cpre_Estenosis_Alta.all()
      estenosis_baja = Cpre_Estenosis_Baja.all()
      eus = Cpre_Eus.all()
      grado_asge = Cpre_Grado_Asge.all()
      grado_dif = Cpre_Grado_Dif.all()
      indicacion = Cpre_Indicacion.all()
      indicacion_asge = Cpre_Indicacion_Asge.all()
      indicacion_ept = Cpre_Indicacion_Ept.all()
      litotripsia = Cpre_Litotripsia.all()
      lpqvb = Cpre_Lpqvb.all()
      miscelaneas = Cpre_Miscelaneas.all()
      precorte = Cpre_Precorte.all()
      profilaxis_atb = Cpre_Profilaxis_Atb.all()
      resolucion_complica = Cpre_Resolucion_Complica.all()
      rnm = Cpre_Rnm.all()
      stent_autoexp = Cpre_Stent_Autoexp.all()
      stent_plastico = Cpre_Stent_Plastico.all()
      tac = Cpre_Tac.all()
      terap_pancreas = Cpre_Terap_Pancreas.all()
      transk = Cpre_Transk.all()
      wirsung = Cpre_Wirsung.all()

      cirugia_prev_list = cpre.cirugia_prev_list
      coledocolitiasis_list = cpre.coledocolitiasis_list
      complicaciones_list = cpre.complicaciones_list
      diverticulo_list = cpre.diverticulo_list
      eco_abd_list = cpre.eco_abd_list
      estenosis_alta_list = cpre.estenosis_alta_list
      estenosis_baja_list = cpre.estenosis_baja_list
      eus_list = cpre.eus_list
      #grado_asge_list = cpre.grado_asge_list
      #grado_dif_list = cpre.grado_dif_list
      indicacion_list = cpre.indicacion_list
      indicacion_asge_list = cpre.indicacion_asge_list
      indicacion_ept_list = cpre.indicacion_ept_list
      lpqvb_list = cpre.lpqvb_list
      miscelaneas_list = cpre.miscelaneas_list
      profilaxis_atb_list = cpre.profilaxis_atb_list
      resolucion_complica_list = cpre.resolucion_complica_list
      rnm_list = cpre.rnm_list
      tac_list = cpre.tac_list
      terap_pancreas_list = cpre.terap_pancreas_list
      transk_list = cpre.transk_list

      return render_template("historialEventos/cargarCpre.html", 
                              cpre=cpre,
                              operadores=operadores,
                              amilasemia_2hs = amilasemia_2hs,
                              asa = asa,
                              cirugia_prev = cirugia_prev,
                              coledocolitiasis = coledocolitiasis,
                              complicaciones = complicaciones,
                              dilatacion_biliar = dilatacion_biliar,
                              diverticulo = diverticulo,
                              eco_abd = eco_abd,
                              ept = ept,
                              estenosis_alta = estenosis_alta,
                              estenosis_baja = estenosis_baja,
                              eus = eus,
                              grado_asge = grado_asge,
                              grado_dif = grado_dif,
                              indicacion = indicacion,
                              indicacion_asge = indicacion_asge,
                              indicacion_ept = indicacion_ept,
                              litotripsia = litotripsia,
                              lpqvb = lpqvb,
                              miscelaneas = miscelaneas,
                              precorte = precorte,
                              profilaxis_atb = profilaxis_atb,
                              resolucion_complica = resolucion_complica,
                              rnm = rnm,
                              stent_autoexp = stent_autoexp,
                              stent_plastico = stent_plastico,
                              tac = tac,
                              terap_pancreas = terap_pancreas,
                              transk = transk,
                              wirsung = wirsung,

                              cirugia_prev_list = cirugia_prev_list,
                              coledocolitiasis_list = coledocolitiasis_list,
                              complicaciones_list = complicaciones_list,
                              diverticulo_list = diverticulo_list,
                              eco_abd_list = eco_abd_list,
                              estenosis_alta_list = estenosis_alta_list,
                              estenosis_baja_list = estenosis_baja_list,
                              eus_list = eus_list,
                              #grado_asge_list = grado_asge_list,
                              #grado_dif_list = grado_dif_list,
                              indicacion_list = indicacion_list,
                              indicacion_asge_list = indicacion_asge_list,
                              indicacion_ept_list = indicacion_ept_list,
                              lpqvb_list = lpqvb_list,
                              miscelaneas_list = miscelaneas_list,
                              profilaxis_atb_list = profilaxis_atb_list,
                              resolucion_complica_list = resolucion_complica_list,
                              rnm_list = rnm_list,
                              tac_list = tac_list,
                              terap_pancreas_list = terap_pancreas_list,
                              transk_list = transk_list,

                              form_action="edit")

def cpre_modify():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      errores = []

      data = request.form
      evento = Cpre.find_by_id(data['id'])

      atributos_validar = [     ("comentarios", "txt", "4000", "Comentarios")
                        ]

      validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)
      
      if (len(errores)==0):
            result = Cpre.modify(evento, request.form)
            if (not result):
                  errores.append('Error al grabar el evento')

      if (len(errores)==0):
            return redirect(url_for("historia_edit",id=evento.id_historia))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("cpre_edit", id=request.form['id']))

def delete_cpre_confirma(id):
      """
            Muestra la vista de confirmacion para la eliminacion de un evento
      """
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
          flash("No posee permisos para borarr el evento. Utilice una cuenta con permisos")


      cpre = Cpre.find_by_id(id)
      operadores = User.all()
      amilasemia_2hs = Cpre_Amilasemia_2hs.all()
      asa = Cpre_Asa.all()
      cirugia_prev = Cpre_Cirugia_Prev.all()
      coledocolitiasis = Cpre_Coledocolitiasis.all()
      complicaciones = Cpre_Complicaciones.all()
      dilatacion_biliar = Cpre_Dilatacion_Biliar.all()
      diverticulo = Cpre_Diverticulo.all()
      eco_abd = Cpre_Eco_Abd.all()
      ept = Cpre_Ept.all()
      estenosis_alta = Cpre_Estenosis_Alta.all()
      estenosis_baja = Cpre_Estenosis_Baja.all()
      eus = Cpre_Eus.all()
      grado_asge = Cpre_Grado_Asge.all()
      grado_dif = Cpre_Grado_Dif.all()
      indicacion = Cpre_Indicacion.all()
      indicacion_asge = Cpre_Indicacion_Asge.all()
      indicacion_ept = Cpre_Indicacion_Ept.all()
      litotripsia = Cpre_Litotripsia.all()
      lpqvb = Cpre_Lpqvb.all()
      miscelaneas = Cpre_Miscelaneas.all()
      precorte = Cpre_Precorte.all()
      profilaxis_atb = Cpre_Profilaxis_Atb.all()
      resolucion_complica = Cpre_Resolucion_Complica.all()
      rnm = Cpre_Rnm.all()
      stent_autoexp = Cpre_Stent_Autoexp.all()
      stent_plastico = Cpre_Stent_Plastico.all()
      tac = Cpre_Tac.all()
      terap_pancreas = Cpre_Terap_Pancreas.all()
      transk = Cpre_Transk.all()
      wirsung = Cpre_Wirsung.all()

      cirugia_prev_list = cpre.cirugia_prev_list
      coledocolitiasis_list = cpre.coledocolitiasis_list
      complicaciones_list = cpre.complicaciones_list
      diverticulo_list = cpre.diverticulo_list
      eco_abd_list = cpre.eco_abd_list
      estenosis_alta_list = cpre.estenosis_alta_list
      estenosis_baja_list = cpre.estenosis_baja_list
      eus_list = cpre.eus_list
      #grado_asge_list = cpre.grado_asge_list
      #grado_dif_list = cpre.grado_dif_list
      indicacion_list = cpre.indicacion_list
      indicacion_asge_list = cpre.indicacion_asge_list
      indicacion_ept_list = cpre.indicacion_ept_list
      lpqvb_list = cpre.lpqvb_list
      miscelaneas_list = cpre.miscelaneas_list
      profilaxis_atb_list = cpre.profilaxis_atb_list
      resolucion_complica_list = cpre.resolucion_complica_list
      rnm_list = cpre.rnm_list
      tac_list = cpre.tac_list
      terap_pancreas_list = cpre.terap_pancreas_list
      transk_list = cpre.transk_list

      return render_template("historialEventos/cargarCpre.html", cpre=cpre,
                              operadores = operadores, 
                              amilasemia_2hs = amilasemia_2hs,
                              asa = asa,
                              cirugia_prev = cirugia_prev,
                              coledocolitiasis = coledocolitiasis,
                              complicaciones = complicaciones,
                              dilatacion_biliar = dilatacion_biliar,
                              diverticulo = diverticulo,
                              eco_abd = eco_abd,
                              ept = ept,
                              estenosis_alta = estenosis_alta,
                              estenosis_baja = estenosis_baja,
                              eus = eus,
                              grado_asge = grado_asge,
                              grado_dif = grado_dif,
                              indicacion = indicacion,
                              indicacion_asge = indicacion_asge,
                              indicacion_ept = indicacion_ept,
                              litotripsia = litotripsia,
                              lpqvb = lpqvb,
                              miscelaneas = miscelaneas,
                              precorte = precorte,
                              profilaxis_atb = profilaxis_atb,
                              resolucion_complica = resolucion_complica,
                              rnm = rnm,
                              stent_autoexp = stent_autoexp,
                              stent_plastico = stent_plastico,
                              tac = tac,
                              terap_pancreas = terap_pancreas,
                              transk = transk,
                              wirsung = wirsung,

                              cirugia_prev_list = cirugia_prev_list,
                              coledocolitiasis_list = coledocolitiasis_list,
                              complicaciones_list = complicaciones_list,
                              diverticulo_list = diverticulo_list,
                              eco_abd_list = eco_abd_list,
                              estenosis_alta_list = estenosis_alta_list,
                              estenosis_baja_list = estenosis_baja_list,
                              eus_list = eus_list,
                              #grado_asge_list = grado_asge_list,
                              #grado_dif_list = grado_dif_list,
                              indicacion_list = indicacion_list,
                              indicacion_asge_list = indicacion_asge_list,
                              indicacion_ept_list = indicacion_ept_list,
                              lpqvb_list = lpqvb_list,
                              miscelaneas_list = miscelaneas_list,
                              profilaxis_atb_list = profilaxis_atb_list,
                              resolucion_complica_list = resolucion_complica_list,
                              rnm_list = rnm_list,
                              tac_list = tac_list,
                              terap_pancreas_list = terap_pancreas_list,
                              transk_list = transk_list,

                              form_action="delete")

def delete_cpre():
      """
            busca el evento indicado en un POST e invoca a la clase correspondiente al evento para elimninarlo
      """    
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
        abort(401)
    
      errores = []

      data = request.form

      evento = Cpre.find_by_id(data['id'])
      id_historia = evento.id_historia

      if (evento is None):
            errores.append("El evento no existe")            
      else:
            status = Cpre.delete(evento)

      if (not status):
            errores.append("Se produjo un error al eliminar el evento")

      for msg in errores:
            flash(msg)

      return redirect(url_for('historia_edit',id=id_historia))
