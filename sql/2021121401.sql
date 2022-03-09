alter table cpre add id_cpre_grado_asge int(10);
alter table cpre add id_cpre_grado_dif int(10);

ALTER TABLE cpre ADD CONSTRAINT cpre_cpre_grado_asge_fk FOREIGN KEY (id_cpre_grado_asge) REFERENCES cpre_grado_asge (id);
ALTER TABLE cpre ADD CONSTRAINT cpre_cpre_grado_dif_fk FOREIGN KEY (id_cpre_grado_dif) REFERENCES cpre_grado_dif (id);

drop table cpre_cpre_grado_asge ;
drop table cpre_cpre_grado_dif ;

