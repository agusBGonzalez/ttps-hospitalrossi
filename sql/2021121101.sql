delete from rol_tiene_permiso;
delete from permiso;
INSERT INTO `tallertecn-is`.permiso (id,nombre) VALUES
	 (18,'historia_update'),
	 (16,'operador_index'),
	 (6,'user_admin'),
	 (13,'user_delete'),
	 (15,'user_index'),
	 (17,'user_issue_report'),
	 (7,'user_list'),
	 (12,'user_new'),
	 (9,'user_perfil'),
	 (8,'user_roles');
INSERT INTO `tallertecn-is`.permiso (id,nombre) VALUES
	 (14,'user_update');
	 
INSERT INTO `tallertecn-is`.rol_tiene_permiso (rol_id,permiso_id) VALUES
	 (1,6),
	 (1,7),
	 (1,8),
	 (1,9),
	 (1,12),
	 (1,13),
	 (1,14),
	 (1,15),
	 (2,17),
	 (2,18);
INSERT INTO `tallertecn-is`.rol_tiene_permiso (rol_id,permiso_id) VALUES
	 (3,16),
	 (3,17);
