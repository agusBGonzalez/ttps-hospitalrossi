from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import text
from datetime import date
import sys

dba = SQLAlchemy()

class Vcc(dba.Model):
    __tablename__ = "vcc"

    id = dba.Column(dba.Integer, primary_key=True, autoincrement=True)
    comentarios = dba.Column(dba.String(4000), unique=True, nullable=False)
    fecha =  dba.Column(dba.Date)
    id_historia =  dba.Column(dba.Integer)

    id_operador =  dba.Column(dba.Integer)
    id_vcc_preparacion =  dba.Column(dba.Integer)
    boston_izq =  dba.Column(dba.Integer)
    boston_trasv =  dba.Column(dba.Integer)
    boston_der =  dba.Column(dba.Integer)
    id_VCC_incompleta_hasta =  dba.Column(dba.Integer)
    id_VCC_incompleta_motivo =  dba.Column(dba.Integer)
    id_VCC_lesion_sospechosa =  dba.Column(dba.Integer)
    id_VCC_polipos_cant =  dba.Column(dba.Integer)
    id_VCC_polipectomia_tam =  dba.Column(dba.Integer)
    id_VCC_polipectomia_material =  dba.Column(dba.Integer)
    id_VCC_polipectomia_tecnica =  dba.Column(dba.Integer)
    id_VCC_polipectomia_paris =  dba.Column(dba.Integer)
    ileoscopia =  dba.Column(dba.Integer)
    id_VCC_de_guardia =  dba.Column(dba.Integer)
    id_VCC_tiempo_ingreso =  dba.Column(dba.Integer)
    id_VCC_tiempo_retirada =  dba.Column(dba.Integer)

    biopsias = relationship("Vcc_Biopsias", secondary="vcc_vcc_biopsias")
    complicaciones = relationship("Vcc_Complicaciones", secondary="vcc_vcc_complicaciones")
    hallazgos = relationship("Vcc_Hallazgos", secondary="vcc_vcc_hallazgos")
    motivos = relationship("Vcc_Motivo", secondary="vcc_vcc_motivo")
    terapeuticas = relationship("Vcc_Terapeutica", secondary="vcc_vcc_terapeutica")


    @classmethod
    def find_by_id(cls, id):
        vcc =  Vcc.query.filter_by(id=id).one_or_none()
        return vcc

    @classmethod
    def create(cls, data):
    
        evento = Vcc(
                    comentarios=data["comentarios"],
                    fecha=data["fecha"],
                    id_historia=data["id_historia"],
                    id_operador=data["id_operador"],
                    id_vcc_preparacion=data["id_vcc_preparacion"],
                    id_VCC_incompleta_hasta=data["id_VCC_incompleta_hasta"],
                    id_VCC_incompleta_motivo=data["id_VCC_incompleta_motivo"],
                    id_VCC_lesion_sospechosa=data["id_VCC_lesion_sospechosa"],
                    id_VCC_polipos_cant=data["id_VCC_polipos_cant"],
                    id_VCC_polipectomia_tam=data["id_VCC_polipectomia_tam"],
                    id_VCC_polipectomia_material=data["id_VCC_polipectomia_material"],
                    id_VCC_polipectomia_tecnica=data["id_VCC_polipectomia_tecnica"],
                    id_VCC_polipectomia_paris=data["id_VCC_polipectomia_paris"],
                    ileoscopia=data["ileoscopia"],
                    id_VCC_de_guardia=data["id_VCC_de_guardia"],
                    id_VCC_tiempo_ingreso=data["id_VCC_tiempo_ingreso"],
                    id_VCC_tiempo_retirada=data["id_VCC_tiempo_retirada"] 
                    )

        boston_izq = data.get('boston_izq', None)
        boston_der = data.get('boston_der', None)
        boston_trasv = data.get('boston_trasv', None)

        try:
            evento.boston_izq = int(boston_izq)
        except:
            evento.boston_izq = None

        try:
            evento.boston_trasv = int(boston_trasv)
        except:
            evento.boston_trasv = None

        try:
            evento.boston_der = int(boston_der)
        except:
            evento.boston_der = None


        evento.zero_to_null()            

        ids_motivos = data.getlist('motivos')
        for id_motivo in ids_motivos:
            motivo = Vcc_Motivo.find_by_id(id_motivo)
            evento.motivos.append(motivo)

        ids_hallazgos = data.getlist('hallazgos')
        for id_hallazgo in ids_hallazgos:
            hallazgo = Vcc_Hallazgos.find_by_id(id_hallazgo)
            evento.hallazgos.append(hallazgo)

        ids = data.getlist('biopsias')
        for id in ids:
            elem = Vcc_Biopsias.find_by_id(id)
            evento.biopsias.append(elem)

        ids = data.getlist('complicaciones')
        for id in ids:
            elem = Vcc_Complicaciones.find_by_id(id)
            evento.complicaciones.append(elem)

        ids = data.getlist('terapeuticas')
        for id in ids:
            elem = Vcc_Terapeutica.find_by_id(id)
            evento.terapeuticas.append(elem)

        try:
            dba.session.add(evento)
            dba.session.commit()
            
            return evento
        except:
            dba.session.rollback()
            return False

    @classmethod
    def modify(cls, evento, data):
        
        boston_izq = data.get('boston_izq', None)
        boston_der = data.get('boston_der', None)
        boston_trasv = data.get('boston_trasv', None)

        try:
            evento.boston_izq = int(boston_izq)
        except:
            evento.boston_izq = None

        try:
            evento.boston_trasv = int(boston_trasv)
        except:
            evento.boston_trasv = None

        try:
            evento.boston_der = int(boston_der)
        except:
            evento.boston_der = None

        evento.comentarios=data["comentarios"]
        evento.fecha=data["fecha"]
        evento.id_operador=data["id_operador"]
        evento.id_vcc_preparacion=data["id_vcc_preparacion"]
        #evento.boston_izq=data["boston_izq"]
        #evento.boston_trasv=data["boston_trasv"]
        #evento.boston_der=data["boston_der"]
        evento.id_VCC_incompleta_hasta=data["id_VCC_incompleta_hasta"]
        evento.id_VCC_incompleta_motivo=data["id_VCC_incompleta_motivo"]
        evento.id_VCC_lesion_sospechosa=data["id_VCC_lesion_sospechosa"]
        evento.id_VCC_polipos_cant=data["id_VCC_polipos_cant"]
        evento.id_VCC_polipectomia_tam=data["id_VCC_polipectomia_tam"]
        evento.id_VCC_polipectomia_material=data["id_VCC_polipectomia_material"]
        evento.id_VCC_polipectomia_tecnica=data["id_VCC_polipectomia_tecnica"]
        evento.id_VCC_polipectomia_paris=data["id_VCC_polipectomia_paris"]
        evento.ileoscopia=data["ileoscopia"]
        evento.id_VCC_de_guardia=data["id_VCC_de_guardia"]
        evento.id_VCC_tiempo_ingreso=data["id_VCC_tiempo_ingreso"]
        evento.id_VCC_tiempo_retirada=data["id_VCC_tiempo_retirada"]

        evento.zero_to_null()
        
        ids_motivos = data.getlist('motivos')
        evento.motivos.clear()
        for id_motivo in ids_motivos:
            motivo = Vcc_Motivo.find_by_id(id_motivo)
            evento.motivos.append(motivo)

        ids_hallazgos = data.getlist('hallazgos')
        evento.hallazgos.clear()
        for id_hallazgo in ids_hallazgos:
            hallazgo = Vcc_Hallazgos.find_by_id(id_hallazgo)
            evento.hallazgos.append(hallazgo)

        ids = data.getlist('biopsias')
        evento.biopsias.clear()
        for id in ids:
            elem = Vcc_Biopsias.find_by_id(id)
            evento.biopsias.append(elem)

        ids = data.getlist('complicaciones')
        evento.complicaciones.clear()
        for id in ids:
            elem = Vcc_Complicaciones.find_by_id(id)
            evento.complicaciones.append(elem)

        ids = data.getlist('terapeuticas')
        evento.terapeuticas.clear()
        for id in ids:
            elem = Vcc_Terapeutica.find_by_id(id)
            evento.terapeuticas.append(elem)

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
        if self.id_VCC_incompleta_hasta=="0":
            self.id_VCC_incompleta_hasta = None 
        if self.id_VCC_incompleta_motivo=="0":
            self.id_VCC_incompleta_motivo = None
        if self.id_VCC_lesion_sospechosa=="0":
            self.id_VCC_lesion_sospechosa = None
        if self.id_VCC_lesion_sospechosa=="0":
            self.id_VCC_lesion_sospechosa = None
        if self.id_VCC_polipos_cant=="0":
            self.id_VCC_polipos_cant = None
        if self.id_VCC_polipectomia_tam=="0":
            self.id_VCC_polipectomia_tam = None
        if self.id_VCC_polipectomia_material=="0":
            self.id_VCC_polipectomia_material = None
        if self.id_VCC_polipectomia_tecnica=="0":
            self.id_VCC_polipectomia_tecnica = None
        if self.id_VCC_polipectomia_paris=="0":
            self.id_VCC_polipectomia_paris = None
        if self.id_VCC_de_guardia=="0":
            self.id_VCC_de_guardia = None
        if self.id_operador=="0":
            self.id_operador = None


class Vcc_Biopsias(dba.Model):
    __tablename__ = "vcc_biopsias" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Biopsias.query.order_by(Vcc_Biopsias.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Biopsias que coincida con el parametro indicado para id
      """ 
      return Vcc_Biopsias.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Biopsias que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Biopsias.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Complicaciones(dba.Model):
    __tablename__ = "vcc_complicaciones" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Complicaciones.query.order_by(Vcc_Complicaciones.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Complicaciones que coincida con el parametro indicado para id
      """ 
      return Vcc_Complicaciones.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Complicaciones que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Complicaciones.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_De_Guardia(dba.Model):
    __tablename__ = "vcc_de_guardia" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_De_Guardia.query.order_by(Vcc_De_Guardia.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_De_Guardia que coincida con el parametro indicado para id
      """ 
      return Vcc_De_Guardia.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_De_Guardia que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_De_Guardia.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Hallazgos(dba.Model):
    __tablename__ = "vcc_hallazgos" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Hallazgos.query.order_by(Vcc_Hallazgos.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Hallazgos que coincida con el parametro indicado para id
      """ 
      return Vcc_Hallazgos.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Hallazgos que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Hallazgos.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Incompleta_Hasta(dba.Model):
    __tablename__ = "vcc_incompleta_hasta" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Incompleta_Hasta.query.order_by(Vcc_Incompleta_Hasta.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Incompleta_Hasta que coincida con el parametro indicado para id
      """ 
      return Vcc_Incompleta_Hasta.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Incompleta_Hasta que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Incompleta_Hasta.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Incompleta_Motivo(dba.Model):
    __tablename__ = "vcc_incompleta_motivo" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Incompleta_Motivo.query.order_by(Vcc_Incompleta_Motivo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Incompleta_Motivo que coincida con el parametro indicado para id
      """ 
      return Vcc_Incompleta_Motivo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Incompleta_Motivo que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Incompleta_Motivo.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Lesion_Sospechosa(dba.Model):
    __tablename__ = "vcc_lesion_sospechosa" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Lesion_Sospechosa.query.order_by(Vcc_Lesion_Sospechosa.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Lesion_Sospechosa que coincida con el parametro indicado para id
      """ 
      return Vcc_Lesion_Sospechosa.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Lesion_Sospechosa que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Lesion_Sospechosa.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Motivo(dba.Model):
    __tablename__ = "vcc_motivo" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Motivo.query.order_by(Vcc_Motivo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Motivo que coincida con el parametro indicado para id
      """ 
      return Vcc_Motivo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Motivo que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Motivo.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Polipectomia_Material(dba.Model):
    __tablename__ = "vcc_polipectomia_material" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Polipectomia_Material.query.order_by(Vcc_Polipectomia_Material.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Material que coincida con el parametro indicado para id
      """ 
      return Vcc_Polipectomia_Material.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Material que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Polipectomia_Material.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Polipectomia_Paris(dba.Model):
    __tablename__ = "vcc_polipectomia_paris" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Polipectomia_Paris.query.order_by(Vcc_Polipectomia_Paris.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Paris que coincida con el parametro indicado para id
      """ 
      return Vcc_Polipectomia_Paris.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Paris que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Polipectomia_Paris.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Polipectomia_Tam(dba.Model):
    __tablename__ = "vcc_polipectomia_tam" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Polipectomia_Tam.query.order_by(Vcc_Polipectomia_Tam.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Tam que coincida con el parametro indicado para id
      """ 
      return Vcc_Polipectomia_Tam.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Tam que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Polipectomia_Tam.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Polipectomia_Tecnica(dba.Model):
    __tablename__ = "vcc_polipectomia_tecnica" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Polipectomia_Tecnica.query.order_by(Vcc_Polipectomia_Tecnica.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Tecnica que coincida con el parametro indicado para id
      """ 
      return Vcc_Polipectomia_Tecnica.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipectomia_Tecnica que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Polipectomia_Tecnica.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Polipos_Cant(dba.Model):
    __tablename__ = "vcc_polipos_cant" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Polipos_Cant.query.order_by(Vcc_Polipos_Cant.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipos_Cant que coincida con el parametro indicado para id
      """ 
      return Vcc_Polipos_Cant.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Polipos_Cant que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Polipos_Cant.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Preparacion(dba.Model):
    __tablename__ = "vcc_preparacion" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Preparacion.query.order_by(Vcc_Preparacion.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Preparacion que coincida con el parametro indicado para id
      """ 
      return Vcc_Preparacion.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Preparacion que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Preparacion.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Terapeutica(dba.Model):
    __tablename__ = "vcc_terapeutica" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Terapeutica.query.order_by(Vcc_Terapeutica.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Terapeutica que coincida con el parametro indicado para id
      """ 
      return Vcc_Terapeutica.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Terapeutica que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Terapeutica.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Tiempo_Ingreso(dba.Model):
    __tablename__ = "vcc_tiempo_ingreso" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Tiempo_Ingreso.query.order_by(Vcc_Tiempo_Ingreso.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Tiempo_Ingreso que coincida con el parametro indicado para id
      """ 
      return Vcc_Tiempo_Ingreso.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Tiempo_Ingreso que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Tiempo_Ingreso.query.filter_by(descripcion=nombre).one_or_none()


class Vcc_Tiempo_Retirada(dba.Model):
    __tablename__ = "vcc_tiempo_retirada" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Vcc_Tiempo_Retirada.query.order_by(Vcc_Tiempo_Retirada.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Vcc_Tiempo_Retirada que coincida con el parametro indicado para id
      """ 
      return Vcc_Tiempo_Retirada.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Vcc_Tiempo_Retirada que coincida con el parametro indicado para descripcion
      """ 
      return Vcc_Tiempo_Retirada.query.filter_by(descripcion=nombre).one_or_none()

class Vcc_Vcc_Biopsias(dba.Model):
    """
    Clase que modela la relacion muchos a muchos entre Vcc y Vcc_Biopsias
    """

    __tablename__ = "vcc_vcc_biopsias"

    id_VCC = dba.Column(dba.Integer, dba.ForeignKey('vcc.id'), primary_key=True)
    id_VCC_biopsias = dba.Column(dba.Integer, dba.ForeignKey('vcc_biopsias.id'), primary_key=True)

    vcc = relationship("Vcc", backref=backref("vcc_vcc_biopsias", cascade="all, delete-orphan"))
    vcc_biopsias = relationship("Vcc_Biopsias", backref=backref("vcc_vcc_biopsias", cascade="all, delete-orphan"))




class Vcc_Vcc_Complicaciones(dba.Model):
    """
    Clase que modela la relacion muchos a muchos entre Vcc y Vcc_Complicaciones
    """

    __tablename__ = "vcc_vcc_complicaciones"

    id_VCC = dba.Column(dba.Integer, dba.ForeignKey('vcc.id'), primary_key=True)
    id_VCC_complicaciones = dba.Column(dba.Integer, dba.ForeignKey('vcc_complicaciones.id'), primary_key=True)

    vcc = relationship("Vcc", backref=backref("vcc_vcc_complicaciones", cascade="all, delete-orphan"))
    vcc_complicaciones = relationship("Vcc_Complicaciones", backref=backref("vcc_vcc_complicaciones", cascade="all, delete-orphan"))




class Vcc_Vcc_Hallazgos(dba.Model):
    """
    Clase que modela la relacion muchos a muchos entre Vcc y Vcc_Hallazgos
    """

    __tablename__ = "vcc_vcc_hallazgos"

    id_VCC = dba.Column(dba.Integer, dba.ForeignKey('vcc.id'), primary_key=True)
    id_VCC_hallazgos = dba.Column(dba.Integer, dba.ForeignKey('vcc_hallazgos.id'), primary_key=True)

    vcc = relationship("Vcc", backref=backref("vcc_vcc_hallazgos", cascade="all, delete-orphan"))
    vcc_hallazgos = relationship("Vcc_Hallazgos", backref=backref("vcc_vcc_hallazgos", cascade="all, delete-orphan"))




class Vcc_Vcc_Motivo(dba.Model):
    """
    Clase que modela la relacion muchos a muchos entre Vcc y Vcc_Motivo
    """

    __tablename__ = "vcc_vcc_motivo"

    id_VCC = dba.Column(dba.Integer, dba.ForeignKey('vcc.id'), primary_key=True)
    id_VCC_motivo = dba.Column(dba.Integer, dba.ForeignKey('vcc_motivo.id'), primary_key=True)

    vcc = relationship("Vcc", backref=backref("vcc_vcc_motivo", cascade="all, delete-orphan"))
    vcc_motivo = relationship("Vcc_Motivo", backref=backref("vcc_vcc_motivo", cascade="all, delete-orphan"))




class Vcc_Vcc_Terapeutica(dba.Model):
    """
    Clase que modela la relacion muchos a muchos entre Vcc y Vcc_Terapeutica
    """

    __tablename__ = "vcc_vcc_terapeutica"

    id_VCC = dba.Column(dba.Integer, dba.ForeignKey('vcc.id'), primary_key=True)
    id_VCC_terapeutica = dba.Column(dba.Integer, dba.ForeignKey('vcc_terapeutica.id'), primary_key=True)

    vcc = relationship("Vcc", backref=backref("vcc_vcc_terapeutica", cascade="all, delete-orphan"))
    vcc_terapeutica = relationship("Vcc_Terapeutica", backref=backref("vcc_vcc_terapeutica", cascade="all, delete-orphan"))
