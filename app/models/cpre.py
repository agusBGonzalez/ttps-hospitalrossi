from flask_sqlalchemy import SQLAlchemy
import datetime
from sqlalchemy.orm import relationship, backref
from sqlalchemy import text
from datetime import date
import sys

dba = SQLAlchemy()


class Cpre(dba.Model):

    __tablename__ = "cpre"
    id = dba.Column(dba.Integer, primary_key=True, autoincrement=True)
    comentarios = dba.Column(dba.String(4000), unique=True, nullable=False)
    fecha =  dba.Column(dba.Date)
    id_historia =  dba.Column(dba.Integer)
    id_operador =  dba.Column(dba.Integer)
    ASA  =  dba.Column(dba.Integer)
    ambulatorio = dba.Column(dba.Boolean, nullable=False)
    cpre_previa = dba.Column(dba.Boolean, nullable=False)
    BILIRRUBINA = dba.Column(dba.String(2000), nullable=True)
    FAL = dba.Column(dba.String(2000), nullable=True)
    TGP = dba.Column(dba.String(2000), nullable=True)
    TGO = dba.Column(dba.String(2000), nullable=True)
    AMILASA = dba.Column(dba.String(2000), nullable=True)
    GGT = dba.Column(dba.String(2000), nullable=True)
    GB = dba.Column(dba.String(2000), nullable=True)
    FR_DE_PA_SOD = dba.Column(dba.Boolean, nullable=False)
    FR_DE_PA_AUSENCIA_PC = dba.Column(dba.Boolean, nullable=False)
    FR_DE_PA_ANTEC_PA = dba.Column(dba.Boolean, nullable=False)
    CPRE_normal = dba.Column(dba.Boolean, nullable=False)
    id_CPRE_EPT  =  dba.Column(dba.Integer)
    ESFINTEROPLASTIA = dba.Column(dba.Boolean, nullable=False)
    id_CPRE_WIRSUNG  =  dba.Column(dba.Integer)
    id_CPRE_PRECORTE  =  dba.Column(dba.Integer)
    id_CPRE_Dilatacion_biliar  =  dba.Column(dba.Integer)
    id_CPRE_Litotripsia  =  dba.Column(dba.Integer)
    id_CPRE_stent_plastico  =  dba.Column(dba.Integer)
    id_CPRE_stent_autoexp  =  dba.Column(dba.Integer)
    stent_duodenal = dba.Column(dba.Boolean, nullable=False)
    RX_dosis = dba.Column(dba.String(2000), nullable=True)
    DPA = dba.Column(dba.String(2000), nullable=True)
    RX_tiempo = dba.Column(dba.String(2000), nullable=True)
    nro_sesiones  =  dba.Column(dba.Integer)
    resolucion_completa = dba.Column(dba.Boolean, nullable=False)
    id_CPRE_AMILASEMIA_2HS  =  dba.Column(dba.Integer)
    canulacion = dba.Column(dba.Boolean, nullable=False)
    biopsias = dba.Column(dba.Boolean, nullable=False)
    citologia = dba.Column(dba.String(2000), nullable=True)
    fracaso = dba.Column(dba.Boolean, nullable=False)
    embarazo = dba.Column(dba.Boolean, nullable=False)
    hospital_derivacion = dba.Column(dba.String(2000), nullable=True)
    id_cpre_grado_asge  =  dba.Column(dba.Integer) 
    id_cpre_grado_dif  =  dba.Column(dba.Integer) 

    cirugia_prev_list = relationship("Cpre_Cirugia_Prev", secondary="cpre_cpre_cirugia_prev")
    coledocolitiasis_list = relationship("Cpre_Coledocolitiasis", secondary="cpre_cpre_coledocolitiasis")
    complicaciones_list = relationship("Cpre_Complicaciones", secondary="cpre_cpre_complicaciones")
    diverticulo_list = relationship("Cpre_Diverticulo", secondary="cpre_cpre_diverticulo")
    eco_abd_list = relationship("Cpre_Eco_Abd", secondary="cpre_cpre_eco_abd")
    estenosis_alta_list = relationship("Cpre_Estenosis_Alta", secondary="cpre_cpre_estenosis_alta")
    estenosis_baja_list = relationship("Cpre_Estenosis_Baja", secondary="cpre_cpre_estenosis_baja")
    eus_list = relationship("Cpre_Eus", secondary="cpre_cpre_eus")
    #grado_asge_list = relationship("Cpre_Grado_Asge", secondary="cpre_cpre_grado_asge")
    #grado_dif_list = relationship("Cpre_Grado_Dif", secondary="cpre_cpre_grado_dif")
    indicacion_list = relationship("Cpre_Indicacion", secondary="cpre_cpre_indicacion")
    indicacion_asge_list = relationship("Cpre_Indicacion_Asge", secondary="cpre_cpre_indicacion_asge")
    indicacion_ept_list = relationship("Cpre_Indicacion_Ept", secondary="cpre_cpre_indicacion_ept")
    lpqvb_list = relationship("Cpre_Lpqvb", secondary="cpre_cpre_lpqvb")
    miscelaneas_list = relationship("Cpre_Miscelaneas", secondary="cpre_cpre_miscelaneas")
    profilaxis_atb_list = relationship("Cpre_Profilaxis_Atb", secondary="cpre_cpre_profilaxis_atb")
    resolucion_complica_list = relationship("Cpre_Resolucion_Complica", secondary="cpre_cpre_resolucion_complica")
    rnm_list = relationship("Cpre_Rnm", secondary="cpre_cpre_rnm")
    tac_list = relationship("Cpre_Tac", secondary="cpre_cpre_tac")
    terap_pancreas_list = relationship("Cpre_Terap_Pancreas", secondary="cpre_cpre_terap_pancreas")
    transk_list = relationship("Cpre_Transk", secondary="cpre_cpre_transk")

    @classmethod
    def find_by_id(cls, id):
        cpre =  Cpre.query.filter_by(id=id).one_or_none()
        return cpre

    @classmethod
    def create(cls, data):
    
        evento = Cpre(
                    comentarios=data["comentarios"],
                    fecha=data["fecha"],
                    id_historia=data["id_historia"],
                    id_operador=data["id_operador"],
                    ASA=data["ASA"],
                    ambulatorio=data["ambulatorio"],
                    cpre_previa=data["cpre_previa"],
                    BILIRRUBINA=data["BILIRRUBINA"],
                    FAL=data["FAL"],
                    TGP=data["TGP"],
                    TGO=data["TGO"],
                    AMILASA=data["AMILASA"],
                    GGT=data["GGT"],
                    GB=data["GB"],
                    FR_DE_PA_SOD=data["FR_DE_PA_SOD"],
                    FR_DE_PA_AUSENCIA_PC=data["FR_DE_PA_AUSENCIA_PC"],
                    FR_DE_PA_ANTEC_PA=data["FR_DE_PA_ANTEC_PA"],
                    CPRE_normal=data["CPRE_normal"],
                    id_CPRE_EPT=data["id_CPRE_EPT"],
                    ESFINTEROPLASTIA=data["ESFINTEROPLASTIA"],
                    id_CPRE_WIRSUNG=data["id_CPRE_WIRSUNG"],
                    id_CPRE_PRECORTE=data["id_CPRE_PRECORTE"],
                    id_CPRE_Dilatacion_biliar=data["id_CPRE_Dilatacion_biliar"],
                    id_CPRE_Litotripsia=data["id_CPRE_Litotripsia"],
                    id_CPRE_stent_plastico=data["id_CPRE_stent_plastico"],
                    id_CPRE_stent_autoexp=data["id_CPRE_stent_autoexp"],
                    stent_duodenal=data["stent_duodenal"],
                    RX_dosis=data["RX_dosis"],
                    DPA=data["DPA"],
                    RX_tiempo=data["RX_tiempo"],
                    nro_sesiones=data["nro_sesiones"],
                    resolucion_completa=data["resolucion_completa"],
                    id_CPRE_AMILASEMIA_2HS=data["id_CPRE_AMILASEMIA_2HS"],
                    canulacion=data["canulacion"],
                    biopsias=data["biopsias"],
                    citologia=data["citologia"],
                    fracaso=data["fracaso"],
                    embarazo=data["embarazo"],
                    hospital_derivacion=data["hospital_derivacion"],
                    id_cpre_grado_asge=data["id_cpre_grado_asge"],
                    id_cpre_grado_dif=data["id_cpre_grado_dif"]
                )
        evento.zero_to_null()

        evento.addList('cirugia_prev_list', data.getlist('cirugia_prev_list'), Cpre_Cirugia_Prev)
        evento.addList('coledocolitiasis_list', data.getlist('coledocolitiasis_list'), Cpre_Coledocolitiasis)
        evento.addList('complicaciones_list', data.getlist('complicaciones_list'), Cpre_Complicaciones)
        evento.addList('diverticulo_list', data.getlist('diverticulo_list'), Cpre_Diverticulo)
        evento.addList('eco_abd_list', data.getlist('eco_abd_list'), Cpre_Eco_Abd)
        evento.addList('estenosis_alta_list', data.getlist('estenosis_alta_list'), Cpre_Estenosis_Alta)
        evento.addList('estenosis_baja_list', data.getlist('estenosis_baja_list'), Cpre_Estenosis_Baja)
        evento.addList('eus_list', data.getlist('eus_list'), Cpre_Eus)
        #evento.addList('grado_asge_list', data.getlist('grado_asge_list'), Cpre_Grado_Asge)
        #evento.addList('grado_dif_list', data.getlist('grado_dif_list'), Cpre_Grado_Dif)
        evento.addList('indicacion_list', data.getlist('indicacion_list'), Cpre_Indicacion)
        evento.addList('indicacion_asge_list', data.getlist('indicacion_asge_list'), Cpre_Indicacion_Asge)
        evento.addList('indicacion_ept_list', data.getlist('indicacion_ept_list'), Cpre_Indicacion_Ept)
        evento.addList('lpqvb_list', data.getlist('lpqvb_list'), Cpre_Lpqvb)
        evento.addList('miscelaneas_list', data.getlist('miscelaneas_list'), Cpre_Miscelaneas)
        evento.addList('profilaxis_atb_list', data.getlist('profilaxis_atb_list'), Cpre_Profilaxis_Atb)
        evento.addList('resolucion_complica_list', data.getlist('resolucion_complica_list'), Cpre_Resolucion_Complica)
        evento.addList('rnm_list', data.getlist('rnm_list'), Cpre_Rnm)
        evento.addList('tac_list', data.getlist('tac_list'), Cpre_Tac)
        evento.addList('terap_pancreas_list', data.getlist('terap_pancreas_list'), Cpre_Terap_Pancreas)
        evento.addList('transk_list', data.getlist('transk_list'), Cpre_Transk)

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

        evento.id_historia=data["id_historia"]
        evento.id_operador=data["id_operador"]
        evento.ASA=data["ASA"]
        evento.ambulatorio=data["ambulatorio"]
        evento.cpre_previa=data["cpre_previa"]
        evento.BILIRRUBINA=data["BILIRRUBINA"]
        evento.FAL=data["FAL"]
        evento.TGP=data["TGP"]
        evento.TGO=data["TGO"]
        evento.AMILASA=data["AMILASA"]
        evento.GGT=data["GGT"]
        evento.GB=data["GB"]
        evento.FR_DE_PA_SOD=data["FR_DE_PA_SOD"]
        evento.FR_DE_PA_AUSENCIA_PC=data["FR_DE_PA_AUSENCIA_PC"]
        evento.FR_DE_PA_ANTEC_PA=data["FR_DE_PA_ANTEC_PA"]
        evento.CPRE_normal=data["CPRE_normal"]
        evento.id_CPRE_EPT=data["id_CPRE_EPT"]
        evento.ESFINTEROPLASTIA=data["ESFINTEROPLASTIA"]
        evento.id_CPRE_WIRSUNG=data["id_CPRE_WIRSUNG"]
        evento.id_CPRE_PRECORTE=data["id_CPRE_PRECORTE"]
        evento.id_CPRE_Dilatacion_biliar=data["id_CPRE_Dilatacion_biliar"]
        evento.id_CPRE_Litotripsia=data["id_CPRE_Litotripsia"]
        evento.id_CPRE_stent_plastico=data["id_CPRE_stent_plastico"]
        evento.id_CPRE_stent_autoexp=data["id_CPRE_stent_autoexp"]
        evento.stent_duodenal=data["stent_duodenal"]
        evento.RX_dosis=data["RX_dosis"]
        evento.DPA=data["DPA"]
        evento.RX_tiempo=data["RX_tiempo"]
        evento.nro_sesiones=data["nro_sesiones"]
        evento.resolucion_completa=data["resolucion_completa"]
        evento.id_CPRE_AMILASEMIA_2HS=data["id_CPRE_AMILASEMIA_2HS"]
        evento.canulacion=data["canulacion"]
        evento.biopsias=data["biopsias"]
        evento.citologia=data["citologia"]
        evento.fracaso=data["fracaso"]
        evento.embarazo=data["embarazo"]
        evento.hospital_derivacion=data["hospital_derivacion"]

        evento.id_cpre_grado_asge=data["id_cpre_grado_asge"]
        evento.id_cpre_grado_dif=data["id_cpre_grado_dif"]

        evento.zero_to_null()

        # ids = data.getlist('cirugia_prev_list')
        # evento.cirugia_prev_list.clear()
        # for id in ids:
        #     elem = Cpre_Cirugia_Prev.find_by_id(id)
        #     evento.cirugia_prev_list.append(elem)

        evento.addList('cirugia_prev_list', data.getlist('cirugia_prev_list'), Cpre_Cirugia_Prev)
        evento.addList('coledocolitiasis_list', data.getlist('coledocolitiasis_list'), Cpre_Coledocolitiasis)
        evento.addList('complicaciones_list', data.getlist('complicaciones_list'), Cpre_Complicaciones)
        evento.addList('diverticulo_list', data.getlist('diverticulo_list'), Cpre_Diverticulo)
        evento.addList('eco_abd_list', data.getlist('eco_abd_list'), Cpre_Eco_Abd)
        evento.addList('estenosis_alta_list', data.getlist('estenosis_alta_list'), Cpre_Estenosis_Alta)
        evento.addList('estenosis_baja_list', data.getlist('estenosis_baja_list'), Cpre_Estenosis_Baja)
        evento.addList('eus_list', data.getlist('eus_list'), Cpre_Eus)
        #evento.addList('grado_asge_list', data.getlist('grado_asge_list'), Cpre_Grado_Asge)
        #evento.addList('grado_dif_list', data.getlist('grado_dif_list'), Cpre_Grado_Dif)
        evento.addList('indicacion_list', data.getlist('indicacion_list'), Cpre_Indicacion)
        evento.addList('indicacion_asge_list', data.getlist('indicacion_asge_list'), Cpre_Indicacion_Asge)
        evento.addList('indicacion_ept_list', data.getlist('indicacion_ept_list'), Cpre_Indicacion_Ept)
        evento.addList('lpqvb_list', data.getlist('lpqvb_list'), Cpre_Lpqvb)
        evento.addList('miscelaneas_list', data.getlist('miscelaneas_list'), Cpre_Miscelaneas)
        evento.addList('profilaxis_atb_list', data.getlist('profilaxis_atb_list'), Cpre_Profilaxis_Atb)
        evento.addList('resolucion_complica_list', data.getlist('resolucion_complica_list'), Cpre_Resolucion_Complica)
        evento.addList('rnm_list', data.getlist('rnm_list'), Cpre_Rnm)
        evento.addList('tac_list', data.getlist('tac_list'), Cpre_Tac)
        evento.addList('terap_pancreas_list', data.getlist('terap_pancreas_list'), Cpre_Terap_Pancreas)
        evento.addList('transk_list', data.getlist('transk_list'), Cpre_Transk)


        try:
            dba.session.commit()
            return evento
        except:
            dba.session.rollback()
            return False

    def addList(self, campo, lista_ids, Clase):
        # agrego las selecciones multiples pasadas en el form
        getattr(self, campo).clear()
        for id in lista_ids:
            elem = Clase.find_by_id(id)
            getattr(self, campo).append(elem)

    
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
        # cambia ceros por None (null) 
        # y corrige los campos booleanos que vienen como texto desde el form
        if self.ASA=="0":
            self.ASA = None
        if self.id_CPRE_EPT=="0":
            self.id_CPRE_EPT = None
        if self.id_CPRE_WIRSUNG=="0":
            self.id_CPRE_WIRSUNG = None
        if self.id_CPRE_PRECORTE=="0":
            self.id_CPRE_PRECORTE = None
        if self.id_CPRE_Dilatacion_biliar=="0":
            self.id_CPRE_Dilatacion_biliar = None
        if self.id_CPRE_Litotripsia=="0":
            self.id_CPRE_Litotripsia = None
        if self.id_CPRE_stent_plastico=="0":
            self.id_CPRE_stent_plastico = None
        if self.id_CPRE_stent_autoexp=="0":
            self.id_CPRE_stent_autoexp = None
        if self.id_CPRE_AMILASEMIA_2HS=="0":
            self.id_CPRE_AMILASEMIA_2HS = None
        if self.id_cpre_grado_asge=="0":
            self.id_cpre_grado_asge = None
        if self.id_cpre_grado_dif=="0":
            self.id_cpre_grado_dif = None


        if self.ambulatorio=="0":
            self.ambulatorio = False
        else:
            self.ambulatorio = True
        if self.cpre_previa=="0":
            self.cpre_previa = False
        else:
            self.cpre_previa = True
        if self.FR_DE_PA_SOD=="0":
            self.FR_DE_PA_SOD = False
        else:
            self.FR_DE_PA_SOD = True
        if self.FR_DE_PA_AUSENCIA_PC=="0":
            self.FR_DE_PA_AUSENCIA_PC = False
        else:
            self.FR_DE_PA_AUSENCIA_PC = True
        if self.FR_DE_PA_ANTEC_PA=="0":
            self.FR_DE_PA_ANTEC_PA = False
        else:
            self.FR_DE_PA_ANTEC_PA = True
        if self.CPRE_normal=="0":
            self.CPRE_normal = False
        else:
            self.CPRE_normal = True
        if self.ESFINTEROPLASTIA=="0":
            self.ESFINTEROPLASTIA = False
        else:
            self.ESFINTEROPLASTIA = True
        if self.stent_duodenal=="0":
            self.stent_duodenal = False
        else:
            self.stent_duodenal = True
        if self.resolucion_completa=="0":
            self.resolucion_completa = False
        else:
            self.resolucion_completa = True
        if self.canulacion=="0":
            self.canulacion = False
        else:
            self.canulacion = True
        if self.biopsias=="0":
            self.biopsias = False
        else:
            self.biopsias = True
        if self.fracaso=="0":
            self.fracaso = False
        else:
            self.fracaso = True
        if self.embarazo=="0":
            self.embarazo = False
        else:
            self.embarazo = True

        return None


class Cpre_Amilasemia_2hs(dba.Model):
    __tablename__ = "cpre_amilasemia_2hs" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Amilasemia_2hs.query.order_by(Cpre_Amilasemia_2hs.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Amilasemia_2hs que coincida con el parametro indicado para id
      """ 
      return Cpre_Amilasemia_2hs.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Amilasemia_2hs que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Amilasemia_2hs.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Asa(dba.Model):
    __tablename__ = "cpre_asa" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Asa.query.order_by(Cpre_Asa.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Asa que coincida con el parametro indicado para id
      """ 
      return Cpre_Asa.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Asa que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Asa.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Cirugia_Prev(dba.Model):
    __tablename__ = "cpre_cirugia_prev" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Cirugia_Prev.query.order_by(Cpre_Cirugia_Prev.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Cirugia_Prev que coincida con el parametro indicado para id
      """ 
      return Cpre_Cirugia_Prev.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Cirugia_Prev que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Cirugia_Prev.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Coledocolitiasis(dba.Model):
    __tablename__ = "cpre_coledocolitiasis" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Coledocolitiasis.query.order_by(Cpre_Coledocolitiasis.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Coledocolitiasis que coincida con el parametro indicado para id
      """ 
      return Cpre_Coledocolitiasis.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Coledocolitiasis que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Coledocolitiasis.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Complicaciones(dba.Model):
    __tablename__ = "cpre_complicaciones" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Complicaciones.query.order_by(Cpre_Complicaciones.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Complicaciones que coincida con el parametro indicado para id
      """ 
      return Cpre_Complicaciones.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Complicaciones que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Complicaciones.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Dilatacion_Biliar(dba.Model):
    __tablename__ = "cpre_dilatacion_biliar" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Dilatacion_Biliar.query.order_by(Cpre_Dilatacion_Biliar.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Dilatacion_Biliar que coincida con el parametro indicado para id
      """ 
      return Cpre_Dilatacion_Biliar.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Dilatacion_Biliar que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Dilatacion_Biliar.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Diverticulo(dba.Model):
    __tablename__ = "cpre_diverticulo" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Diverticulo.query.order_by(Cpre_Diverticulo.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Diverticulo que coincida con el parametro indicado para id
      """ 
      return Cpre_Diverticulo.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Diverticulo que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Diverticulo.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Eco_Abd(dba.Model):
    __tablename__ = "cpre_eco_abd" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Eco_Abd.query.order_by(Cpre_Eco_Abd.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Eco_Abd que coincida con el parametro indicado para id
      """ 
      return Cpre_Eco_Abd.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Eco_Abd que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Eco_Abd.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Ept(dba.Model):
    __tablename__ = "cpre_ept" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Ept.query.order_by(Cpre_Ept.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Ept que coincida con el parametro indicado para id
      """ 
      return Cpre_Ept.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Ept que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Ept.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Estenosis_Alta(dba.Model):
    __tablename__ = "cpre_estenosis_alta" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Estenosis_Alta.query.order_by(Cpre_Estenosis_Alta.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Estenosis_Alta que coincida con el parametro indicado para id
      """ 
      return Cpre_Estenosis_Alta.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Estenosis_Alta que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Estenosis_Alta.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Estenosis_Baja(dba.Model):
    __tablename__ = "cpre_estenosis_baja" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Estenosis_Baja.query.order_by(Cpre_Estenosis_Baja.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Estenosis_Baja que coincida con el parametro indicado para id
      """ 
      return Cpre_Estenosis_Baja.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Estenosis_Baja que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Estenosis_Baja.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Eus(dba.Model):
    __tablename__ = "cpre_eus" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Eus.query.order_by(Cpre_Eus.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Eus que coincida con el parametro indicado para id
      """ 
      return Cpre_Eus.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Eus que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Eus.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Grado_Asge(dba.Model):
    __tablename__ = "cpre_grado_asge" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Grado_Asge.query.order_by(Cpre_Grado_Asge.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Grado_Asge que coincida con el parametro indicado para id
      """ 
      return Cpre_Grado_Asge.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Grado_Asge que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Grado_Asge.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Grado_Dif(dba.Model):
    __tablename__ = "cpre_grado_dif" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Grado_Dif.query.order_by(Cpre_Grado_Dif.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Grado_Dif que coincida con el parametro indicado para id
      """ 
      return Cpre_Grado_Dif.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Grado_Dif que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Grado_Dif.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Indicacion(dba.Model):
    __tablename__ = "cpre_indicacion" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Indicacion.query.order_by(Cpre_Indicacion.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Indicacion que coincida con el parametro indicado para id
      """ 
      return Cpre_Indicacion.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Indicacion que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Indicacion.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Indicacion_Asge(dba.Model):
    __tablename__ = "cpre_indicacion_asge" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Indicacion_Asge.query.order_by(Cpre_Indicacion_Asge.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Indicacion_Asge que coincida con el parametro indicado para id
      """ 
      return Cpre_Indicacion_Asge.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Indicacion_Asge que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Indicacion_Asge.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Indicacion_Ept(dba.Model):
    __tablename__ = "cpre_indicacion_ept" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Indicacion_Ept.query.order_by(Cpre_Indicacion_Ept.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Indicacion_Ept que coincida con el parametro indicado para id
      """ 
      return Cpre_Indicacion_Ept.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Indicacion_Ept que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Indicacion_Ept.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Litotripsia(dba.Model):
    __tablename__ = "cpre_litotripsia" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Litotripsia.query.order_by(Cpre_Litotripsia.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Litotripsia que coincida con el parametro indicado para id
      """ 
      return Cpre_Litotripsia.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Litotripsia que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Litotripsia.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Lpqvb(dba.Model):
    __tablename__ = "cpre_lpqvb" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Lpqvb.query.order_by(Cpre_Lpqvb.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Lpqvb que coincida con el parametro indicado para id
      """ 
      return Cpre_Lpqvb.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Lpqvb que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Lpqvb.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Miscelaneas(dba.Model):
    __tablename__ = "cpre_miscelaneas" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Miscelaneas.query.order_by(Cpre_Miscelaneas.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Miscelaneas que coincida con el parametro indicado para id
      """ 
      return Cpre_Miscelaneas.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Miscelaneas que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Miscelaneas.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Precorte(dba.Model):
    __tablename__ = "cpre_precorte" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Precorte.query.order_by(Cpre_Precorte.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Precorte que coincida con el parametro indicado para id
      """ 
      return Cpre_Precorte.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Precorte que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Precorte.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Profilaxis_Atb(dba.Model):
    __tablename__ = "cpre_profilaxis_atb" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Profilaxis_Atb.query.order_by(Cpre_Profilaxis_Atb.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Profilaxis_Atb que coincida con el parametro indicado para id
      """ 
      return Cpre_Profilaxis_Atb.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Profilaxis_Atb que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Profilaxis_Atb.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Resolucion_Complica(dba.Model):
    __tablename__ = "cpre_resolucion_complica" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Resolucion_Complica.query.order_by(Cpre_Resolucion_Complica.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Resolucion_Complica que coincida con el parametro indicado para id
      """ 
      return Cpre_Resolucion_Complica.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Resolucion_Complica que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Resolucion_Complica.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Rnm(dba.Model):
    __tablename__ = "cpre_rnm" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Rnm.query.order_by(Cpre_Rnm.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Rnm que coincida con el parametro indicado para id
      """ 
      return Cpre_Rnm.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Rnm que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Rnm.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Stent_Autoexp(dba.Model):
    __tablename__ = "cpre_stent_autoexp" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Stent_Autoexp.query.order_by(Cpre_Stent_Autoexp.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Stent_Autoexp que coincida con el parametro indicado para id
      """ 
      return Cpre_Stent_Autoexp.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Stent_Autoexp que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Stent_Autoexp.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Stent_Plastico(dba.Model):
    __tablename__ = "cpre_stent_plastico" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Stent_Plastico.query.order_by(Cpre_Stent_Plastico.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Stent_Plastico que coincida con el parametro indicado para id
      """ 
      return Cpre_Stent_Plastico.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Stent_Plastico que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Stent_Plastico.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Tac(dba.Model):
    __tablename__ = "cpre_tac" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Tac.query.order_by(Cpre_Tac.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Tac que coincida con el parametro indicado para id
      """ 
      return Cpre_Tac.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Tac que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Tac.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Terap_Pancreas(dba.Model):
    __tablename__ = "cpre_terap_pancreas" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Terap_Pancreas.query.order_by(Cpre_Terap_Pancreas.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Terap_Pancreas que coincida con el parametro indicado para id
      """ 
      return Cpre_Terap_Pancreas.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Terap_Pancreas que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Terap_Pancreas.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Transk(dba.Model):
    __tablename__ = "cpre_transk" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Transk.query.order_by(Cpre_Transk.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Transk que coincida con el parametro indicado para id
      """ 
      return Cpre_Transk.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Transk que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Transk.query.filter_by(descripcion=nombre).one_or_none()


class Cpre_Wirsung(dba.Model):
    __tablename__ = "cpre_wirsung" 
    id = dba.Column(dba.Integer, primary_key=True)
    descripcion = dba.Column(dba.String(100), unique=True, nullable=False)

    def __repr__(self):
      return self.descripcion

    @classmethod
    def all(cls):
      """ Devuelve el total de filas de la tabla 
      """ 
      return Cpre_Wirsung.query.order_by(Cpre_Wirsung.descripcion).all()

    @classmethod
    def find_by_id(cls, id):
      """ 
      devuelve el primer elemento de la tabla Cpre_Wirsung que coincida con el parametro indicado para id
      """ 
      return Cpre_Wirsung.query.filter_by(id=id).one_or_none()

    @classmethod
    def find_by_nombre(cls, nombre):
      """ 
      devuelve el primer elemento de la tabla Cpre_Wirsung que coincida con el parametro indicado para descripcion
      """ 
      return Cpre_Wirsung.query.filter_by(descripcion=nombre).one_or_none()

class Cpre_Cpre_Cirugia_Prev(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Cirugia_Prev
    """ 

    __tablename__ = "cpre_cpre_cirugia_prev" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_cirugia_prev = dba.Column(dba.Integer, dba.ForeignKey('cpre_cirugia_prev.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_cirugia_prev", cascade="all, delete-orphan"))
    cpre_cirugia_prev = relationship("Cpre_Cirugia_Prev", backref=backref("cpre_cpre_cirugia_prev", cascade="all, delete-orphan"))




class Cpre_Cpre_Coledocolitiasis(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Coledocolitiasis
    """ 

    __tablename__ = "cpre_cpre_coledocolitiasis" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_coledocolitiasis = dba.Column(dba.Integer, dba.ForeignKey('cpre_coledocolitiasis.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_coledocolitiasis", cascade="all, delete-orphan"))
    cpre_coledocolitiasis = relationship("Cpre_Coledocolitiasis", backref=backref("cpre_cpre_coledocolitiasis", cascade="all, delete-orphan"))




class Cpre_Cpre_Complicaciones(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Complicaciones
    """ 

    __tablename__ = "cpre_cpre_complicaciones" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_complicaciones = dba.Column(dba.Integer, dba.ForeignKey('cpre_complicaciones.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_complicaciones", cascade="all, delete-orphan"))
    cpre_complicaciones = relationship("Cpre_Complicaciones", backref=backref("cpre_cpre_complicaciones", cascade="all, delete-orphan"))




class Cpre_Cpre_Diverticulo(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Diverticulo
    """ 

    __tablename__ = "cpre_cpre_diverticulo" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_diverticulo = dba.Column(dba.Integer, dba.ForeignKey('cpre_diverticulo.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_diverticulo", cascade="all, delete-orphan"))
    cpre_diverticulo = relationship("Cpre_Diverticulo", backref=backref("cpre_cpre_diverticulo", cascade="all, delete-orphan"))




class Cpre_Cpre_Eco_Abd(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Eco_Abd
    """ 

    __tablename__ = "cpre_cpre_eco_abd" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_eco_abd = dba.Column(dba.Integer, dba.ForeignKey('cpre_eco_abd.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_eco_abd", cascade="all, delete-orphan"))
    cpre_eco_abd = relationship("Cpre_Eco_Abd", backref=backref("cpre_cpre_eco_abd", cascade="all, delete-orphan"))




class Cpre_Cpre_Estenosis_Alta(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Estenosis_Alta
    """ 

    __tablename__ = "cpre_cpre_estenosis_alta" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_estenosis_alta = dba.Column(dba.Integer, dba.ForeignKey('cpre_estenosis_alta.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_estenosis_alta", cascade="all, delete-orphan"))
    cpre_estenosis_alta = relationship("Cpre_Estenosis_Alta", backref=backref("cpre_cpre_estenosis_alta", cascade="all, delete-orphan"))




class Cpre_Cpre_Estenosis_Baja(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Estenosis_Baja
    """ 

    __tablename__ = "cpre_cpre_estenosis_baja" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_estenosis_baja = dba.Column(dba.Integer, dba.ForeignKey('cpre_estenosis_baja.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_estenosis_baja", cascade="all, delete-orphan"))
    cpre_estenosis_baja = relationship("Cpre_Estenosis_Baja", backref=backref("cpre_cpre_estenosis_baja", cascade="all, delete-orphan"))




class Cpre_Cpre_Eus(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Eus
    """ 

    __tablename__ = "cpre_cpre_eus" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_eus = dba.Column(dba.Integer, dba.ForeignKey('cpre_eus.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_eus", cascade="all, delete-orphan"))
    cpre_eus = relationship("Cpre_Eus", backref=backref("cpre_cpre_eus", cascade="all, delete-orphan"))




class Cpre_Cpre_Indicacion(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Indicacion
    """ 

    __tablename__ = "cpre_cpre_indicacion" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_indicacion = dba.Column(dba.Integer, dba.ForeignKey('cpre_indicacion.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_indicacion", cascade="all, delete-orphan"))
    cpre_indicacion = relationship("Cpre_Indicacion", backref=backref("cpre_cpre_indicacion", cascade="all, delete-orphan"))




class Cpre_Cpre_Indicacion_Asge(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Indicacion_Asge
    """ 

    __tablename__ = "cpre_cpre_indicacion_asge" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_indicacion_asge = dba.Column(dba.Integer, dba.ForeignKey('cpre_indicacion_asge.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_indicacion_asge", cascade="all, delete-orphan"))
    cpre_indicacion_asge = relationship("Cpre_Indicacion_Asge", backref=backref("cpre_cpre_indicacion_asge", cascade="all, delete-orphan"))




class Cpre_Cpre_Indicacion_Ept(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Indicacion_Ept
    """ 

    __tablename__ = "cpre_cpre_indicacion_ept" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_indicacion_ept = dba.Column(dba.Integer, dba.ForeignKey('cpre_indicacion_ept.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_indicacion_ept", cascade="all, delete-orphan"))
    cpre_indicacion_ept = relationship("Cpre_Indicacion_Ept", backref=backref("cpre_cpre_indicacion_ept", cascade="all, delete-orphan"))




class Cpre_Cpre_Lpqvb(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Lpqvb
    """ 

    __tablename__ = "cpre_cpre_lpqvb" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_lpqvb = dba.Column(dba.Integer, dba.ForeignKey('cpre_lpqvb.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_lpqvb", cascade="all, delete-orphan"))
    cpre_lpqvb = relationship("Cpre_Lpqvb", backref=backref("cpre_cpre_lpqvb", cascade="all, delete-orphan"))




class Cpre_Cpre_Miscelaneas(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Miscelaneas
    """ 

    __tablename__ = "cpre_cpre_miscelaneas" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_miscelaneas = dba.Column(dba.Integer, dba.ForeignKey('cpre_miscelaneas.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_miscelaneas", cascade="all, delete-orphan"))
    cpre_miscelaneas = relationship("Cpre_Miscelaneas", backref=backref("cpre_cpre_miscelaneas", cascade="all, delete-orphan"))




class Cpre_Cpre_Profilaxis_Atb(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Profilaxis_Atb
    """ 

    __tablename__ = "cpre_cpre_profilaxis_atb" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_profilaxis_atb = dba.Column(dba.Integer, dba.ForeignKey('cpre_profilaxis_atb.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_profilaxis_atb", cascade="all, delete-orphan"))
    cpre_profilaxis_atb = relationship("Cpre_Profilaxis_Atb", backref=backref("cpre_cpre_profilaxis_atb", cascade="all, delete-orphan"))




class Cpre_Cpre_Resolucion_Complica(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Resolucion_Complica
    """ 

    __tablename__ = "cpre_cpre_resolucion_complica" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_resolucion_complica = dba.Column(dba.Integer, dba.ForeignKey('cpre_resolucion_complica.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_resolucion_complica", cascade="all, delete-orphan"))
    cpre_resolucion_complica = relationship("Cpre_Resolucion_Complica", backref=backref("cpre_cpre_resolucion_complica", cascade="all, delete-orphan"))




class Cpre_Cpre_Rnm(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Rnm
    """ 

    __tablename__ = "cpre_cpre_rnm" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_rnm = dba.Column(dba.Integer, dba.ForeignKey('cpre_rnm.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_rnm", cascade="all, delete-orphan"))
    cpre_rnm = relationship("Cpre_Rnm", backref=backref("cpre_cpre_rnm", cascade="all, delete-orphan"))




class Cpre_Cpre_Tac(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Tac
    """ 

    __tablename__ = "cpre_cpre_tac" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_tac = dba.Column(dba.Integer, dba.ForeignKey('cpre_tac.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_tac", cascade="all, delete-orphan"))
    cpre_tac = relationship("Cpre_Tac", backref=backref("cpre_cpre_tac", cascade="all, delete-orphan"))




class Cpre_Cpre_Terap_Pancreas(dba.Model):
    """ 
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Terap_Pancreas
    """ 

    __tablename__ = "cpre_cpre_terap_pancreas" 

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_terap_pancreas = dba.Column(dba.Integer, dba.ForeignKey('cpre_terap_pancreas.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_terap_pancreas", cascade="all, delete-orphan"))
    cpre_terap_pancreas = relationship("Cpre_Terap_Pancreas", backref=backref("cpre_cpre_terap_pancreas", cascade="all, delete-orphan"))


class Cpre_Cpre_Transk(dba.Model):
    """
    Clase que modela la relacion muchos a muchos entre Cpre y Cpre_Transk
    """

    __tablename__ = "cpre_cpre_transk"

    id_CPRE = dba.Column(dba.Integer, dba.ForeignKey('cpre.id'), primary_key=True)
    id_CPRE_transk = dba.Column(dba.Integer, dba.ForeignKey('cpre_transk.id'), primary_key=True)

    cpre = relationship("Cpre", backref=backref("cpre_cpre_transk", cascade="all, delete-orphan"))
    cpre_transk = relationship("Cpre_Transk", backref=backref("cpre_cpre_transk", cascade="all, delete-orphan"))
