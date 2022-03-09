alter table VEDA add fecha date not null default now();
alter table CPRE add fecha date not null default now();
ALTER TABLE VCC MODIFY COLUMN fecha date NOT NULL DEFAULT now();

ALTER TABLE VCC MODIFY ileoscopia boolean NOT NULL DEFAULT false;
ALTER TABLE VCC MODIFY comentarios varchar(4000) NOT NULL;
ALTER TABLE VCC MODIFY id_historia int(10) NOT NULL;

ALTER TABLE VEDA modify anestesia boolean NOT NULL DEFAULT false;
ALTER TABLE VEDA modify id_VEDA_tiempo int(10) NOT NULL DEFAULT 1;
ALTER TABLE VEDA modify comentarios varchar(4000) NOT NULL;

ALTER TABLE CPRE modify ambulatorio boolean NOT NULL default false;
ALTER TABLE CPRE modify cpre_previa boolean NOT NULL default false;
ALTER TABLE CPRE modify FR_DE_PA_SOD boolean NOT NULL default false;
ALTER TABLE CPRE modify FR_DE_PA_AUSENCIA_PC boolean NOT NULL default false;
ALTER TABLE CPRE modify FR_DE_PA_ANTEC_PA boolean NOT NULL default false;
ALTER TABLE CPRE modify CPRE_normal boolean NOT NULL default false; 
ALTER TABLE CPRE modify ESFINTEROPLASTIA boolean NOT NULL default false;
ALTER TABLE CPRE modify stent_duodenal boolean NOT NULL default false;
ALTER TABLE CPRE modify resolucion_completa boolean NOT NULL default false;
ALTER TABLE CPRE modify canulacion boolean NOT NULL default false;
ALTER TABLE CPRE modify biopsias boolean NOT NULL default false;
ALTER TABLE CPRE modify fracaso boolean NOT NULL default false;
ALTER TABLE CPRE modify embarazo boolean NOT NULL default false;
ALTER TABLE CPRE modify comentarios varchar(4000) NOT NULL;

ALTER TABLE VEDA ADD id_operador INT(10) NULL;
UPDATE veda SET id_operador=NULL;
ALTER TABLE VEDA ADD CONSTRAINT VEDA_usuario_fk FOREIGN KEY (id_operador) REFERENCES usuario (id);
