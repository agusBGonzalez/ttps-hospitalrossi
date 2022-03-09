from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import text
from datetime import date
import sys

dba = SQLAlchemy()


class Veda(dba.Model):

    __tablename__ = "veda"
    id = dba.Column(dba.Integer, primary_key=True, autoincrement=True)
    comentarios = dba.Column(dba.String(4000), unique=True, nullable=False)
    fecha =  dba.Column(dba.Date)
    id_historia =  dba.Column(dba.Integer)
    motivos = relationship("Veda_Motivo", secondary="veda_veda_motivo")
    anestesia = dba.Column(dba.Boolean, nullable=False)
    id_VEDA_incompleto  =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_terapeutica =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_polipectomia_tam =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_polipectomia_material =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_polipectomia_paris =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_biopsia =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_protocolo =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_de_guardia =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_VEDA_tiempo =  dba.Column(dba.Integer, unique=False, nullable=True)
    id_operador = dba.Column(dba.Integer, unique=False, nullable=True)
    hallazgos = relationship("Veda_Hallazgo", secondary="veda_veda_hallazgo")   

    @classmethod
    def find_by_id(cls, id):
        veda =  Veda.query.filter_by(id=id).one_or_none()
        return veda

    @classmethod
    def create(cls, data):
    
        evento = Veda(
                    comentarios=data["comentarios"],
                    fecha=data["fecha"],
                    id_historia=data["id_historia"],
                    anestesia=(data["anestesia"]=="1"),
                    id_VEDA_incompleto=data["id_VEDA_incompleto"],
                    id_VEDA_polipectomia_tam=data["id_VEDA_polipectomia_tam"],
                    id_VEDA_polipectomia_material=data["id_VEDA_polipectomia_material"],
                    id_VEDA_tiempo=data["id_VEDA_tiempo"]
                )

        evento.zero_to_null()
        ids_motivos = data.getlist('motivos')
        for id_motivo in ids_motivos:
            motivo = Veda_Motivo.find_by_id(id_motivo)
            evento.motivos.append(motivo)

        ids_hallazgos = data.getlist('hallazgos')
        for id_hallazgo in ids_hallazgos:
            hallazgo = Veda_Hallazgo.find_by_id(id_hallazgo)
            evento.hallazgos.append(hallazgo)


        try:
            dba.session.add(evento)
            dba.session.commit()
            
            return evento
        except:
            dba.session.rollback()
            return False

    @classmethod
    def modify(cls, evento, data):
        
        evento.comentarios=data["comentarios"]
        evento.fecha=data["fecha"]
        evento.anestesia=(data["anestesia"]=="1")
        evento.id_VEDA_incompleto=data["id_VEDA_incompleto"]
        evento.id_VEDA_polipectomia_tam=data["id_VEDA_polipectomia_tam"]
        evento.id_VEDA_polipectomia_material=data["id_VEDA_polipectomia_material"]
        evento.id_VEDA_polipectomia_paris=data["id_VEDA_polipectomia_paris"]
        evento.id_VEDA_biopsia=data["id_VEDA_biopsia"]
        evento.id_VEDA_protocolo=data["id_VEDA_protocolo"]
        evento.id_VEDA_de_guardia=data["id_VEDA_de_guardia"]
        evento.id_VEDA_tiempo=data["id_VEDA_tiempo"]

        evento.zero_to_null()

        ids_motivos = data.getlist('motivos')
        evento.motivos.clear()
        for id_motivo in ids_motivos:
            motivo = Veda_Motivo.find_by_id(id_motivo)
            evento.motivos.append(motivo)

        ids_hallazgos = data.getlist('hallazgos')
        evento.hallazgos.clear()
        for id_hallazgo in ids_hallazgos:
            hallazgo = Veda_Hallazgo.find_by_id(id_hallazgo)
            evento.hallazgos.append(hallazgo)

        try:
            dba.session.commit()
            return evento
        except:
            dba.session.rollback()
            return False


    @classmethod
    def delete(cls, evento):
        """
            Elimina el evento indicado en el parametro
        """        
        
        try:
            dba.session.delete(evento)
            dba.session.commit()
            return True
        except:
            return False

    def zero_to_null(self):
        if self.id_VEDA_incompleto=="0":
            self.id_VEDA_incompleto = None 
        if self.id_VEDA_polipectomia_tam=="0":
            self.id_VEDA_polipectomia_tam = None
        if self.id_VEDA_polipectomia_material=="0":
            self.id_VEDA_polipectomia_material = None
        if self.id_VEDA_polipectomia_paris=="0":
            self.id_VEDA_polipectomia_paris = None
        if self.id_VEDA_biopsia=="0":
            self.id_VEDA_biopsia = None
        if self.id_VEDA_protocolo=="0":
            self.id_VEDA_protocolo = None
        if self.id_VEDA_de_guardia=="0":
            self.id_VEDA_de_guardia = None

class Veda_Biopsia(dba.Model):
    __tablename__ = "Veda_Biopsia" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Biopsia.query.order_by(Veda_Biopsia.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Biopsia que coincida con el parametro indicado para id
      """ 
      return Veda_Biopsia.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Biopsia que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Biopsia.query.filter_by(descripcion=nombre).one_or_none()


class Veda_de_Guardia(dba.Model):
    __tablename__ = "Veda_de_Guardia" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_de_Guardia.query.order_by(Veda_de_Guardia.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_de_Guardia que coincida con el parametro indicado para id
      """ 
      return Veda_de_Guardia.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_de_Guardia que coincida con el parametro indicado para descripcion
      """ 
      return Veda_de_Guardia.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Hallazgo(dba.Model):
    __tablename__ = "veda_hallazgo" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Hallazgo.query.order_by(Veda_Hallazgo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Hallazgo que coincida con el parametro indicado para id
      """ 
      return Veda_Hallazgo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Hallazgo que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Hallazgo.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Incompleto(dba.Model):
    __tablename__ = "Veda_Incompleto" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Incompleto.query.order_by(Veda_Incompleto.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Incompleto que coincida con el parametro indicado para id
      """ 
      return Veda_Incompleto.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Incompleto que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Incompleto.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Motivo(dba.Model):
    __tablename__ = "veda_motivo" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)
    vedas = relationship("Veda", secondary="veda_veda_motivo")

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Motivo.query.order_by(Veda_Motivo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Motivo que coincida con el parametro indicado para id
      """ 
      return Veda_Motivo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Motivo que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Motivo.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Polipectomia_Material(dba.Model):
    __tablename__ = "Veda_Polipectomia_Material" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Polipectomia_Material.query.order_by(Veda_Polipectomia_Material.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Polipectomia_Material que coincida con el parametro indicado para id
      """ 
      return Veda_Polipectomia_Material.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Polipectomia_Material que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Polipectomia_Material.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Polipectomia_Paris(dba.Model):
    __tablename__ = "Veda_Polipectomia_Paris" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Polipectomia_Paris.query.order_by(Veda_Polipectomia_Paris.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Polipectomia_Paris que coincida con el parametro indicado para id
      """ 
      return Veda_Polipectomia_Paris.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Polipectomia_Paris que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Polipectomia_Paris.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Polipectomia_Tam(dba.Model):
    __tablename__ = "Veda_Polipectomia_Tam" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Polipectomia_Tam.query.order_by(Veda_Polipectomia_Tam.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Polipectomia_Tam que coincida con el parametro indicado para id
      """ 
      return Veda_Polipectomia_Tam.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Polipectomia_Tam que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Polipectomia_Tam.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Protocolo(dba.Model):
    __tablename__ = "Veda_Protocolo" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Protocolo.query.order_by(Veda_Protocolo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Protocolo que coincida con el parametro indicado para id
      """ 
      return Veda_Protocolo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Protocolo que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Protocolo.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Terapeutica(dba.Model):
    __tablename__ = "Veda_Terapeutica" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Terapeutica.query.order_by(Veda_Terapeutica.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Terapeutica que coincida con el parametro indicado para id
      """ 
      return Veda_Terapeutica.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Terapeutica que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Terapeutica.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Tiempo(dba.Model):
    __tablename__ = "Veda_Tiempo" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Veda_Tiempo.query.order_by(Veda_Tiempo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Veda_Tiempo que coincida con el parametro indicado para id
      """ 
      return Veda_Tiempo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Veda_Tiempo que coincida con el parametro indicado para descripcion
      """ 
      return Veda_Tiempo.query.filter_by(descripcion=nombre).one_or_none()


class Veda_Veda_Motivo(dba.Model):
    """
        Clase que modela la relacion muchos a muchos entre VEDA y motivos de VEDA
    """

    __tablename__ = "veda_veda_motivo"

    id_VEDA = dba.Column(dba.Integer, dba.ForeignKey('veda.id'), primary_key=True)
    id_VEDA_motivo = dba.Column(dba.Integer, dba.ForeignKey('veda_motivo.id'), primary_key=True)

    veda = relationship("Veda", backref=backref("veda_veda_motivo", cascade="all, delete-orphan"))
    veda_motivo = relationship("Veda_Motivo", backref=backref("veda_veda_motivo", cascade="all, delete-orphan"))


class Veda_Veda_Hallazgo(dba.Model):
    """
        Clase que modela la relacion muchos a muchos entre VEDA y motivos de VEDA
    """

    __tablename__ = "veda_veda_hallazgo"

    id_VEDA = dba.Column(dba.Integer, dba.ForeignKey('veda.id'), primary_key=True)
    id_VEDA_hallazgo = dba.Column(dba.Integer, dba.ForeignKey('veda_hallazgo.id'), primary_key=True)

    veda = relationship("Veda", backref=backref("veda_veda_hallazgo", cascade="all, delete-orphan"))
    veda_hallazgo = relationship("Veda_Hallazgo", backref=backref("veda_veda_hallazgo", cascade="all, delete-orphan"))

