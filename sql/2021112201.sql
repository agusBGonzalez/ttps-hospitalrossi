CREATE TABLE IF NOT EXISTS HEPA_etiologia (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO HEPA_etiologia (descripcion) VALUES
('VHC'),
('Alcohol'),
('NASH'),
('VHB'),
('HAI'),
('CEP'),
('CBP'),
('Hemocromatosis'),
('Enfermedad de Wilson LFH'),
('Hipertransaminasemia'),
('VHA'),
('Hiperbilirrubinemia/Colestasis'),
('otras')
;

CREATE TABLE IF NOT EXISTS HEPA_descompensacion (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO HEPA_descompensacion (descripcion) VALUES
('HDA'),
('PBE'),
('Encefalopatía'),
('Hiponatremia'),
('AKI'),
('Sindrome Hepatorenal'),
('Síndrome Hepatopulmonar/Hpp'),
('Varices no Sangrantes'),
('Infecciones no Pbe'),
('Control Consultorio')
;

CREATE TABLE IF NOT EXISTS HEPA_cirrosis_etiologia (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO HEPA_etiologia (descripcion) VALUES
('VHC'),
('Alcohol'),
('NASH'),
('VHB'),
('HAI'),
('CEP'),
('CBP'),
('Hemocromatosis'),
('Enfermedad de Wilson'),
('otras')
;

CREATE TABLE IF NOT EXISTS HEPA_child_pugh (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO HEPA_child_pugh (descripcion) VALUES
('A5'),
('A6'),
('B7'),
('B8'),
('B9'),
('C10'),
('C11'),
('C12'),
('C13'),
('C14'),
('C15')
;

CREATE TABLE IF NOT EXISTS HEPA (
    id int(10) NOT NULL AUTO_INCREMENT,
    id_historia int(10),
    fecha date,
    id_operador INT(10),
    -- etilogia
    consultorio boolean NOT NULL,
    -- Cirrosis - Etiología
    id_HEPA_descompensacion int(10) NULL,
    hepatocarcinoma  boolean NOT NULL,
    lesion_focal_hepatica  boolean NOT NULL,
    meld int(10) NULL,
    id_HEPA_child_pugh int(10) NULL,
    PRIMARY KEY (id),
    CONSTRAINT HEPA_HEPA_descompensacion_fk FOREIGN KEY (id_HEPA_descompensacion) REFERENCES HEPA_descompensacion (id),
    CONSTRAINT HEPA_HEPA_child_pugh_fk FOREIGN KEY (id_HEPA_child_pugh) REFERENCES HEPA_child_pugh (id)
);

CREATE TABLE IF NOT EXISTS HEPA_HEPA_etiologia (
  id_HEPA int(10),
  id_HEPA_etiologia int(10),
  PRIMARY KEY (id_HEPA, id_HEPA_etiologia),
  CONSTRAINT HEPA_HEPA_etiologia_fk_1 FOREIGN KEY (id_HEPA) REFERENCES HEPA (id),
  CONSTRAINT HEPA_HEPA_etiologia_fk_2 FOREIGN KEY (id_HEPA_etiologia) REFERENCES HEPA_etiologia (id) );

CREATE TABLE IF NOT EXISTS HEPA_HEPA_cirrosis_etiologia (
  id_HEPA int(10),
  id_HEPA_cirrosis_etiologia int(10),
  PRIMARY KEY (id_HEPA, id_HEPA_cirrosis_etiologia),
  CONSTRAINT HEPA_HEPA_cirrosis_etiologia_fk_1 FOREIGN KEY (id_HEPA) REFERENCES HEPA (id),
  CONSTRAINT HEPA_HEPA_cirrosis_etiologia_fk_2 FOREIGN KEY (id_HEPA_cirrosis_etiologia) REFERENCES HEPA_cirrosis_etiologia (id)
);
