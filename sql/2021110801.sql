CREATE TABLE IF NOT EXISTS Sexo (
  id INT(1) NOT NULL,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );

INSERT INTO Sexo(id, descripcion) VALUES
(1, 'Femenino'),
(2, 'Masculino'),
(3, 'Otros');

CREATE TABLE IF NOT EXISTS Historia (
  id int(10) NOT NULL AUTO_INCREMENT,
  nombre varchar(300) NOT NULL,
  dni varchar(10) NOT NULL,
  nacimiento date,
  id_sexo INT(10),
  activa boolean DEFAULT true,
  PRIMARY KEY (id),
  CONSTRAINT historia_sexo_fk_1 FOREIGN KEY (id_sexo) REFERENCES Sexo (id) );

CREATE TABLE IF NOT EXISTS VCC_preparacion (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );

INSERT INTO VCC_preparacion(descripcion) VALUES
('fosfatos'),
('polietilenglicol'),
('sulfatos'),
('PEG + bisacodilo'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_motivo (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );

INSERT INTO VCC_motivo(descripcion) VALUES
('screening'),
('vigilancia de pólipos'),
('vigilancia de CCR'),
('TSOMF +'),
('Anemia'),
('Proctorragia'),
('Dolor abdominal'),
('Cambio de hábito evacuatorio'),
('SRG - diarrea crónica'),
('enfermedad inflamatoria intestinal'),
('polipectomía programada'),
('búsqueda de primario'),
('reconexión'),
('estenosis colónica '),
('alteración por imágenes '),
('colocación de stent'),
('suboclusivo'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_incompleta_hasta (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );

INSERT INTO VCC_incompleta_hasta(descripcion) VALUES
('sigmoides'),
('esplénico'),
('hepático'),
('derecho'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_incompleta_motivo (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_incompleta_motivo(descripcion) VALUES
('mala preparación'),
('asa fija'),
('estenosis'),
('dolico-mega'),
('anestésicas'),
('estado del paciente'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_hallazgos (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );

INSERT INTO VCC_hallazgos(descripcion) VALUES
('normal'),
('pólipo'),
('divertículos'),
('LST'),
('lesión orgánica'),
('angioectasias'),
('colitis segmentaria'),
('erosiones'),
('pérdida del patrón vascular'),
('úlceras'),
('lesión submucosa'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_terapeutica (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL, 
  PRIMARY KEY (id) );

INSERT INTO VCC_terapeutica(descripcion) VALUES
('Polipectomía'),
('Mucosectomía'),
('Electrofulguración'),
('Dilatación'),
('Colocación de Stent'),
('Marcación con tinta china'),
('Otros')
;

CREATE TABLE IF NOT EXISTS VCC_lesion_sospechosa (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_lesion_sospechosa(descripcion) VALUES
('Si, proximal al esplénico'),
('Si, Distal'),
('No'),
('Otros')
;

CREATE TABLE IF NOT EXISTS VCC_polipos_cant (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_polipos_cant(descripcion) VALUES
('1'),
('2 a 9'),
('10 o más')
;

CREATE TABLE IF NOT EXISTS VCC_polipectomía_tam (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_polipectomía_tam(descripcion) VALUES
('<5mm'),
('e/ 5 y 10 mm'),
('>10mm'),
('>20mm')
;

CREATE TABLE IF NOT EXISTS VCC_polipectomía_material (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id));
INSERT INTO VCC_polipectomía_material (descripcion) VALUES
('pinza de biopsia'),
('ansa fría'),
('ansa caliente'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_polipectomía_tecnica (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_polipectomía_tecnica (descripcion) VALUES
('lifting'),
('marcación de tinta china')
;

CREATE TABLE IF NOT EXISTS VCC_polipectomía_paris (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_polipectomía_paris (descripcion) VALUES
('paris 0-ls'),
('paris 0-lsp'),
('paris 0-lp'),
('paris 0-lla'),
('paris 0-llb'),
('paris 0-llc'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_de_guardia (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_de_guardia (descripcion) VALUES
('hematoquecia'),
('melena'),
('vólvulo intestinal'),
('extracción de cuerpo extraño'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_Complicaciones (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_Complicaciones (descripcion) VALUES
('perforación'),
('sangrado'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_Biopsias (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_Biopsias (descripcion) VALUES
('dirigida'),
('sectorizada'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_tiempo_ingreso (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_tiempo_ingreso (descripcion) VALUES
('< 10 min'),
('e/10 y 20 min'),
('>20 min')
;

CREATE TABLE IF NOT EXISTS VCC_tiempo_retirada (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_tiempo_retirada (descripcion) VALUES
('<6min'),
('>6min')
;



CREATE TABLE IF NOT EXISTS VCC (
  id int(10) NOT NULL AUTO_INCREMENT,
  id_historia int(10),
  fecha date,
  id_operador INT(10),
  id_vcc_preparacion int(10),
  boston_izq int(10) NULL,
  boston_trasv int(10) NULL,
  boston_der int(10) NULL,
  id_VCC_incompleta_hasta int(10),
  id_VCC_incompleta_motivo int(10),
  id_VCC_lesion_sospechosa int(10),
  id_VCC_polipos_cant int(10),
  id_VCC_polipectomía_tam int(10),
  id_VCC_polipectomía_material int(10),
  id_VCC_polipectomía_tecnica int(10),
  id_VCC_polipectomía_paris int(10),
  ileoscopia boolean,
  id_VCC_de_guardia int(10),
  id_VCC_tiempo_ingreso int(10),
  id_VCC_tiempo_retirada int(10),
  comentarios varchar(2000) NOT NULL,
  PRIMARY KEY (id),
  CONSTRAINT VCC_VCC_preparacion_fk_1 FOREIGN KEY (id_vcc_preparacion) REFERENCES VCC_preparacion (id),
  CONSTRAINT VCC_VCC_preparacion_fk_2 FOREIGN KEY (id_VCC_incompleta_hasta) REFERENCES VCC_incompleta_hasta (id),
  CONSTRAINT VCC_VCC_preparacion_fk_3 FOREIGN KEY (id_VCC_incompleta_motivo) REFERENCES VCC_incompleta_motivo (id),
  CONSTRAINT VCC_VCC_preparacion_fk_4 FOREIGN KEY (id_VCC_lesion_sospechosa) REFERENCES VCC_lesion_sospechosa (id),
  CONSTRAINT VCC_VCC_preparacion_fk_5 FOREIGN KEY (id_VCC_polipos_cant) REFERENCES VCC_polipos_cant (id),
  CONSTRAINT VCC_VCC_preparacion_fk_6 FOREIGN KEY (id_VCC_polipectomía_tam) REFERENCES VCC_polipectomía_tam (id),
  CONSTRAINT VCC_VCC_preparacion_fk_7 FOREIGN KEY (id_VCC_polipectomía_material) REFERENCES VCC_polipectomía_material (id),
  CONSTRAINT VCC_VCC_preparacion_fk_8 FOREIGN KEY (id_VCC_polipectomía_tecnica) REFERENCES VCC_polipectomía_tecnica (id),
  CONSTRAINT VCC_VCC_preparacion_fk_9 FOREIGN KEY (id_VCC_polipectomía_paris) REFERENCES VCC_polipectomía_paris (id),
  CONSTRAINT VCC_VCC_preparacion_fk_10 FOREIGN KEY (id_VCC_de_guardia) REFERENCES VCC_de_guardia (id),
  CONSTRAINT VCC_VCC_preparacion_fk_11 FOREIGN KEY (id_VCC_tiempo_ingreso) REFERENCES VCC_tiempo_ingreso (id),
  CONSTRAINT VCC_VCC_preparacion_fk_12 FOREIGN KEY (id_VCC_tiempo_retirada) REFERENCES VCC_tiempo_retirada (id)
  );

CREATE TABLE IF NOT EXISTS VCC_VCC_motivo (
  id_VCC int(10),
  id_VCC_motivo int(10),
  PRIMARY KEY (id_VCC, id_VCC_motivo),
  CONSTRAINT VCC_VCC_motivo_fk_1 FOREIGN KEY (id_VCC) REFERENCES VCC (id),
  CONSTRAINT VCC_VCC_motivo_fk_2 FOREIGN KEY (id_VCC_motivo) REFERENCES VCC_motivo (id) );

CREATE TABLE IF NOT EXISTS VCC_VCC_hallazgos (
  id_VCC int(10),
  id_VCC_hallazgos int(10),
  PRIMARY KEY (id_VCC, id_VCC_hallazgos),
  CONSTRAINT VCC_VCC_hallazgos_fk_1 FOREIGN KEY (id_VCC) REFERENCES VCC (id),
  CONSTRAINT VCC_VCC_hallazgos_fk_2 FOREIGN KEY (id_VCC_hallazgos) REFERENCES VCC_hallazgos (id) );

CREATE TABLE IF NOT EXISTS VCC_VCC_terapeutica (
  id_VCC int(10),
  id_VCC_terapeutica int(10),
  PRIMARY KEY (id_VCC, id_VCC_terapeutica),
  CONSTRAINT VCC_VCC_terapeutica_fk_1 FOREIGN KEY (id_VCC) REFERENCES VCC (id),
  CONSTRAINT VCC_VCC_terapeutica_fk_2 FOREIGN KEY (id_VCC_terapeutica) REFERENCES VCC_terapeutica (id) );
  
CREATE TABLE IF NOT EXISTS VCC_VCC_complicaciones (
  id_VCC int(10),
  id_VCC_complicaciones int(10),
  PRIMARY KEY (id_VCC, id_VCC_complicaciones),
  CONSTRAINT VCC_VCC_complicaciones_fk_1 FOREIGN KEY (id_VCC) REFERENCES VCC (id),
  CONSTRAINT VCC_VCC_complicaciones_fk_2 FOREIGN KEY (id_VCC_complicaciones) REFERENCES VCC_complicaciones (id) );

CREATE TABLE IF NOT EXISTS VCC_VCC_biopsias (
  id_VCC int(10),
  id_VCC_biopsias int(10),
  PRIMARY KEY (id_VCC, id_VCC_biopsias),
  CONSTRAINT VCC_VCC_biopsias_fk_1 FOREIGN KEY (id_VCC) REFERENCES VCC (id),
  CONSTRAINT VCC_VCC_biopsias_fk_2 FOREIGN KEY (id_VCC_biopsias) REFERENCES VCC_biopsias (id) );

