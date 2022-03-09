-- Solucion de meld
ALTER TABLE hepa DROP COLUMN meld;
ALTER TABLE hepa ADD meld int(2) NULL;

CREATE TABLE IF NOT EXISTS HEPA_HEPA_cirrosis_etiologia (
  id_HEPA int(10),
  id_HEPA_cirrosis_etiologia int(10),
  PRIMARY KEY (id_HEPA, id_HEPA_cirrosis_etiologia),
  CONSTRAINT HEPA_HEPA_cirrosis_etiologia_fk_1 FOREIGN KEY (id_HEPA) REFERENCES HEPA (id),
  CONSTRAINT HEPA_HEPA_cirrosis_etiologia_fk_2 FOREIGN KEY (id_HEPA_cirrosis_etiologia) REFERENCES HEPA_cirrosis_etiologia (id)
);

