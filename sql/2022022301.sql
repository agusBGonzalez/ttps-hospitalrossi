CREATE TABLE IF NOT EXISTS HEPA_cirrosis_etiologia (
  id int(10) NOT NULL AUTO_INCREMENT,
  descripcion varchar(100) NOT NULL,
  PRIMARY KEY (id) );
INSERT INTO HEPA_cirrosis_etiologia (descripcion) VALUES
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