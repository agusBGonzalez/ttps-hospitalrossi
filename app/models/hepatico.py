from flask.helpers import flash
from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import text
from datetime import date
import sys

dba = SQLAlchemy()


class Hepa(dba.Model):
    __tablename__ = "hepa"
    id = dba.Column(dba.Integer, primary_key=True, autoincrement=True)
    fecha = dba.Column(dba.Date)
    id_operador = dba.Column(dba.Integer, unique=False, nullable=True)
    consultorio = dba.Column(dba.Boolean, nullable=False)
    # evento de descompensacion (obligatorio) no se si es multiple o unico lo hago como si fuera unico
    id_HEPA_descompensacion = dba.Column(dba.Integer)
    id_HEPA_child_pugh = dba.Column(dba.Integer)
    # CIRROSIS - ETIOLOGÍA (opcional) no se si multiple o unico, lo hago como multiple
    hepatocarcinoma = dba.Column(dba.Boolean, nullable=False)
    lesion_focal_hepatica = dba.Column(dba.Boolean, nullable=False)
    meld = dba.Column(dba.Integer)
    id_historia = dba.Column(dba.Integer)

    etiologias = relationship(
        "Hepa_Etiologia", secondary="hepa_hepa_etiologia")
    cirrosis_etiologias = relationship(
        "Hepa_Cirrosis_Etiologia", secondary="hepa_hepa_cirrosis_etiologia")

    @classmethod
    def find_by_id(cls, id):
        hepa = Hepa.query.filter_by(id=id).one_or_none()
        return hepa

    @classmethod
    def create(cls, data):
        print(data["meld"], file=sys.stderr)

        evento = Hepa(
            fecha=data["fecha"],
            id_operador=data["id_operador"],
            consultorio=(data["consultorio"] == "1"),
            id_HEPA_descompensacion=data["id_HEPA_descompensacion"],
            hepatocarcinoma=(data["hepatocarcinoma"] == "1"),
            lesion_focal_hepatica=(data["lesion_focal_hepatica"] == "1"),
            meld=data["meld"],
            id_HEPA_child_pugh=data["id_HEPA_child_pugh"],
            id_historia=data["id_historia"]
        )
        evento.zero_to_null()
        ids_etiologias = data.getlist('etiologias')
        for id_etiologia in ids_etiologias:
            etiologia = Hepa_Etiologia.find_by_id(id_etiologia)
            evento.etiologias.append(etiologia)

        ids_cirrosis_etiologias = data.getlist('cirrosis_etiologias')
        for id_cirrosis_etiologia in ids_cirrosis_etiologias:
            cirrosis_etiologia = Hepa_Cirrosis_Etiologia.find_by_id(
                id_cirrosis_etiologia)
            evento.cirrosis_etiologias.append(cirrosis_etiologia)
        # try:
        #     dba.session.add(evento)
        #     dba.session.commit()
        #     return evento
        # except:
        #     dba.session.rollback()
        #     return False

        dba.session.add(evento)
        dba.session.commit()
        return evento

    @classmethod
    def modify(cls, evento, data):
        evento.fecha = data["fecha"]
        evento.consultorio = data["consultorio"]
        evento.id_HEPA_descompensacion = data["id_HEPA_descompensacion"]
        evento.hepatocarcinoma = data["hepatocarcinoma"]
        evento.lesion_focal_hepatica = data["lesion_focal_hepatica"]
        evento.meld = data["meld"]
        evento.id_HEPA_child_pugh = data["id_HEPA_child_pugh"]

        evento.zero_to_null()

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
        if self.id_HEPA_descompensacion == "0":
            self.id_HEPA_descompensacion = None
        if self.id_HEPA_child_pugh == "0":
            self.id_HEPA_child_pugh = None


class Hepa_Descompensacion(dba.Model):
    __tablename__ = "hepa_descompensacion"
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.descripcion

    @classmethod
    def all(cls):
        """ Devuelve el total de filas de la tabla 
        """
        return Hepa_Descompensacion.query.order_by(Hepa_Descompensacion.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
        """ 
        devuelve el primer elemento de la tabla Hepa_descompensacion que coincida con el parametro indicado para id
        """
        return Hepa_Descompensacion.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
        """ 
        devuelve el primer elemento de la tabla Hepa_descompensacion que coincida con el parametro indicado para descripcion
        """
        return Hepa_Descompensacion.query.filter_by(descripcion=nombre).one_or_none()


class Hepa_child_pugh(dba.Model):
    __tablename__ = "hepa_child_pugh"
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
        return self.descripcion

    @classmethod
    def all(cls):
        """ Devuelve el total de filas de la tabla 
        """
        return Hepa_child_pugh.query.order_by(Hepa_child_pugh.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
        """ 
        devuelve el primer elemento de la tabla Hepa_child_pugh que coincida con el parametro indicado para id
        """
        return Hepa_child_pugh.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
        """ 
        devuelve el primer elemento de la tabla Hepa_child_pugh que coincida con el parametro indicado para descripcion
        """
        return Hepa_child_pugh.query.filter_by(descripcion=nombre).one_or_none()


class Hepa_Etiologia(dba.Model):
    __tablename__ = "hepa_etiologia"
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)
    hepas = relationship("Hepa", secondary="hepa_hepa_etiologia")

    def __repr__(self):
        return self.descripcion

    @classmethod
    def all(cls):
        """ Devuelve el total de filas de la tabla 
        """
        return Hepa_Etiologia.query.order_by(Hepa_Etiologia.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
        """ 
        devuelve el primer elemento de la tabla Hepa_Etiologia que coincida con el parametro indicado para id
        """
        return Hepa_Etiologia.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
        """ 
        devuelve el primer elemento de la tabla Hepa_Etiologia que coincida con el parametro indicado para descripcion
        """
        return Hepa_Etiologia.query.filter_by(descripcion=nombre).one_or_none()


class Hepa_Hepa_Etiologia(dba.Model):
    """
        Clase que modela la relacion muchos a muchos entre HEPA y etiologia de HEPA
    """

    __tablename__ = "hepa_hepa_etiologia"

    id_HEPA = dba.Column(dba.Integer, dba.ForeignKey(
        'hepa.id'), primary_key=True)
    id_HEPA_etiologia = dba.Column(dba.Integer, dba.ForeignKey(
        'hepa_etiologia.id'), primary_key=True)

    hepa = relationship("Hepa", backref=backref(
        "hepa_hepa_etiologia", cascade="all, delete-orphan"))
    hepa_etiologia = relationship("Hepa_Etiologia", backref=backref(
        "hepa_hepa_etiologia", cascade="all, delete-orphan"))


class Hepa_Cirrosis_Etiologia(dba.Model):
    __tablename__ = "hepa_cirrosis_etiologia"
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)
    hepas = relationship("Hepa", secondary="hepa_hepa_cirrosis_etiologia")

    def __repr__(self):
        return self.descripcion

    @classmethod
    def all(cls):
        """ Devuelve el total de filas de la tabla 
        """
        return Hepa_Cirrosis_Etiologia.query.order_by(Hepa_Cirrosis_Etiologia.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
        """ 
        devuelve el primer elemento de la tabla Hepa_Cirrosis_Etiologia que coincida con el parametro indicado para id
        """
        return Hepa_Cirrosis_Etiologia.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
        """ 
        devuelve el primer elemento de la tabla Hepa_Cirrosis_Etiologia que coincida con el parametro indicado para descripcion
        """
        return Hepa_Cirrosis_Etiologia.query.filter_by(descripcion=nombre).one_or_none()


class Hepa_Hepa_Cirrosis_Etiologia(dba.Model):
    """
        Clase que modela la relacion muchos a muchos entre HEPA y cirrosis etiologia de HEPA
    """

    __tablename__ = "hepa_hepa_cirrosis_etiologia"

    id_HEPA = dba.Column(dba.Integer, dba.ForeignKey(
        'hepa.id'), primary_key=True)
    id_HEPA_cirrosis_etiologia = dba.Column(dba.Integer, dba.ForeignKey(
        'hepa_cirrosis_etiologia.id'), primary_key=True)

    hepa = relationship("Hepa", backref=backref(
        "hepa_hepa_cirrosis_etiologia", cascade="all, delete-orphan"))
    hepa_cirrosis_etiologia = relationship("Hepa_Cirrosis_Etiologia", backref=backref(
        "hepa_hepa_cirrosis_etiologia", cascade="all, delete-orphan"))
