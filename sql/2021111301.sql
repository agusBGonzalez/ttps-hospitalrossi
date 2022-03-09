ALTER TABLE VCC ADD CONSTRAINT VCC_historia_fk FOREIGN KEY (id_historia) REFERENCES historia (id);


ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_1;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_2;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_3;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_4;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_5;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_6;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_7;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_8;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_9;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_10;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_11;
ALTER TABLE VCC DROP CONSTRAINT VCC_VCC_preparacion_fk_12;

DROP TABLE VCC_polipectomía_tam;
DROP TABLE VCC_polipectomía_material;
DROP TABLE VCC_polipectomía_tecnica;
DROP TABLE VCC_polipectomía_paris;

ALTER TABLE VCC RENAME COLUMN id_VCC_polipectomía_tam TO id_VCC_polipectomia_tam;
ALTER TABLE VCC RENAME COLUMN id_VCC_polipectomía_material TO id_VCC_polipectomia_material;
ALTER TABLE VCC RENAME COLUMN id_VCC_polipectomía_tecnica TO id_VCC_polipectomia_tecnica;
ALTER TABLE VCC RENAME COLUMN id_VCC_polipectomía_paris TO id_VCC_polipectomia_paris;

CREATE TABLE IF NOT EXISTS VCC_polipectomia_tam (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_polipectomia_tam(descripcion) VALUES
('<5mm'),
('e/ 5 y 10 mm'),
('>10mm'),
('>20mm')
;

CREATE TABLE IF NOT EXISTS VCC_polipectomia_material (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id));
INSERT INTO VCC_polipectomia_material (descripcion) VALUES
('pinza de biopsia'),
('ansa fría'),
('ansa caliente'),
('otros')
;

CREATE TABLE IF NOT EXISTS VCC_polipectomia_tecnica (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_polipectomia_tecnica (descripcion) VALUES
('lifting'),
('marcación de tinta china')
;

CREATE TABLE IF NOT EXISTS VCC_polipectomia_paris (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VCC_polipectomia_paris (descripcion) VALUES
('paris 0-ls'),
('paris 0-lsp'),
('paris 0-lp'),
('paris 0-lla'),
('paris 0-llb'),
('paris 0-llc'),
('otros')
;

ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_preparacion_fk FOREIGN KEY (id_vcc_preparacion) REFERENCES VCC_preparacion (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_incompleta_hasta_fk FOREIGN KEY (id_VCC_incompleta_hasta) REFERENCES VCC_incompleta_hasta (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_incompleta_motivo_fk FOREIGN KEY (id_VCC_incompleta_motivo) REFERENCES VCC_incompleta_motivo (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_lesion_sospechosa_fk FOREIGN KEY (id_VCC_lesion_sospechosa) REFERENCES VCC_lesion_sospechosa (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_polipos_cant_fk FOREIGN KEY (id_VCC_polipos_cant) REFERENCES VCC_polipos_cant (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_polipectomia_tam_fk FOREIGN KEY (id_VCC_polipectomia_tam) REFERENCES VCC_polipectomia_tam (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_polipectomia_material_fk FOREIGN KEY (id_VCC_polipectomia_material) REFERENCES VCC_polipectomia_material (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_polipectomia_tecnica_fk FOREIGN KEY (id_VCC_polipectomia_tecnica) REFERENCES VCC_polipectomia_tecnica (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_polipectomia_paris_fk FOREIGN KEY (id_VCC_polipectomia_paris) REFERENCES VCC_polipectomia_paris (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_de_guardia_fk FOREIGN KEY (id_VCC_de_guardia) REFERENCES VCC_de_guardia (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_tiempo_ingreso_fk FOREIGN KEY (id_VCC_tiempo_ingreso) REFERENCES VCC_tiempo_ingreso (id);
ALTER TABLE VCC ADD CONSTRAINT VCC_VCC_tiempo_retirada_fk FOREIGN KEY (id_VCC_tiempo_retirada) REFERENCES VCC_tiempo_retirada (id);


CREATE TABLE IF NOT EXISTS VEDA_incompleto (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_incompleto (descripcion) VALUES
('Intolerancia'),
('Restos alimentarios'),
('Descompensación clínica'),
('Otros')
;

CREATE TABLE IF NOT EXISTS VEDA_motivo (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_motivo (descripcion) VALUES
('erge'),
('erge refractario'),
('dispepsia'),
('dolor abdominal'),
('difagia'),
('imagen patológica'),
('srg'),
('anemia'),
('diarrea crónica'),
('vómitos persistente'),
('paf'),
('evaluación htp'),
('control de metaplasia'),
('control de barret'),
('búsqueda de primario'),
('otros')
;

CREATE TABLE IF NOT EXISTS VEDA_terapeutica (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_terapeutica (descripcion) VALUES
('lev'),
('dilatación'),
('escleroterapia'),
('colocación de stent'),
('extraccion de cuerpo extraño'),
('electrofulguración'),
('polipectomía'),
('gep'),
('colocación de k-108'),
('sengstaken-blakemore'),
('colocación de balón intragástrico'),
('hemospray'),
('otros')
;

CREATE TABLE IF NOT EXISTS VEDA_polipectomia_tam (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_polipectomia_tam(descripcion) VALUES
('<5mm'),
('e/ 5 y 10 mm'),
('>10mm'),
('>20mm')
;

CREATE TABLE IF NOT EXISTS VEDA_polipectomia_material (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id));
INSERT INTO VEDA_polipectomia_material (descripcion) VALUES
('pinza de biopsia'),
('ansa fría'),
('ansa caliente'),
('otros')
;


CREATE TABLE IF NOT EXISTS VEDA_polipectomia_paris (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_polipectomia_paris (descripcion) VALUES
('paris 0-ls'),
('paris 0-lsp'),
('paris 0-lp'),
('paris 0-lla'),
('paris 0-llb'),
('paris 0-llc'),
('otros')
;

CREATE TABLE IF NOT EXISTS VEDA_hallazgo (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_hallazgo (descripcion) VALUES
('normal'),
('eritema'),
('erosión'),
('úlcera'),
('pólipo'),
('patrón nodular'),
('mosaico'),
('signos de atrofia vellositaria'),
('esofagitis'),
('lesión submucosa'),
('estenosis'),
('gastropatía htp'),
('várices esofágicas'),
('varices gastricas'),
('angioectasias'),
('sufusiones hemorrágicas'),
('lesión orgánica'),
('dieulafoy'),
('gave'),
('hernia hiatal'),
('mese'),
('otros')
;

CREATE TABLE IF NOT EXISTS VEDA_biopsia (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_biopsia (descripcion) VALUES
('esfoago'),
('estómago'),
('duodeno'),
('otros')
;

CREATE TABLE IF NOT EXISTS VEDA_protocolo (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_protocolo (descripcion) VALUES
('seattle'),
('sydney'),
('e-celíaca'),
('esofagitis eosinofílica'),
('h.pylori'),
('otros')
;

CREATE TABLE IF NOT EXISTS VEDA_de_guardia (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_de_guardia (descripcion) VALUES
('hematemesis'),
('melena'),
('cuerpo extraño'),
('afagia'),
('cáusticos'),
('otros')
;

CREATE TABLE IF NOT EXISTS VEDA_tiempo (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO VEDA_tiempo (descripcion) VALUES
('menos de 7 min'),
('más de 7 min')
;

CREATE TABLE IF NOT EXISTS VEDA (
    id int(10) NOT NULL AUTO_INCREMENT,
    anestesia boolean NOT NULL,
    id_VEDA_incompleto int(10) NULL,
    id_VEDA_terapeutica int(10) NULL,
    id_VEDA_polipectomia_tam int(10) NULL,
    id_VEDA_polipectomia_material int(10) NULL,
    id_VEDA_polipectomia_paris int(10) NULL,
    id_VEDA_biopsia int(10) NULL,
    id_VEDA_protocolo int(10) NULL,
    id_VEDA_de_guardia int(10) NULL,
    id_VEDA_tiempo int(10) NOT NULL,
    comentarios varchar(2000) NOT NULL,
    PRIMARY KEY (id),
    CONSTRAINT VEDA_VEDA_incompleto_fk FOREIGN KEY (id_VEDA_incompleto) REFERENCES VEDA_incompleto (id),
    CONSTRAINT VEDA_VEDA_terapeutica_fk FOREIGN KEY (id_VEDA_terapeutica ) REFERENCES VEDA_terapeutica (id),
    CONSTRAINT VEDA_VEDA_polipectomia_tam_fk FOREIGN KEY (id_VEDA_polipectomia_tam ) REFERENCES VEDA_polipectomia_tam (id),
    CONSTRAINT VEDA_VEDA_polipectomia_material_fk FOREIGN KEY (id_VEDA_polipectomia_material ) REFERENCES VEDA_polipectomia_material (id),
    CONSTRAINT VEDA_VEDA_polipectomia_paris_fk FOREIGN KEY (id_VEDA_polipectomia_paris ) REFERENCES VEDA_polipectomia_paris (id),
    CONSTRAINT VEDA_VEDA_biopsia_fk FOREIGN KEY (id_VEDA_biopsia ) REFERENCES VEDA_biopsia (id),
    CONSTRAINT VEDA_VEDA_protocolo_fk FOREIGN KEY (id_VEDA_protocolo ) REFERENCES VEDA_protocolo (id),
    CONSTRAINT VEDA_VEDA_de_guardia_fk FOREIGN KEY (id_VEDA_de_guardia ) REFERENCES VEDA_de_guardia (id),
    CONSTRAINT VEDA_VEDA_tiempo_fk FOREIGN KEY (id_VEDA_tiempo ) REFERENCES VEDA_tiempo (id)
);

CREATE TABLE IF NOT EXISTS VEDA_VEDA_motivo (
  id_VEDA int(10),
  id_VEDA_motivo int(10),
  PRIMARY KEY (id_VEDA, id_VEDA_motivo),
  CONSTRAINT VEDA_VEDA_motivo_fk_1 FOREIGN KEY (id_VEDA) REFERENCES VEDA (id),
  CONSTRAINT VEDA_VEDA_motivo_fk_2 FOREIGN KEY (id_VEDA_motivo) REFERENCES VEDA_motivo (id) );

CREATE TABLE IF NOT EXISTS VEDA_VEDA_hallazgo (
  id_VEDA int(10),
  id_VEDA_hallazgo int(10),
  PRIMARY KEY (id_VEDA, id_VEDA_hallazgo),
  CONSTRAINT VEDA_VEDA_hallazgo_fk_1 FOREIGN KEY (id_VEDA) REFERENCES VEDA (id),
  CONSTRAINT VEDA_VEDA_hallazgo_fk_2 FOREIGN KEY (id_VEDA_hallazgo) REFERENCES VEDA_hallazgo (id) );
