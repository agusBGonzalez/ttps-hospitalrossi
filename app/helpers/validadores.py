from datetime import datetime, date, timedelta

def analiza_atributos_requeridos(atributos_requeridos, form_validar):
    """
    Analiza que los atributos recibido por parámetro estén en el form que
    se quiere validar y que no sean vacíos. Además, analiza: 
        - si el atributo es de tipo texto y requiere validación de longitud
        - si el atributo es de tipo entero y requiere validación de rango
        - si el atributo es de tipo fecha y está en formato YYYY-MM-DD
        - si el atributo es de tipo tiempo y está en formato HH:MM
    Devuelve una tupla indicando si se detectó algún error o no y una lista
    de los errores encontrados.
    """
    errores = []
    for atributo in atributos_requeridos:
        # En la 5ta posición de la tupla se indica si el atributo es requerido
        # Para no afectar tanto el código ya generado, se asume que si esa
        # posición no existe en la tupla, entonces el atributo es requerido.
        if (len(atributo) > 4):
            atr_req = atributo[4]
        else:
            atr_req = True
        if (atributo[0] not in form_validar) and atr_req:
            errores.append(f"El atributo '{atributo[3]}' es requerido.")
        if not form_validar.get(atributo[0]):
            if atr_req:
                errores.append(f"El atributo '{atributo[3]}' no puede estar vacío.")
        else:
            if (atributo[1] == "txt") and (atributo[2] != ""):
                # Si el atributo a validar es de tipo string (txt) y se especifica en atributo[2] una longitud,
                # se valida que el atributo no supere dicha longitud.
                if (int(atributo[2]) < len(form_validar.get(atributo[0]))):
                    errores.append(f"El atributo '{atributo[3]}' no debe superar los '{atributo[2]}' caracteres.")
            elif (atributo[1] == "num"):
                # Si el atributo a validar es de tipo integer (num), se verifica que se pueda convertir a numérico.
                # Además, si se especifica en atributo[2] de la forma "valor mínimo¬valor máximo", se puede validar
                # si ese atributo es >= "valor mínimo", si es <= "valor máximo" o si está entre ambos.
                if (form_validar.get(atributo[0]).isnumeric()):
                    if (atributo[2] != ""):
                        rango = atributo[2].split("¬")
                        if (rango[0] != "") and (rango[1] == ""):
                            if int(rango[0]) > int(form_validar.get(atributo[0])):
                                errores.append(f"El valor del atributo '{atributo[3]}' debe ser mayor o igual a '{rango[0]}'.")
                        elif (rango[0] == "") and (rango[1] != ""):
                            if int(rango[1]) < int(form_validar.get(atributo[0])):
                                errores.append(f"El valor del atributo '{atributo[3]}' debe ser menor o igual a '{rango[1]}'.")
                        else:
                            if not (int(rango[0]) <= int(form_validar.get(atributo[0])) and int(form_validar.get(atributo[0])) <= int(rango[1])):
                                errores.append(f"El valor del atributo '{atributo[3]}' debe estar entre '{rango[0]}' y '{rango[1]}'.")
                else:
                    errores.append(f"El atributo '{atributo[3]}' debe ser numérico.")
            elif (atributo[1] == "dt"):
                # Si el atributo a validar es de tipo date (dt), se valida contra el formato YYYY-MM-DD. Por lo tanto
                # se verifica que tenga 10 caracteres y que se pueda convertir a tipo date.
                if (len(form_validar.get(atributo[0])) == 10):
                    try:
                        fecha_tipo_date = datetime.strptime(form_validar.get(atributo[0]), '%Y-%m-%d').date()
                    except:
                        errores.append(f"El atributo '{atributo[3]}' no está en el formato requerido: YYYY-MM-DD.")
                else:
                    errores.append(f"El atributo '{atributo[3]}' no está en el formato requerido: YYYY-MM-DD.")
            elif (atributo[1] == "tm"):
                # Si el atributo a validar es de tipo time (tm), se valida contra el formato HH:MM (en 24). Por lo tanto
                # se verifica que tenga 5 caracteres y que se pueda convertir a tipo time.
                if (len(form_validar.get(atributo[0])) == 5):
                    try:
                        hora_tipo_time = datetime.strptime(form_validar.get(atributo[0]), '%H:%M').time()
                    except:
                        errores.append(f"El atributo '{atributo[3]}' no está en el formato requerido: HH:MM.")
                else:
                    errores.append(f"El atributo '{atributo[3]}' no está en el formato requerido: HH:MM.")
    result = len(errores) == 0
    return result, errores

def valida_hora(hora):
    ok = True
    try:
        hh = int(hora[0:2])
        mm = int(hora[3:5])
        ss = int(hora[6:8])
        if (hh>24) or (hh<0) or \
        (mm>60) or (mm<0) or \
        (ss>60) or (ss<0):
            ok = False
    except:
        ok = False

    return ok
