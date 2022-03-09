from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

dba = SQLAlchemy()

class ConfSist(dba.Model):
    """Clase que modela la configuración del sistema"""
    __tablename__ = "configuracion_sistema"
    # Se agrega clave primaria por exigencia de SQLAlchemy. Esta clase tendrá siempre 1 sola instancia
    id = dba.Column(dba.Integer, primary_key=True)
    titulo_pagina_principal = dba.Column(dba.String(255), unique=False, nullable=False)
    descripcion_sitio = dba.Column(dba.String(2000), unique=False, nullable=False)
    email_contacto = dba.Column(dba.String(100), unique=False, nullable=False)
    cantidad_registros_x_pagina = dba.Column(dba.Integer, unique=False, nullable=False)
    sitio_habilitado = dba.Column(dba.Boolean, default=True, unique=False, nullable=False)
    mensaje_sitio_deshabilitado = dba.Column(dba.String(255), unique=False, nullable=True)
    actualizado_en = dba.Column(dba.DateTime, onupdate=datetime.now, nullable=False)


    @classmethod
    def update(cls, updconfig, data):
        """
        Edita los parámetros de configuración de acuerdo a los datos incluídos
        en el parámetro data
        """
        updconfig.titulo_pagina_principal = data['titPagPpal']
        updconfig.descripcion_sitio = data['desSitio']
        updconfig.email_contacto = data['mailContacto']
        updconfig.cantidad_registros_x_pagina = data['elemPagina']
        # Si existe el input "sitioOn" en el form de entrada, se entiende que 
        # ha sido tildado. Por el except, se entiende que ha sido destildado
        try:
            updconfig.sitio_habilitado = (data['sitioOn'] == 'on')
        except:
            updconfig.sitio_habilitado = False
        # Se actualiza el mensaje de sitio deshabilitado solo si el sitio se 
        # deshabilitó
        # if (not updconfig.sitio_habilitado):
        updconfig.mensaje_sitio_deshabilitado = data['msjSitioOff']

        try:
            dba.session.commit()
            return updconfig
        except:
            dba.session.rollback()
            return False

    @classmethod
    def getConfig(cls):    
        return ConfSist.query.first()
