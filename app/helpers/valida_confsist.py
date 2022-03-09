from app.helpers.validadores import analiza_atributos_requeridos

def valida_edit_config(form_validar):
    """Se definen los atributos a validar en el form"""
    atributos_validar = [("titPagPpal", "txt", "255", "Título página principal")
        , ("desSitio", "txt", "2000", "Descripción del sitio")
        , ("mailContacto", "txt", "100", "Mail de contacto")
        , ("elemPagina", "num", "1¬3000", "Cantidad de elementos por página")]

    # Si no existe el atributo "sitioOn" en el form de entrada, se hace
    # requerida la carga de un mensaje para el sitio deshabilitado
    if (not form_validar.get('sitioOn')):
        atributos_validar.append(("msjSitioOff", "txt", "255", "Mensaje para sitio deshabilitado"))

    validacion_ok, errores = analiza_atributos_requeridos(atributos_validar, form_validar)
    return validacion_ok, errores
