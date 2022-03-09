from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref

dba = SQLAlchemy()

"""
    Tabla para la relacion muchos a muchos entre roles y  usuarios
"""
usuario_tiene_rol = dba.Table('usuario_tiene_rol',
                        dba.Column('usuario.id', dba.Integer, dba.ForeignKey('usuario.id'), primary_key=True),
                        dba.Column('rol.id', dba.Integer, dba.ForeignKey('rol.id'), primary_key=True)
                        )

class Rol(dba.Model):
    """ 
    Clase que modela los roles
    """

    __tablename__ = "rol"
    id = dba.Column(dba.Integer, primary_key=True)
    nombre = dba.Column(dba.String(30), unique=True, nullable=False)
    #users = relationship("User", secondary="usuario_tiene_rol")
    permisos = relationship("Permiso", secondary="rol_tiene_permiso")

    def __repr__(self):
        return self.id + " " + self.nombre

    @classmethod
    def all(cls):
        return Rol.query.all()

    @classmethod
    def find_by_id(cls, id):
        return Rol.query.filter_by(id=id).one_or_none()

    def has_perm(this, nombrePerm):
        perms = list(filter(lambda x: x.nombre == nombrePerm, this.permisos)) 
        return (len(perms) > 0)

"""
class UsuarioRol(dba.Model):
    __tablename__ = "usuario_tiene_rol"

    usuario_id = dba.Column(dba.Integer, dba.ForeignKey('usuario.id'), primary_key=True)
    rol_id = dba.Column(dba.Integer, dba.ForeignKey('rol.id'), primary_key=True)

    #usuario = relationship("User", backref=backref("usuario_tiene_rol", cascade="all, delete-orphan"))
    rol = relationship("Rol", backref=backref("usuario_tiene_rol", cascade="all, delete-orphan"))
"""

class Permiso(dba.Model):
    """
        Clase que modela los permisos
    """
    __tablename__ = "permiso"
    
    id = dba.Column(dba.Integer, primary_key=True)
    nombre = dba.Column(dba.String(255), unique=True, nullable=False)

class RolPermiso(dba.Model):
    """
        Clase que modela la relacion entre roles y permisos
    """

    __tablename__ = "rol_tiene_permiso"

    rol_id = dba.Column(dba.Integer, dba.ForeignKey('rol.id'), primary_key=True)
    permiso_id = dba.Column(dba.Integer, dba.ForeignKey('permiso.id'), primary_key=True)

    
    rol = relationship("Rol", backref=backref("rol_tiene_permiso", cascade="all, delete-orphan"))
    permiso = relationship("Permiso", backref=backref("rol_tiene_permiso", cascade="all, delete-orphan"))

