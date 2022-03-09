from flask import redirect, render_template, request, url_for, abort, session, flash
from app.models.user import User
from app.models.confsist import ConfSist


def login():
    return render_template("auth/login.html")

def authenticate():
    params = request.form

    user = User.find_by_username_and_pass(params["username"], params["password"])

    if not user:
        flash("Usuario o clave incorrecto.")
        return redirect(url_for("auth_login"))
    else:
        if user.activo:
            cfgsis = ConfSist.getConfig()
            # Si el sitio se encuentra deshabilitado, solo se permite iniciar sesión
            # a los usuarios con rol Administrador
            if (cfgsis.sitio_habilitado == True) or (cfgsis.sitio_habilitado == False and user.is_admin()):
                # a partir de implemntar el ORM, lo que obtengo es un objeto
                # no lo puedo leer como si fuera un array asociativo
                session["user"] = user.username
                session["user_id"] = user.id
                # flash("La sesión se inició correctamente.")
                return redirect(url_for("home"))
            else:
                # flash("El sitio se encuentra fuera de servicio momentánemente. Intente ingresar más tarde.")
                flash(cfgsis.mensaje_sitio_deshabilitado)
                return redirect(url_for("auth_login"))
        else:
            flash("Su usuario ha sido desactivado. Comuníquese con el administrador del sistema.")
            return redirect(url_for("auth_login"))


def logout():
    del session["user"]
    session.clear()
    
    flash("La sesión se cerró correctamente.")

    return redirect(url_for("auth_login"))
