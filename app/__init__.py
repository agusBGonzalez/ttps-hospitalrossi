from os import path, environ
from flask import Flask, render_template, g
from flask_session import Session
from flask import current_app
from flask import cli
from config import config
from app import db
from app.resources import user
from app.resources import historialDeEventos
from app.resources import historiaClinica
from app.resources import reporte
from app.resources import rol
from app.resources import auth
from app.resources import confsist
from app.helpers import handler
from app.helpers import auth as helper_auth
from flask import Flask, render_template, request, session
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api
from flask_cors import CORS

def create_app(environment="development"):
    # Configuración inicial de la app
    app = Flask(__name__)

    # Carga de la configuración
    env = environ.get("FLASK_ENV", environment)
    app.config.from_object(config[env])

    # Server Side session
    app.config["SESSION_TYPE"] = "filesystem"
    Session(app)

    # Flask-Restful
    api = Api(app)
    
    # Habilito CORS
    CORS(app)
    
    # Configure db
    #db.init_app(app)
    app.config["SQLALCHEMY_DATABASE_URI"] = app.config["DB_ALCH"]
    app.config["SQLALCHEMY_POOL_TIMEOUT"] = 2
    dba = SQLAlchemy(app)

    # Funciones que se exportan al contexto de Jinja2
    app.jinja_env.globals.update(is_authenticated=helper_auth.authenticated)
    app.jinja_env.globals.update(current_user=helper_auth.current_user)
    app.jinja_env.globals.update(current_user_is_admin=helper_auth.current_user_is_admin)

    # Autenticación
    app.add_url_rule("/iniciar_sesion", "auth_login", auth.login)
    app.add_url_rule("/cerrar_sesion", "auth_logout", auth.logout)
    app.add_url_rule(
        "/autenticacion", "auth_authenticate", auth.authenticate, methods=["POST"]
    )

    # Rutas de Roles
    app.add_url_rule("/rol/permisos/<id>", "rol_permisos", rol.permisos)
    app.add_url_rule("/rol/tiene_permiso/<id>/<nombre_permiso>", "rol_tiene_permiso", rol.tiene_permiso)

    # Rutas de Usuarios
    app.add_url_rule("/usuarios", "user_index", user.index)
    app.add_url_rule("/usuarios/listar", "user_listar", user.listar)
    app.add_url_rule("/usuarios/browse", "user_browse", user.browse, methods=["POST"])
    app.add_url_rule("/usuarios/browse/<pagina>", "user_pagina", user.browse_pagina)
    app.add_url_rule("/usuarios", "user_create", user.create, methods=["POST"])
    app.add_url_rule("/usuarios/nuevo", "user_new", user.new)
    app.add_url_rule("/usuarios/borrar", "user_delete", user.delete, methods=["POST"])
    app.add_url_rule("/usuarios/conf_borrar/<id>", "user_delete_confirma", user.delete_confirma)
    app.add_url_rule("/usuarios/edit/<id>", "user_edit", user.edit)
    app.add_url_rule("/usuarios/roles/<id>", "user_roles", user.roles)
    app.add_url_rule("/usuarios/guardar_roles", "user_guardar_roles", user.guardar_roles, methods=["POST"])
    app.add_url_rule("/usuarios/modify", "user_modify", user.modify, methods=["POST"])
    app.add_url_rule("/usuarios/by_email/<email>/<password>", "user_by_email", user.find_by_email_and_pass)
    app.add_url_rule("/usuarios/perfil", "user_perfil", user.perfil)

    # Rutas de Configuración
    app.add_url_rule("/config", "config_edit", confsist.edit, methods=["GET", "POST"])

    ############
    #convencion para las rutas
    # la ruta que llama a un form de creacion incluye la palabra new
    # la ruta que llama al metodo que guarda un nuevo dato a partir del form de creacion incluye la palabra create
    # la ruta que llama a un form de edicion incluye la palabra edit
    # la ruta que llama al metodo que guarda un dato modificado a partir del form de edicion incluye la palabra modify
    ############

    # ruta historia clinica de pacientes
    app.add_url_rule("/historiaClinica", "historia_index", historiaClinica.browse)
    app.add_url_rule("/historiaClinica/browse", "historia_browse", historiaClinica.browse, methods=["POST"])
    app.add_url_rule("/historiaClinica/browse/<pagina>", "historia_pagina", historiaClinica.browse_pagina)
    
    app.add_url_rule("/historiaClinica/edit/<id>", "historia_edit", historiaClinica.edit)
    app.add_url_rule("/historiaClinica/<id>", "historia_edit_estado", historiaClinica.edit_estado)
    app.add_url_rule("/historiaClinica/modify", "historia_modify", historiaClinica.modify, methods=["POST"])
    app.add_url_rule("/historiaClinica/new", "historia_new", historiaClinica.new)
    app.add_url_rule("/historiaClinica/create", "historia_create", historiaClinica.create, methods=["POST"])

    # Ruta de historial de eventos
    app.add_url_rule("/historialEventos/newVeda/<id_historia>", "veda_new", historialDeEventos.veda_new)
    app.add_url_rule("/historialEventos/createVeda", "veda_create", historialDeEventos.veda_create, methods=["POST"])
    app.add_url_rule("/historialEventos/editVeda/<id>", "veda_edit", historialDeEventos.veda_edit)
    app.add_url_rule("/historialEventos/modifyVeda", "veda_modify", historialDeEventos.veda_modify, methods=["POST"])
    app.add_url_rule("/historialEventos/delete_Veda", "veda_delete", historialDeEventos.delete_veda, methods=["POST"])
    app.add_url_rule("/historialEventos/conf_borrarVeda/<id>", "veda_delete_confirma", historialDeEventos.delete_veda_confirma)

    
    app.add_url_rule("/historialEventos/newVcc/<id_historia>", "vcc_new", historialDeEventos.vcc_new)
    app.add_url_rule("/historialEventos/createVcc", "vcc_create", historialDeEventos.vcc_create, methods=["POST"])
    app.add_url_rule("/historialEventos/editVcc/<id>", "vcc_edit", historialDeEventos.vcc_edit)
    app.add_url_rule("/historialEventos/modifyVcc", "vcc_modify", historialDeEventos.vcc_modify, methods=["POST"])
    app.add_url_rule("/historialEventos/delete_Vcc", "vcc_delete", historialDeEventos.delete_vcc, methods=["POST"])
    app.add_url_rule("/historialEventos/conf_borrarVcc/<id>", "vcc_delete_confirma", historialDeEventos.delete_vcc_confirma)

    app.add_url_rule("/historialEventos/newCpre/<id_historia>", "cpre_new", historialDeEventos.cpre_new)
    app.add_url_rule("/historialEventos/createCpre", "cpre_create", historialDeEventos.cpre_create, methods=["POST"])
    app.add_url_rule("/historialEventos/editCpre/<id>", "cpre_edit", historialDeEventos.cpre_edit)
    app.add_url_rule("/historialEventos/modifyCpre", "cpre_modify", historialDeEventos.cpre_modify, methods=["POST"])
    app.add_url_rule("/historialEventos/delete_Cpre", "cpre_delete", historialDeEventos.delete_cpre, methods=["POST"])
    app.add_url_rule("/historialEventos/conf_borrarCpre/<id>", "cpre_delete_confirma", historialDeEventos.delete_cpre_confirma)

    
    # rutas de evento hepa
    app.add_url_rule("/historialEventos/newHepa/<id_historia>", "hepa_new", historialDeEventos.hepa_new)
    app.add_url_rule("/historialEventos/createHepa", "hepa_create", historialDeEventos.hepa_create, methods=["POST"])
    app.add_url_rule("/historialEventos/editHepa/<id>", "hepa_edit", historialDeEventos.hepa_edit)
    app.add_url_rule("/historialEventos/modifyHepa", "hepa_modify", historialDeEventos.hepa_modify, methods=["POST"])
    app.add_url_rule("/historialEventos/delete_hepa", "hepa_delete", historialDeEventos.delete_hepa, methods=["POST"])
    app.add_url_rule("/historialEventos/conf_borrarHepa/<id>", "hepa_delete_confirma", historialDeEventos.delete_hepa_confirma)

    # rutas de reportes
    app.add_url_rule("/reporte/estadVCC_form", "repo_estadVCC_form", reporte.estadVCC_form)
    app.add_url_rule("/reporte/estadVCC", "repo_estadVCC", reporte.estadVCC, methods=["POST"])
    app.add_url_rule("/reporte/estadVEDA_form", "repo_estadVEDA_form", reporte.estadVEDA_form)
    app.add_url_rule("/reporte/estadVEDA", "repo_estadVEDA", reporte.estadVEDA, methods=["POST"])
    app.add_url_rule("/reporte/vccCompleto_form", "repo_vccCompleto_form", reporte.vccCompleto_form)
    app.add_url_rule("/reporte/vccCompleto", "repo_vccCompleto", reporte.vccCompleto, methods=["POST"])
    app.add_url_rule("/reporte/vedaCompleto_form", "repo_vedaCompleto_form", reporte.vedaCompleto_form)
    app.add_url_rule("/reporte/vedaCompleto", "repo_vedaCompleto", reporte.vedaCompleto, methods=["POST"])
    app.add_url_rule("/reporte/vccBoston_form", "repo_vccBoston_form", reporte.vccBoston_form)
    app.add_url_rule("/reporte/vccBoston", "repo_vccBoston", reporte.vccBoston, methods=["POST"])
    app.add_url_rule("/reporte/vccPoliposPac_form", "vccPoliposPac_form", reporte.vccPoliposPac_form)
    app.add_url_rule("/reporte/vccPoliposPac", "vccPoliposPac", reporte.vccPoliposPac, methods=["POST"])

    #rutas reporte hepa
    app.add_url_rule("/reporte/estadHEPA_form", "repo_estadHEPA_form", reporte.estadHEPA_form)
    app.add_url_rule("/reporte/estadHEPA", "repo_estadHEPA", reporte.estadHEPA, methods=["POST"])
    app.add_url_rule("/reporte/hepaCompleto_form", "repo_hepaCompleto_form", reporte.hepaCompleto_form)
    app.add_url_rule("/reporte/hepaCompleto", "repo_hepaCompleto", reporte.hepaCompleto, methods=["POST"])

    app.add_url_rule("/reporte/estadCPRE_form", "repo_estadCPRE_form", reporte.estadCPRE_form)
    app.add_url_rule("/reporte/estadCPRE", "repo_estadCPRE", reporte.estadCPRE, methods=["POST"])
    app.add_url_rule("/reporte/cpreCompleto_form", "repo_cpreCompleto_form", reporte.cpreCompleto_form)
    app.add_url_rule("/reporte/cpreCompleto", "repo_cpreCompleto", reporte.cpreCompleto, methods=["POST"])
    app.add_url_rule("/reporte/historiaPeriodo_form/<id>", "repo_historiaPeriodo_form", reporte.historiaPeriodo_form)
    app.add_url_rule("/reporte/historiaPeriodo", "repo_historiaPeriodo", reporte.historiaPeriodo, methods=["POST"])


    
    

    app.add_url_rule("/reporte/polipos", "tamPolipos_index", reporte.polipos)
    app.add_url_rule("/reporte/vcc", "vcc_index", reporte.vccCompleto)
    



    # Ruta para el Home (usando decorator)
    @app.route("/")
    def home():
        return render_template("home.html")

    # Handlers
    app.register_error_handler(404, handler.not_found_error)
    app.register_error_handler(401, handler.unauthorized_error)
    # Implementar lo mismo para el error 500 y 401

    # Retornar la instancia de app configurada
    return app
