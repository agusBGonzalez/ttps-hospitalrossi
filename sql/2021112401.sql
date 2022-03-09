UPDATE vcc SET id_vcc_lesion_sospechosa = NULL WHERE  id_vcc_lesion_sospechosa = 3;
DELETE FROM vcc_lesion_sospechosa where id = 3;

UPDATE vcc_lesion_sospechosa SET descripcion=replace(descripcion, 'Si, ','');
