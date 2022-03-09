ALTER TABLE VEDA ADD id_historia INT(10) NOT NULL;
ALTER TABLE VEDA ADD CONSTRAINT VEDA_historia_fk FOREIGN KEY (id_historia) REFERENCES historia (id);

CREATE TABLE IF NOT EXISTS Hospital (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO Hospital (descripcion) VALUES
('Avellaneda'),
('Adrogué'),
('Baradero'),
('Berazategui'),
('Casanova'),
('Escobar'),
('Ezeiza'),
('G.Catan'),
('Hec Amb'),
('Hec Int'),
('Lanús'),
('Lomas De Zamora'),
('Mdp'),
('Posadas'),
('Quilmes'),
('R. Calzada'),
('Ranchos'),
('Ranchos'),
('Romero'),
('Rossi'),
('San Antonio De Areco'),
('San Martin'),
('San Martín'),
('San Miguel Del Monte'),
('Udaondo'),
('Varela'),
('Wilde'),
('Otros')
;

CREATE TABLE IF NOT EXISTS CPRE_indicacion_ASGE (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_indicacion_ASGE (descripcion) VALUES
('Ictericia c/sospecha obst. Biliar'),
('pac. Anicterico + datos lab o imagen enf biliopanc.'),
('sospecha CA páncreas con estudios normales'),
('pancreatitis causa desconocida'),
('eval. Preop. En PC y/o PS'),
('manometría oddi'),
('colocación stent en estenosis/distulas/fugas o litos gigantes'),
('dilatación de estenosis'),
('dilatación papilar'),
('colocación DNB'),
('drenaje Pseudoquiste'),
('Bx tejido biliar o pancreat'),
('ampuelctomia'),
('terapéutica enf. Biliopancreatica'),
('para facilitar colangioscopia y/o pancreatosc.')
;

CREATE TABLE IF NOT EXISTS CPRE_indicacion (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_indicacion (descripcion) VALUES
('ictericia'),
('colangitis'),
('coledocolitiasis'),
('prurito'),
('sme. coled.'),
('pa'),
('pat.pancreat.'),
('recambio stent'),
('pancreatitis recurrente'),
('pseudoquiste'),
('lpqvb'),
('estenosis biliar benigna'),
('otros')
;


CREATE TABLE IF NOT EXISTS CPRE_cirugia_prev (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_cirugia_prev (descripcion) VALUES
('Cole lap'),
('cole conv.'),
('BII'),
('Der. B-d.'),
('banda gástrica'),
('otros'),
('Post-trasplante')
;

CREATE TABLE IF NOT EXISTS CPRE_ECO_ABD (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_ECO_ABD (descripcion) VALUES
('normal'),
('VBIH dilatada'),
('VBEH dilatada'),
('coledocolitiasis'),
('VB dilatada'),
('otros')
;

CREATE TABLE IF NOT EXISTS CPRE_TAC (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_TAC (descripcion) VALUES
('lesiones focales hepáticas'),
('VBIH dilatada'),
('VBEH dilatada'),
('masa páncreas'),
('masa vesícula'),
('adenopatías'),
('VB dilatada'),
('pseudoquiste'),
('quistes'),
('colecciones'),
('ampuloma')
;

CREATE TABLE IF NOT EXISTS CPRE_RNM (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_RNM (descripcion) VALUES
('coledocolitiasis'),
('quiste de colédoco'),
('masa páncreas'),
('masa vesícula'),
('estenosis biliar'),
('ampuloma'),
('vbih dilatada'),
('vbeh dilatada'),
('vb dilatada')
;

CREATE TABLE IF NOT EXISTS CPRE_EUS (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_EUS (descripcion) VALUES
('coledocolitiasis'),
('vb dilatada'),
('tumor ampular'),
('tumor pancreas'),
('colangio CA'),
('Mirizzi'),
('normal'),
('otras')
;

CREATE TABLE IF NOT EXISTS CPRE_TRANSK (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_TRANSK (descripcion) VALUES
('fuga'),
('estenosis'),
('lito residual'),
('estenosis más fuga')
;

CREATE TABLE IF NOT EXISTS CPRE_grado_ASGE (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_grado_ASGE (descripcion) VALUES
('alto'),
('medio'),
('bajo')
;

CREATE TABLE IF NOT EXISTS CPRE_grado_dif (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_grado_dif (descripcion) VALUES
('1'),
('2'),
('3')
;

CREATE TABLE IF NOT EXISTS CPRE_profilaxis_ATB (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_profilaxis_ATB (descripcion) VALUES
('obstr biliar maligna'),
('obstr biliar benigna'),
('inmunosupresión'),
('colangitis'),
('pseudoquiste p.'),
('colelitiasis'),
('CEP'),
('otras'),
('NO')
;

CREATE TABLE IF NOT EXISTS CPRE_COLEDOCOLITIASIS (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_COLEDOCOLITIASIS (descripcion) VALUES
('no complicada'),
('gigante'),
('múltiple'),
('con estenosis'),
('impactada'),
('B.II'),
('intrahepática'),
('G+M'),
('E+G'),
('M+E'),
('G+I'),
('Intra+E'),
('M+I')
;

CREATE TABLE IF NOT EXISTS CPRE_diverticulo (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_diverticulo (descripcion) VALUES
('yuxta'),
('intra')
;

CREATE TABLE IF NOT EXISTS CPRE_LPQVB (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_LPQVB (descripcion) VALUES
('estenosis'),
('fuga alto débito'),
('fuga bajo débito'),
('estenosis más fuga')
;


CREATE TABLE IF NOT EXISTS CPRE_ESTENOSIS_BAJA (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_ESTENOSIS_BAJA (descripcion) VALUES
('ampuloma'),
('colangiocarcinoma'),
('ca vesicula'),
('ca páncreas'),
('compresión gang.'),
('MIRIZZI'),
('colédoco medio'),
('colédoco inf.')
;

CREATE TABLE IF NOT EXISTS CPRE_ESTENOSIS_ALTA (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_ESTENOSIS_ALTA (descripcion) VALUES
('B.I'),
('B.II'),
('B.III'),
('B.IV'),
('ca vesicula'),
('compresión gang.'),
('MIRIZZI'),
('colédoco sup.')
;

CREATE TABLE IF NOT EXISTS CPRE_Miscelaneas (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_Miscelaneas (descripcion) VALUES
('parasitario'),
('cuerpo extraño'),
('disfunción Oddi'),
('otros')
;

CREATE TABLE IF NOT EXISTS CPRE_Terap_Pancreas (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_Terap_Pancreas (descripcion) VALUES
('wirsungtomia'),
('dilat. Estenosis'),
('litos'),
('papila menor'),
('pseudoquistes'),
('stent'),
('ampulectomia'),
('fuga'),
('fístula')
;

CREATE TABLE IF NOT EXISTS CPRE_EPT (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_EPT (descripcion) VALUES
('si'),
('no'),
('previa')
;

CREATE TABLE IF NOT EXISTS CPRE_Indicacion_EPT (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_Indicacion_EPT (descripcion) VALUES
('Coledocolitiasis'),
('estenosis papilar'),
('DEO'),
('colocación stent biliar'),
('dilatación biliar'),
('Sme sumidero'),
('coledococele'),
('ampuloma'),
('acceso pancreático'),
('OTRAS')
;

CREATE TABLE IF NOT EXISTS CPRE_WIRSUNG (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_WIRSUNG (descripcion) VALUES
('inyección'),
('> 3 canulaciones'),
('ept páncreas')
;

CREATE TABLE IF NOT EXISTS CPRE_PRECORTE (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_PRECORTE (descripcion) VALUES
('standard'),
('infundibulotomia'),
('septumtomia'),
('otros'),
('previo')
;

CREATE TABLE IF NOT EXISTS CPRE_Dilatacion_biliar (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_Dilatacion_biliar (descripcion) VALUES
('soehendra 7f'),
('soehendra 10f'),
('balón 8mm'),
('balón 10mm'),
('balón 12mm'),
('balón 15mm'),
('balón 18mm'),
('balón 20mm')
;

CREATE TABLE IF NOT EXISTS CPRE_Litotripsia (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_Litotripsia (descripcion) VALUES
('olympus'),
('boston'),
('cook'),
('soehendra'),
('otras')
;

CREATE TABLE IF NOT EXISTS CPRE_stent_plastico (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_stent_plastico (descripcion) VALUES
('7F'),
('10F'),
('drenaje N/B'),
('5F')
;

CREATE TABLE IF NOT EXISTS CPRE_stent_autoexp (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_stent_autoexp (descripcion) VALUES
('c/cobertura'),
('s/cobertura'),
('Biodegradable')
;

CREATE TABLE IF NOT EXISTS CPRE_AMILASEMIA_2HS (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_AMILASEMIA_2HS (descripcion) VALUES
('< 1,5 vn'),
('>3 vn'),
('> 5 vn')
;

CREATE TABLE IF NOT EXISTS CPRE_Complicaciones (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_Complicaciones (descripcion) VALUES
('pancreatitis'),
('perforación'),
('colangitis'),
('hemorragia'),
('colecistitis'),
('anestesia'),
('migración stent'),
('hematoma hepático'),
('hematoma esplénico'),
('hematoma +migración')
;

CREATE TABLE IF NOT EXISTS CPRE_resolucion_complica (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO CPRE_resolucion_complica (descripcion) VALUES
('medica'),
('endoscópica'),
('Cx'),
('obito'),
('endosc+qx')
;


CREATE TABLE IF NOT EXISTS CPRE (
    id int(10) NOT NULL AUTO_INCREMENT,
    ASA int(1) NULL,
    ambulatorio boolean NOT NULL,
    cpre_previa boolean NOT NULL,
    id_hospital_derivacion int(10) NULL,
    BILIRRUBINA varchar(2000) NULL,
    FAL varchar(2000) NULL,
    TGP varchar(2000) NULL,
    TGO varchar(2000) NULL,
    AMILASA varchar(2000) NULL,
    GGT varchar(2000) NULL,
    GB varchar(2000) NULL,
    id_operador INT(10),
    FR_DE_PA_SOD boolean NOT NULL,
    FR_DE_PA_AUSENCIA_PC boolean NOT NULL,
    FR_DE_PA_ANTEC_PA boolean NOT NULL,
    CPRE_normal boolean NOT NULL,
    id_CPRE_EPT int(10) NULL,
    ESFINTEROPLASTIA boolean NOT NULL,
    id_CPRE_WIRSUNG int(10) NULL,
    id_CPRE_PRECORTE int(10) NULL,
    id_CPRE_Dilatacion_biliar int(10) NULL,
    id_CPRE_Litotripsia int(10) NULL,
    id_CPRE_stent_plastico int(10) NULL,
    id_CPRE_stent_autoexp int(10) NULL,
    stent_duodenal boolean NOT NULL,
    RX_dosis varchar(2000) NULL,
    DPA varchar(2000) NULL,
    RX_tiempo varchar(2000) NULL,
    nro_sesiones INT(1) NULL,
    resolucion_completa boolean NOT NULL,
    id_CPRE_AMILASEMIA_2HS int(10) NULL,
    canulacion boolean NOT NULL,
    biopsias boolean NOT NULL,
    citologia varchar(2000) NULL,
    fracaso boolean NOT NULL,
    comentarios varchar(2000) NULL,
    embarazo boolean NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT CPRE_hospital_fk FOREIGN KEY (id_hospital_derivacion) REFERENCES hospital (id),
    CONSTRAINT CPRE_CPRE_EPT_fk FOREIGN KEY (id_CPRE_EPT) REFERENCES CPRE_EPT (id),
    CONSTRAINT CPRE_CPRE_WIRSUNG_fk FOREIGN KEY (id_CPRE_WIRSUNG) REFERENCES CPRE_WIRSUNG (id),
    CONSTRAINT CPRE_CPRE_PRECORTE_fk FOREIGN KEY (id_CPRE_PRECORTE) REFERENCES CPRE_PRECORTE (id),
    CONSTRAINT CPRE_CPRE_Dilatacion_biliar_fk FOREIGN KEY (id_CPRE_Dilatacion_biliar) REFERENCES CPRE_Dilatacion_biliar (id),
    CONSTRAINT CPRE_CPRE_Litotripsia_fk FOREIGN KEY (id_CPRE_Litotripsia) REFERENCES CPRE_Litotripsia (id),
    CONSTRAINT CPRE_CPRE_stent_plastico_fk FOREIGN KEY (id_CPRE_stent_plastico) REFERENCES CPRE_stent_plastico (id),
    CONSTRAINT CPRE_CPRE_stent_autoexp_fk FOREIGN KEY (id_CPRE_stent_autoexp) REFERENCES CPRE_stent_autoexp (id),
    CONSTRAINT CPRE_CPRE_AMILASEMIA_2HS_fk FOREIGN KEY (id_CPRE_AMILASEMIA_2HS) REFERENCES CPRE_AMILASEMIA_2HS (id)
);

CREATE TABLE IF NOT EXISTS CPRE_CPRE_indicacion_ASGE (
  id_CPRE int(10),
  id_CPRE_indicacion_ASGE int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_indicacion_ASGE),
  CONSTRAINT CPRE_CPRE_indicacion_ASGE_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_indicacion_ASGE_fk_2 FOREIGN KEY (id_CPRE_indicacion_ASGE) REFERENCES CPRE_indicacion_ASGE (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_indicacion (
  id_CPRE int(10),
  id_CPRE_indicacion int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_indicacion),
  CONSTRAINT CPRE_CPRE_indicacion_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_indicacion_fk_2 FOREIGN KEY (id_CPRE_indicacion) REFERENCES CPRE_indicacion (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_cirugia_prev (
  id_CPRE int(10),
  id_CPRE_cirugia_prev int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_cirugia_prev),
  CONSTRAINT CPRE_CPRE_cirugia_prev_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_cirugia_prev_fk_2 FOREIGN KEY (id_CPRE_cirugia_prev) REFERENCES CPRE_cirugia_prev (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_ECO_ABD (
  id_CPRE int(10),
  id_CPRE_ECO_ABD int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_ECO_ABD),
  CONSTRAINT CPRE_CPRE_ECO_ABD_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_ECO_ABD_fk_2 FOREIGN KEY (id_CPRE_ECO_ABD) REFERENCES CPRE_ECO_ABD (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_TAC (
  id_CPRE int(10),
  id_CPRE_TAC int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_TAC),
  CONSTRAINT CPRE_CPRE_TAC_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_TAC_fk_2 FOREIGN KEY (id_CPRE_TAC) REFERENCES CPRE_TAC (id) );


CREATE TABLE IF NOT EXISTS CPRE_CPRE_RNM (
  id_CPRE int(10),
  id_CPRE_RNM int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_RNM),
  CONSTRAINT CPRE_CPRE_RNM_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_RNM_fk_2 FOREIGN KEY (id_CPRE_RNM) REFERENCES CPRE_RNM (id) );


CREATE TABLE IF NOT EXISTS CPRE_CPRE_EUS (
  id_CPRE int(10),
  id_CPRE_EUS int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_EUS),
  CONSTRAINT CPRE_CPRE_EUS_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_EUS_fk_2 FOREIGN KEY (id_CPRE_EUS) REFERENCES CPRE_EUS (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_TRANSK (
  id_CPRE int(10),
  id_CPRE_TRANSK int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_TRANSK),
  CONSTRAINT CPRE_CPRE_TRANSK_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_TRANSK_fk_2 FOREIGN KEY (id_CPRE_TRANSK) REFERENCES CPRE_TRANSK (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_grado_ASGE (
  id_CPRE int(10),
  id_CPRE_grado_ASGE int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_grado_ASGE),
  CONSTRAINT CPRE_CPRE_grado_ASGE_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_grado_ASGE_fk_2 FOREIGN KEY (id_CPRE_grado_ASGE) REFERENCES CPRE_grado_ASGE (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_grado_dif (
  id_CPRE int(10),
  id_CPRE_grado_dif int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_grado_dif),
  CONSTRAINT CPRE_CPRE_grado_dif_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_grado_dif_fk_2 FOREIGN KEY (id_CPRE_grado_dif) REFERENCES CPRE_grado_dif (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_profilaxis_ATB (
  id_CPRE int(10),
  id_CPRE_profilaxis_ATB int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_profilaxis_ATB),
  CONSTRAINT CPRE_CPRE_profilaxis_ATB_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_profilaxis_ATB_fk_2 FOREIGN KEY (id_CPRE_profilaxis_ATB) REFERENCES CPRE_profilaxis_ATB (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_COLEDOCOLITIASIS (
  id_CPRE int(10),
  id_CPRE_COLEDOCOLITIASIS int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_COLEDOCOLITIASIS),
  CONSTRAINT CPRE_CPRE_COLEDOCOLITIASIS_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_COLEDOCOLITIASIS_fk_2 FOREIGN KEY (id_CPRE_COLEDOCOLITIASIS) REFERENCES CPRE_COLEDOCOLITIASIS (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_diverticulo (
  id_CPRE int(10),
  id_CPRE_diverticulo int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_diverticulo),
  CONSTRAINT CPRE_CPRE_diverticulo_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_diverticulo_fk_2 FOREIGN KEY (id_CPRE_diverticulo) REFERENCES CPRE_diverticulo (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_LPQVB (
  id_CPRE int(10),
  id_CPRE_LPQVB int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_LPQVB),
  CONSTRAINT CPRE_CPRE_LPQVB_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_LPQVB_fk_2 FOREIGN KEY (id_CPRE_LPQVB) REFERENCES CPRE_LPQVB (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_ESTENOSIS_BAJA (
  id_CPRE int(10),
  id_CPRE_ESTENOSIS_BAJA int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_ESTENOSIS_BAJA),
  CONSTRAINT CPRE_CPRE_ESTENOSIS_BAJA_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_ESTENOSIS_BAJA_fk_2 FOREIGN KEY (id_CPRE_ESTENOSIS_BAJA) REFERENCES CPRE_ESTENOSIS_BAJA (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_ESTENOSIS_ALTA (
  id_CPRE int(10),
  id_CPRE_ESTENOSIS_ALTA int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_ESTENOSIS_ALTA),
  CONSTRAINT CPRE_CPRE_ESTENOSIS_ALTA_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_ESTENOSIS_ALTA_fk_2 FOREIGN KEY (id_CPRE_ESTENOSIS_ALTA) REFERENCES CPRE_ESTENOSIS_ALTA (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_Miscelaneas (
  id_CPRE int(10),
  id_CPRE_Miscelaneas int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_Miscelaneas),
  CONSTRAINT CPRE_CPRE_Miscelaneas_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_Miscelaneas_fk_2 FOREIGN KEY (id_CPRE_Miscelaneas) REFERENCES CPRE_Miscelaneas (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_Terap_Pancreas (
  id_CPRE int(10),
  id_CPRE_Terap_Pancreas int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_Terap_Pancreas),
  CONSTRAINT CPRE_CPRE_Terap_Pancreas_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_Terap_Pancreas_fk_2 FOREIGN KEY (id_CPRE_Terap_Pancreas) REFERENCES CPRE_Terap_Pancreas (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_Indicacion_EPT (
  id_CPRE int(10),
  id_CPRE_Indicacion_EPT int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_Indicacion_EPT),
  CONSTRAINT CPRE_CPRE_Indicacion_EPT_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_Indicacion_EPT_fk_2 FOREIGN KEY (id_CPRE_Indicacion_EPT) REFERENCES CPRE_Indicacion_EPT (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_Complicaciones (
  id_CPRE int(10),
  id_CPRE_Complicaciones int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_Complicaciones),
  CONSTRAINT CPRE_CPRE_Complicaciones_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_Complicaciones_fk_2 FOREIGN KEY (id_CPRE_Complicaciones) REFERENCES CPRE_Complicaciones (id) );

CREATE TABLE IF NOT EXISTS CPRE_CPRE_resolucion_complica (
  id_CPRE int(10),
  id_CPRE_resolucion_complica int(10),
  PRIMARY KEY (id_CPRE, id_CPRE_resolucion_complica),
  CONSTRAINT CPRE_CPRE_resolucion_complica_fk_1 FOREIGN KEY (id_CPRE) REFERENCES CPRE (id),
  CONSTRAINT CPRE_CPRE_resolucion_complica_fk_2 FOREIGN KEY (id_CPRE_resolucion_complica) REFERENCES CPRE_resolucion_complica (id) );

ALTER TABLE CPRE ADD id_historia INT(10) NOT NULL;
ALTER TABLE CPRE ADD CONSTRAINT CPRE_historia_fk FOREIGN KEY (id_historia) REFERENCES historia (id);