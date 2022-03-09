from flask import redirect, render_template, request, url_for, session, abort, flash
from app.models.confsist import ConfSist
from app.helpers.auth import authenticated, sess_has_perm
from app.helpers.valida_confsist import valida_edit_config

def edit():
    """Edita la configuración del sistema"""
    #if (not authenticated(session)) or (not sess_has_perm('config_update')):
    #    abort(401)

    confsistorig = ConfSist.getConfig()
    if request.method == 'POST':
        validacion_ok, errores = valida_edit_config(request.form)

        if validacion_ok:
            status = ConfSist.update(confsistorig, request.form)
            if (not status):
                flash('Error al modificar la configuración del sistema', category="error")
            else:
                return redirect(url_for("home"))
        else:
            for mensaje_error in errores:
                flash(mensaje_error, category="error")

    return render_template("confsist/edit.html", confsist=confsistorig)
