CREATE TABLE `cpre_asa` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `descripcion` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

ALTER TABLE hepa ADD CONSTRAINT HEPA_historia_fk FOREIGN KEY (id_historia) REFERENCES historia (id);