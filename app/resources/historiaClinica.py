from flask import redirect, render_template, request, url_for, abort, session, flash
from app.db import connection
from app.models.historia import Historia
from app.models.historia import Sexo
from app.models.confsist import ConfSist
from app.helpers.auth import authenticated, sess_has_perm
from app.helpers.validadores import analiza_atributos_requeridos
from sqlalchemy.orm import relationship
from datetime import date

today = date.today()

def new():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("Solo se tiene permisos para visualizar")
      #creo historia vacia
      historia= {
                  "nombre":  "",
                  "dni":  "",
                  "id_sexo":  1,
                  "nacimiento":  today.strftime("%Y-%m-%d"),
                  }      
      sexos = Sexo.all()
      
      return render_template("historialEventos/historialEventos.html", historia=historia, sexos=sexos, form_action="new")

def create():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      errores = []

      data = request.form

      atributos_validar = [    ("nombre", "txt", "255", "Nombre")
                        ]

      validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)

      if (len(errores)==0):
            result = Historia.create(request.form)
            if (not result):
                  errores.append('Error al grabar la historia clinica')

      if (len(errores)==0):
            #return redirect(url_for("historia_index"))
            return redirect(url_for('historia_edit',id=result.id))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("historia_new"))


def edit(id):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("Solo se tiene permisos para visualizar")
      historia = Historia.find_by_id(id)
      sexos = Sexo.all()
      eventos = historia.getEncabezadosEventos()
      return render_template("historialEventos/historialEventos.html", historia=historia, sexos=sexos, eventos=eventos, form_action="edit")

def edit_estado(id):
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      historia = Historia.find_by_id(id)
      Historia.cambiar_estado(historia)
      return redirect(url_for("historia_index"))

def modify():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            abort(401)
      errores = []

      data = request.form

      historia = Historia.find_by_id(data['id'])

      atributos_validar = [    ("nombre", "txt", "255", "Nombre")
                        ]

      validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, data)

      if (len(errores)==0):
            result = Historia.modify(historia, request.form)
            if (not result):
                  errores.append('Error al grabar la historia clinica')

      if (len(errores)==0):
            return redirect(url_for("historia_index"))
      else:
            for msg in errores:
                  flash(msg)
            return redirect(url_for("historia_edit", id=request.form['id']))



def browse():
      if ( (not authenticated(session)) or (not sess_has_perm('historia_update')) ):
            flash ("Solo se tiene permisos para visualizar")
      session['busqueda_nombre'] = ""    #por defecto muestro todos
      session['activos'] = "T"            #

      try:
            data = request.form
            busqueda_nombre = data['busqueda_nombre']
            activos = data['activos']
      except:
            busqueda_nombre = ""
            activos = "A"

      session['busqueda_nombre'] = busqueda_nombre
      session['activos'] = activos
      

      conf = ConfSist.getConfig()
      por_pagina = conf.cantidad_registros_x_pagina
      pagina = 1

      pages = Historia.browse(busqueda_nombre, activos, pagina, por_pagina)
      historias = pages.items

      if (pages.has_next):
            proxima = pages.next_num
      else:
            proxima = 0

      if (pages.has_prev):
            previa = pages.prev_num
      else:
            previa = 0

      return render_template("pacientes/historiaClinica.html", historias=historias, proxima=proxima, previa=previa, activos=activos, busqueda_nombre=busqueda_nombre)

def browse_pagina(pagina):
      #if ( (not authenticated(session)) or (not sess_has_perm('centro_index')) ):
      #   abort(401)

      pagina = int(pagina)
      busqueda_nombre = session['busqueda_nombre']
      activos = session['activos']

      conf = ConfSist.getConfig()
      por_pagina = conf.cantidad_registros_x_pagina

      pages = Historia.browse(busqueda_nombre, activos, pagina, por_pagina)
      historias = pages.items

      if (pages.has_next):
            proxima = pages.next_num
      else:
            proxima = 0

      if (pages.has_prev):
            previa = pages.prev_num
      else:
            previa = 0

      return render_template("pacientes/historiaClinica.html", historias=historias, proxima=proxima, previa=previa, busqueda_nombre=busqueda_nombre,  activos=activos)
