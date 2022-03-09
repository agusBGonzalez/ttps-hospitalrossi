from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship
#from  app.models.rol import Rol, usuario_tiene_rol
from sqlalchemy.orm import relationship, backref

dba = SQLAlchemy()

#class User(object):
class User(dba.Model):
    """
        Clase que modela los usuarios
    """

    __tablename__ = "usuario"
    id = dba.Column(dba.Integer, primary_key=True)
    username = dba.Column(dba.String(100), unique=True, nullable=False)
    email = dba.Column(dba.String(100), unique=True, nullable=False)
    password = dba.Column(dba.String(100), unique=False, nullable=False)
    first_name = dba.Column(dba.String(100), unique=False, nullable=False)
    last_name = dba.Column(dba.String(100), unique=False, nullable=False)
    activo = dba.Column(dba.Boolean, default=True, unique=False, nullable=False)
    updated_at = dba.Column(dba.DateTime, onupdate=datetime.datetime.now)
    created_at = dba.Column(dba.DateTime, default=datetime.datetime.now)
    roles = relationship("Rol", secondary="usuario_tiene_rol")
    #roles = relationship("Rol", secondary="UsuarioRol")

    def __repr__(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def all(cls):
        """
        Devuelve todos los usuarios
        """
        return User.query.all()

    @classmethod
    def browse(cls, busqueda, activos, page, per_page):
        """
        Devuelve todos los usuarios filtrando por nombre y estado, para la pagina page, con per_page filas por pagina
        Parametro busqueda: indica parte inicial del nombre
        Parametro activos: "T" -> todos, "A" -> activos, "I" -> inactivos
        """

        busqueda = busqueda + '%'
        
        if (activos=="T"):
            return User.query.filter(User.username.like(busqueda)).paginate(page, per_page, True)
        elif (activos=="A"):
            return User.query.filter(User.username.like(busqueda)).filter_by(activo=True).paginate(page, per_page, True)
        else:
            return User.query.filter(User.username.like(busqueda)).filter_by(activo=False).paginate(page, per_page, True)

    @classmethod
    def create(cls, data):
        """
            Crea un nuevo usuario a partir de los datos indicados en el parametro data
        """
        nuevo = User(   username=data["username"],
                        email=data["email"], 
                        password=data["password"],
                        first_name=data["first_name"],
                        last_name=data["last_name"]
                    )

        try:
            dba.session.add(nuevo)
            dba.session.commit()
            return nuevo
        except:
            return False

    @classmethod
    def delete(cls, user):
        """
            Elimina el usuario indicado en el parametro user
        """        
        
        try:
            dba.session.delete(user)
            dba.session.commit()
            return True
        except:
            return False

    @classmethod
    def modify(cls, user, data):
        """
            Modifica el usuario user a partir de los datos indicados en el parametro data
        """

        user.email=data["email"]
        user.password=data["password"]
        user.first_name=data["first_name"]
        user.last_name=data["last_name"]
        # Si userAction es "perfil", se saltea username dado que ese 
        # atributo no está en el form ya que modificarlo es una 
        # operación no permitida desde la edición del perfil de usuario
        if (data['userAction'] != "perfil"):
            user.username = data["username"]

        try:
            dba.session.commit()
            return user
        except:
            return False

    @classmethod
    def find_by_email_and_pass(cls, email, password):
        """
            devuelve el primer usuario que coincida con los parametros indicados para email y password
        """
        return User.query.filter_by(email=email,password=password).one_or_none()
    
    @classmethod
    def find_by_username_and_pass(cls, username, password):
        """
            devuelve el primer usuario que coincida con los parametros indicados para username y password
        """
        
        return User.query.filter_by(username=username,password=password).one_or_none()
    
    @classmethod
    def find_by_username(cls, username):
        """
            devuelve el primer usuario que coincida con el parametro indicados para username
        """
        
        #return User.query.filter_by(email=email,password=password).all()
        return User.query.filter_by(username=username).one_or_none()

    @classmethod
    def find_by_email(cls, email):
        """
            devuelve el primer usuario que coincida con el parametro indicados para email
        """
        
        return User.query.filter_by(email=email).one_or_none()

    @classmethod
    def find_by_id(cls, id):
        """
            devuelve el primer usuario que coincida con el parametro indicados para id
        """
        
        return User.query.filter_by(id=id).one_or_none()

    @classmethod
    def add_role(cls, user, rol):
        """
            Agrega al usuario user el rol rol
        """
        user.roles.append(rol)
        try:
            dba.session.add(user)
            dba.session.commit()
            return user
        except:
            return False        


    def has_perm(this, nombrePerm):
        """
            Busca el permiso nombrePerm dentro de los roles que tenga asignados el usuario
        """
        roles_con_perm = list(filter(lambda x: x.has_perm(nombrePerm), this.roles))
        return (len(roles_con_perm) > 0)

    def has_role(this, id_rol):
        """
            Busca si el usuario tiene un rol con el id indicado por id_rol
        """
        roles_busca = list(filter(lambda x: x.id == id_rol, this.roles))
        return (len(roles_busca) > 0)

    def is_admin(this):
        """
        Indica si un usuario tiene rol Administrador. El id del rol se lee desde
        la tabla de parámetros generales del sistema
        """
        param_id_rol_admin = ParametroSistema.find_by_id('ID_ROL_ADMIN')
        if (param_id_rol_admin is not None):
            return this.has_role(param_id_rol_admin.valorInt)
        else:
            return False


class Rol(dba.Model):
    """
        Clase que modela los roles
    """
    __tablename__ = "rol"
    id = dba.Column(dba.Integer, primary_key=True)
    nombre = dba.Column(dba.String(30), unique=True, nullable=False)
    users = relationship("User", secondary="usuario_tiene_rol")
    permisos = relationship("Permiso", secondary="rol_tiene_permiso")

    def __repr__(self):
        return self.id + " " + self.nombre

    @classmethod
    def all(cls):
        """ Devuelve todos los roles
        """
        return Rol.query.all()

    @classmethod
    def find_by_id(cls, id):
        """
            Busca un rol por id
        """
        return Rol.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_name(cls, nombre):
        """Busca un rol por nombre"""
        return Rol.query.filter_by(nombre=nombre).one_or_none()

    def has_perm(this, nombrePerm):
        """
            Verifica si el rol tiene asociado el permiso de nombre nombrePerm
        """
        perms = list(filter(lambda x: x.nombre == nombrePerm, this.permisos)) 
        return (len(perms) > 0)


class UsuarioRol(dba.Model):
    """
        Clase que modela la relacion muchos a muchos entre usuarios y roles
    """
    __tablename__ = "usuario_tiene_rol"

    usuario_id = dba.Column(dba.Integer, dba.ForeignKey('usuario.id'), primary_key=True)
    rol_id = dba.Column(dba.Integer, dba.ForeignKey('rol.id'), primary_key=True)

    usuario = relationship("User", backref=backref("usuario_tiene_rol", cascade="all, delete-orphan"))
    rol = relationship("Rol", backref=backref("usuario_tiene_rol", cascade="all, delete-orphan"))


class Permiso(dba.Model):
    """
        Clase que modela los permisos
    """
    __tablename__ = "permiso"
    
    id = dba.Column(dba.Integer, primary_key=True)
    nombre = dba.Column(dba.String(255), unique=True, nullable=False)


class RolPermiso(dba.Model):
    """
        Clase que modela la relacion muchos a muchos entre roles y permisos
    """

    __tablename__ = "rol_tiene_permiso"

    rol_id = dba.Column(dba.Integer, dba.ForeignKey('rol.id'), primary_key=True)
    permiso_id = dba.Column(dba.Integer, dba.ForeignKey('permiso.id'), primary_key=True)

    
    rol = relationship("Rol", backref=backref("rol_tiene_permiso", cascade="all, delete-orphan"))
    permiso = relationship("Permiso", backref=backref("rol_tiene_permiso", cascade="all, delete-orphan"))


class ParametroSistema(dba.Model):
    """Clase que modela los permisos"""
    __tablename__ = "parametro"
    nombre = dba.Column(dba.String(30), primary_key=True)
    valorStr = dba.Column(dba.String(255), unique=False, nullable=True)
    valorInt = dba.Column(dba.Integer, unique=False, nullable=True)

    @classmethod
    def find_by_id(cls, id):
        """Busca un parámetro del sistema por id"""
        return ParametroSistema.query.filter_by(nombre=id).one_or_none()
