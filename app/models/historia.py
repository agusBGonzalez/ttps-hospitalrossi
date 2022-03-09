from flask.templating import DispatchingJinjaLoader
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import text
from datetime import date
import sys

dba = SQLAlchemy()

class Historia(dba.Model):
    """ 
    Clase que modela las historias
    """

    __tablename__ = "historia"
    id = dba.Column(dba.Integer, primary_key=True, autoincrement=True)
    nombre = dba.Column(dba.String(300), unique=False, nullable=False)
    dni = dba.Column(dba.String(10), unique=True, nullable=False)
    nacimiento =  dba.Column(dba.Date)
    #id_sexo  = dba.Column(dba.Integer, primary_key=True)
    id_sexo = dba.Column(dba.Integer, dba.ForeignKey('sexo.id'), nullable=False)
    sexo = dba.relationship('Sexo')
    activa = dba.Column(dba.Boolean, default=True, unique=False, nullable=False)
    edad = 0

    # SELECT TIMESTAMPDIFF(YEAR,FechaNac,CURDATE()) AS edad  FROM clientes;

    def __repr__(self):
        return str(self.id) + " " + self.nombre

    #def edad(this):
    #    today = date.today()
    #    return today.year - this.nacimiento.year - ((today.month, today.day) < (this.nacimiento.month, this.nacimiento.day))

    def calcularEdad(self):
        today = date.today()
        self.edad = today.year - self.nacimiento.year - ((today.month, today.day) < (self.nacimiento.month, self.nacimiento.day))
    
    @classmethod
    def all(cls):
        historias = Historia.query.all()
        list(map(lambda x:x.calcularEdad(), historias))
        return historias

    @classmethod
    def find_by_id(cls, id):
        h =  Historia.query.filter_by(id=id).one_or_none()
        h.calcularEdad()
        return h

    @classmethod
    def create(cls, data):
        historia = Historia(
                    nombre=data["nombre"],
                    dni=data["dni"],
                    nacimiento=data["nacimiento"],
                    id_sexo=data["id_sexo"],
                    activa=True
                )

        try:
            dba.session.add(historia)
            dba.session.commit()
            
            return historia
        except:
            dba.session.rollback()
            return False
    
    @classmethod
    def cambiar_estado(cls,historia):
        historia.activa= not historia.activa
        dba.session.commit()            
        return historia

    @classmethod
    def modify(cls, historia, data):
        """
            Modifica el usuario user a partir de los datos indicados en el parametro data
        """

        historia.nombre=data["nombre"],
        historia.dni=data["dni"],
        historia.id_sexo=data["id_sexo"],
        historia.nacimiento=data["nacimiento"],
        #historia.nombre=data["nombre"],

        try:
            dba.session.commit()
            return historia
        except:
            dba.session.rollback()
            return False

    @classmethod
    def browse(cls, busqueda, activas, page, per_page):
        """
        Devuelve todos los usuarios filtrando por nombre y estado, para la pagina page, con per_page filas por pagina
        Parametro busqueda: indica parte inicial del nombre
        Parametro activos: "T" -> todos, "A" -> activos, "I" -> inactivos
        """
        dba.session.rollback()

        busqueda = busqueda + '%'
        
        if (activas=="T"):
            historias = Historia.query.filter(Historia.nombre.like(busqueda)).paginate(page, per_page, True)
        elif (activas=="A"):
            historias = Historia.query.filter(Historia.nombre.like(busqueda)).filter_by(activa=True).paginate(page, per_page, True)
        else:
            historias = Historia.query.filter(Historia.nombre.like(busqueda)).filter_by(activa=False).paginate(page, per_page, True)        
        
        list(map(lambda x:x.calcularEdad(), historias.items))

        return historias

    def getEncabezadosEventos(self):
        dba.session.rollback()
        
        result = dba.engine.execute(text("""SELECT id, fecha, 'VCC' AS tipo
                                FROM vcc where id_historia = :id
                                UNION all
                                SELECT id, fecha, 'VEDA' AS tipo
                                FROM veda where id_historia = :id
                                UNION all
                                SELECT id, fecha, 'CPRE' AS tipo
                                FROM cpre where id_historia = :id
                                UNION all
                                SELECT id, fecha, 'HEPA' AS tipo
                                FROM hepa where id_historia = :id
                                """), id=self.id)
        #for data in result:
        #    print(data["cant"], file=sys.stderr)
        #SELECT  0, date_format(NOW(),'%d/%m/%Y')
        return result


class Sexo(dba.Model):
    __tablename__ = "sexo"
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.nombre

    @classmethod
    def all(cls):
        """ Devuelve el listado de sexos
        """
        return Sexo.query.order_by(Sexo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
        """
            devuelve el primer sexo que coincida con el parametro indicado para id
        """
        
        return Sexo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
        """
            devuelve el primer tipo de centro que coincida con el parametro indicado para descripcion
        """
        
        return Sexo.query.filter_by(descripcion=nombre).one_or_none()
