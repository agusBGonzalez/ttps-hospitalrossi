alter table CPRE add hospital_derivacion varchar(200) null;
alter table CPRE DROP CONSTRAINT CPRE_hospital_FK;
alter table CPRE drop column id_hospital_derivacion;
