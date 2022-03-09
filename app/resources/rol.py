from flask import redirect, render_template, request, url_for, session, abort, flash, current_app
from app.db import connection
from  app.models.user import Rol

from app.helpers.auth import authenticated
from sqlalchemy.orm import relationship

def permisos(id):
    if not authenticated(session):
        abort(401)

    rol = Rol.find_by_id(id)

    return render_template("rol/permisos.html", permisos=rol.permisos, rol=rol)

def tiene_permiso(id, nombre_permiso):
    if not authenticated(session):
        abort(401)

    rol = Rol.find_by_id(id)
    if (rol.has_perm(nombre_permiso)):
        flash('tiene el permiso')
    else:
        flash('no tiene el permiso')

    return render_template("rol/permisos.html", permisos=rol.permisos, rol=rol)    

