CREATE TABLE IF NOT EXISTS `configuracion_sistema` (
  `id` tinyint(3) unsigned NOT NULL,
  `titulo_pagina_principal` varchar(255) NOT NULL,
  `descripcion_sitio` varchar(2000) NOT NULL,
  `email_contacto` varchar(100) NOT NULL,
  `cantidad_registros_x_pagina` smallint(5) unsigned NOT NULL,
  `sitio_habilitado` tinyint(1) NOT NULL,
  `mensaje_sitio_deshabilitado` varchar(255) DEFAULT NULL,
  `actualizado_en` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

REPLACE INTO `configuracion_sistema` (`id`, `titulo_pagina_principal`, `descripcion_sitio`, `email_contacto`, `cantidad_registros_x_pagina`, `sitio_habilitado`, `mensaje_sitio_deshabilitado`, `actualizado_en`) VALUES
	(1, 'Servicio de gastroenterología del Hospital Rossi de La Plata', 'Gestión de historias clínicas de pacientes', 'ayuda@baires.com', 6, 1, 'Sitio deshabilitado', '2021-11-26 10:45:08');

CREATE TABLE IF NOT EXISTS `parametro` (
  `nombre` varchar(30) NOT NULL,
  `valorStr` varchar(255) DEFAULT NULL,
  `valorInt` int(10) DEFAULT NULL,
  PRIMARY KEY (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

REPLACE INTO `parametro` (`nombre`, `valorStr`, `valorInt`) VALUES
	('ID_ROL_ADMIN', NULL, 1);

CREATE TABLE IF NOT EXISTS `permiso` (
  `id` int(10) NOT NULL,
  `nombre` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

REPLACE INTO `permiso` (`id`, `nombre`) VALUES
	(6, 'user_admin'),
	(13, 'user_delete'),
	(15, 'user_index'),
	(7, 'user_list'),
	(12, 'user_new'),
	(9, 'user_perfil'),
	(8, 'user_roles'),
	(14, 'user_update');

CREATE TABLE IF NOT EXISTS `rol` (
  `id` int(10) NOT NULL,
  `nombre` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `nombre` (`nombre`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

REPLACE INTO `rol` (`id`, `nombre`) VALUES
	(1, 'ADMINISTRADOR'),
	(2, 'MEDICO'),
	(3, 'OPERADOR');

CREATE TABLE IF NOT EXISTS `rol_tiene_permiso` (
  `rol_id` int(10) NOT NULL,
  `permiso_id` int(10) NOT NULL,
  PRIMARY KEY (`rol_id`,`permiso_id`),
  KEY `rol_perm_fk_2` (`permiso_id`),
  CONSTRAINT `rol_perm_fk_1` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`),
  CONSTRAINT `rol_perm_fk_2` FOREIGN KEY (`permiso_id`) REFERENCES `permiso` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

REPLACE INTO `rol_tiene_permiso` (`rol_id`, `permiso_id`) VALUES
	(1, 6),
	(1, 7),
	(1, 8),
	(1, 9),
	(1, 12),
	(1, 13),
	(1, 14),
	(1, 15);


CREATE TABLE IF NOT EXISTS `usuario` (
  `id` int(10) NOT NULL AUTO_INCREMENT,
  `email` varchar(100) NOT NULL,
  `password` varchar(100) NOT NULL,
  `first_name` varchar(100) NOT NULL,
  `last_name` varchar(100) NOT NULL,
  `activo` tinyint(1) DEFAULT NULL,
  `updated_at` datetime DEFAULT NULL,
  `created_at` datetime DEFAULT NULL,
  `username` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `email` (`email`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;

REPLACE INTO `usuario` (`id`, `email`, `password`, `first_name`, `last_name`, `activo`, `updated_at`, `created_at`, `username`) VALUES
	(1, 'gpicci@gmail.com', 'pepe1234', 'Guillermo', 'Picci', 1, NULL, NULL, 'gpicci');

CREATE TABLE IF NOT EXISTS `usuario_tiene_rol` (
  `usuario_id` int(10) NOT NULL,
  `rol_id` int(10) NOT NULL,
  PRIMARY KEY (`usuario_id`,`rol_id`),
  KEY `usuario_rol_fk_2` (`rol_id`),
  CONSTRAINT `usuario_rol_fk_1` FOREIGN KEY (`usuario_id`) REFERENCES `usuario` (`id`),
  CONSTRAINT `usuario_rol_fk_2` FOREIGN KEY (`rol_id`) REFERENCES `rol` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

