from flask import redirect, render_template, request, url_for, session, abort, flash, current_app
from app.db import connection
from app.models.user import User
#from  app.models.rol import Rol
#from  app.models.rol import UsuarioRol
from  app.models.user import Rol
#from  app.models.user import UsuarioRol
from app.models.confsist import ConfSist
from app.helpers.auth import authenticated, sess_has_perm
from sqlalchemy.orm import relationship

# Protected resources
def index():
    """
        Lista todos los usuarios con filtros por defecto, paginando 
        (a diferencia de list que los lista sin pagina para imprimir por ejemplo) 
    """

    if ( (not authenticated(session)) or (not sess_has_perm('user_index')) ):
       abort(401)

    session['busqueda_usuario'] = ""    #por defecto muestro todos
    session['activos'] = "T"            #
    
    conf = ConfSist.getConfig()
    por_pagina = conf.cantidad_registros_x_pagina
    pagina = 1

    pages = User.browse('', "T", pagina, por_pagina)
    users = pages.items

    if (pages.has_next):
        proxima = pages.next_num
    else:
        proxima = 0
    
    if (pages.has_prev):
        previa = pages.prev_num
    else:
        previa = 0

    return render_template("user/index.html", users=users, proxima=proxima, previa=previa, busqueda="", activos="T")


def browse():
    """Lista usuarios de acuerdp a filtros por nombre y estado, paginando 
    """

    if ( (not authenticated(session)) or (not sess_has_perm('user_index')) ):
       abort(401)

    data = request.form
    busqueda = data['busca_username']
    activos = data['activos']

    session['busqueda_usuario'] = busqueda
    session['activos'] = activos
    
    conf = ConfSist.getConfig()
    por_pagina = conf.cantidad_registros_x_pagina
    pagina = 1

    pages = User.browse(busqueda, activos, pagina, por_pagina)
    users = pages.items

    if (pages.has_next):
        proxima = pages.next_num
    else:
        proxima = 0
    
    if (pages.has_prev):
        previa = pages.prev_num
    else:
        previa = 0

    return render_template("user/index.html", users=users, proxima=proxima, previa=previa, busqueda=busqueda,  activos=activos)

def browse_pagina(pagina):
    """Lista usuarios de acuerdp a filtros por nombre y estado, paginando 
        Funcion complementaria a browse que permite recorrer las diferentes paginas.
        Un llamado inicial a browse configura los parametros de busqueda que 
        luego seran utilizados al recorrer las paginas.
    """

    if ( (not authenticated(session)) or (not sess_has_perm('user_index')) ):
       abort(401)

    pagina = int(pagina)
    busqueda = session['busqueda_usuario']
    activos = session['activos']

    conf = ConfSist.getConfig()
    por_pagina = conf.cantidad_registros_x_pagina

    pages = User.browse(busqueda, activos, pagina, por_pagina)
    users = pages.items
    if (pages.has_next):
        proxima = pages.next_num
    else:
        proxima = 0
    
    if (pages.has_prev):
        previa = pages.prev_num
    else:
        previa = 0

    return render_template("user/index.html", users=users, proxima=proxima, previa=previa, busqueda=busqueda, activos=activos)

def new():
    """Prepara la vista de nuevo usuario. 
        Puede ser que se llegue a este punto luego de un error de datos en un intento anterior. 
        En ese caso cargo los datos del form que el usuario ya habia llegado a cargar para que los corrija
    """
    if ( (not authenticated(session)) or (not sess_has_perm('user_new')) ):
      abort(401)

    if (session.get('new_user_in_progress')):
        return render_template("user/new.html",default_values=session['new_user_in_progress'])
    else:    
        return render_template("user/new.html")

def create():
    """
        Valida los datos cargados para el alta de un usuario.
        Si hay errores se informan y se vuelve a la pantalla de carga
        guardando en la sesion los datos ya cargados para que el usuario
        no necesite volver a cargarlos.
        Si no hay errores pasa los datos a la clase User para su creacion
    """

    if ( (not authenticated(session)) or (not sess_has_perm('user_new')) ):
       abort(401)

    # para evitar tener que cargar todos los campos de nuevo en caso de un error,
    # guardo los campos cargados en una variable de sesion. 
    # Al ir de nuevo a new user, si el variable existe, la utilizo para los valores por defecto
    data = request.form
    session['new_user_in_progress'] = request.form

    errores = []

    if ( 
            (len(data["username"]) > 100 ) or (len(data["email"]) > 100 ) or
            (len(data["password"]) > 100)  or
            (len(data["first_name"]) > 100) or (len(data["last_name"]) > 100)
        ):
        errores.append('Datos exceden longitud máxima')

    if ( 
            (data["username"] == "") or (data["email"]=="") or
            (data["password"] == "") or
            (data["first_name"] == "") or (data["last_name"]=="")
        ):
        errores.append('Faltan campos obligatorios')

    u = User.find_by_username(data["username"])
    if u is not None :
        errores.append('Nombre de usuario ya existe')

    u = User.find_by_email(data["email"])
    if u is not None :
        errores.append('Direccion de email ya existe')

    if (len(errores) == 0):
        user = User.create(data)
        if (not user):
            errores.append('Error al crear el usuario')

    if (len(errores) == 0):
        # si no hubo prolemas quito de la sesion los datos temporales
        session.pop('new_user_in_progress')
        return redirect(url_for("user_index"))
    else:
        for msg in errores:
            flash(msg)
        return redirect(url_for("user_new"))    
        

def find_by_email_and_pass(email, password):
    """
        listo usuarios por mail y password
        Funcion de prueba
    """
    if ( (not authenticated(session)) or (not sess_has_perm('user_index')) ):
       abort(401)

    users = User.find_by_email_and_pass(email, password)

    return render_template("user/index.html", users=users)

def listar():
    """
        Lista todos los usuarios sin filtros ni paginacion
    """
    if ( (not authenticated(session)) or (not sess_has_perm('user_index')) ):
       abort(401)

    users = User.all()

    return render_template("user/list.html", users=users)

def delete_confirma(id):
    """
        Muestra la vista de confirmacion para la eliminacion de un usuario
    """
    if ( (not authenticated(session)) or (not sess_has_perm('user_delete')) ):
       abort(401)

    user = User.find_by_id(id)
    return render_template("user/edit.html", user=user, user_action="delete")

def delete():
    """
        busca el usuario indicado en un POST e invoca a la clase user para elimninarlo
    """    
    if ( (not authenticated(session)) or (not sess_has_perm('user_delete')) ):
       abort(401)
    
    errores = []

    data = request.form
    user = User.find_by_id(data['id'])

    cur_id = session["user_id"]
    if (user.id == cur_id):
        errores.append("No se puede eliminar el usuario actual")
    else:

        if (user is None):
            errores.append("El usuario no existe")            
        else:
            status = User.delete(user)
            if (not status):
                errores.append("Se produjo un error al eliminar el usuario")

    for msg in errores:
        flash(msg)

    return redirect(url_for("user_index"))

def edit(id):
    """
        Muestra los datos de un usuario y permite editarlos.
        Al llamar a la vista que muestra los le indica que esta en modo edicion
        ya que la misma se puede utilizar para solo visualizar 
    """
    if ( (not authenticated(session)) or (not sess_has_perm('user_update')) ):
       abort(401)

    user = User.find_by_id(id)
    return render_template("user/edit.html", user=user, user_action="edit")

def modify():
    """
        Valida los datos cargados para el edit de un usuario.
        Si hay errores se informan y se vuelve a la pantalla de edicion
        Si no hay errores pasa los datos a la clase User para su modificacion
    """    
    if ( (not authenticated(session)) or (not sess_has_perm('user_update')) ):
       abort(401)

    data = request.form
    user = User.find_by_id(data['id'])
    errores = []

    # Si userAction es "perfil" se saltea el análisis de la activación/
    # desactivación del usuario y el análisis del username dado que son
    # operaciones no permitidas desde la edición del perfil de usuario
    if (data['userAction'] != "perfil"):
        activo = ('activo' in request.form)
        # si intento desactivar, y el usuario estaba activo, y el usuario era administrador (id 1)
        if ( (not activo) and (user.activo) and (user.has_role(1)) ):
            errores.append('No se puede desactivar un usuario administrador')
        else:
            user.activo = activo

        if (user.username != data['username']):
            #si se cambio el username debo validar que no se repita
            u = User.find_by_username(data["username"])
            if u is not None :
                errores.append('Nombre de usuario ya existe')

    if (user.email != data['email']):
        #si se cambio el mail debo validar que no se repita
        u = User.find_by_email(data["email"])
        if u is not None :
            errores.append('La direccion de email ya existe')

    if (len(errores)==0):
        result = User.modify(user, request.form)
        if (not result):
            errores.append('Error al modificar el usuario')

    if (len(errores)==0):
        # Si userAction es edit, se vuelve al listado de administración
        # de usuarios. Si no, se editó un perfil, se vuelve al home
        if (data['userAction'] == "edit"):
            return redirect(url_for("user_index"))
        else:
            return redirect(url_for("home"))
    else:
        for msg in errores:
            flash(msg)
        return redirect(url_for("user_edit", id=request.form['id']))

def roles(id):
    """
        listo los roles de un usuario indicado por el parametro id
    """
    if ( (not authenticated(session)) or (not sess_has_perm('user_update')) ):
       abort(401)

    user = User.find_by_id(id)
    roles = Rol.query.all()
    return render_template("user/roles_usuario.html", roles=roles, roles_usuario=user.roles, user=user)

def guardar_roles():
    """
        guardo los roles seleccionados de un usuario indicado en los datos del POST
    """

    if ( (not authenticated(session)) or (not sess_has_perm('user_update')) ):
       abort(401)

    errores = []

    data = request.form
    user = User.find_by_id(data['id'])
    ids_roles = request.form.getlist('id_rol')

    user.roles.clear()
    for id_rol in ids_roles:
        #flash(id_rol)
        rol = Rol.find_by_id(id_rol)
        if rol not in user.roles:
            User.add_role(user, rol)

    if (len(errores)==0):
        return redirect(url_for("user_index"))
    else:
        for msg in errores:
            flash(msg)
        return redirect(url_for("user_roles", id=request.form['id'])) 

def perfil():
    """Se muestran los datos del usuario actual"""

    if (not authenticated(session)):
       abort(401)

    user = User.find_by_username(session['user'])
    return render_template("user/edit.html", user=user, user_action="perfil")
