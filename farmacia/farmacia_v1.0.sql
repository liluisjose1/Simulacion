-- phpMyAdmin SQL Dump
-- version 4.5.4.1deb2ubuntu2
-- http://www.phpmyadmin.net
--
-- Servidor: localhost
-- Tiempo de generación: 28-06-2018 a las 13:27:10
-- Versión del servidor: 10.0.34-MariaDB-0ubuntu0.16.04.1
-- Versión de PHP: 7.0.30-0ubuntu0.16.04.1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `farmacia`
--
CREATE DATABASE IF NOT EXISTS `farmacia` DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE `farmacia`;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(80) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add user dashboard module', 1, 'add_userdashboardmodule'),
(2, 'Can change user dashboard module', 1, 'change_userdashboardmodule'),
(3, 'Can delete user dashboard module', 1, 'delete_userdashboardmodule'),
(4, 'Can add bookmark', 2, 'add_bookmark'),
(5, 'Can change bookmark', 2, 'change_bookmark'),
(6, 'Can delete bookmark', 2, 'delete_bookmark'),
(7, 'Can add pinned application', 3, 'add_pinnedapplication'),
(8, 'Can change pinned application', 3, 'change_pinnedapplication'),
(9, 'Can delete pinned application', 3, 'delete_pinnedapplication'),
(10, 'Can add log entry', 4, 'add_logentry'),
(11, 'Can change log entry', 4, 'change_logentry'),
(12, 'Can delete log entry', 4, 'delete_logentry'),
(13, 'Can add group', 5, 'add_group'),
(14, 'Can change group', 5, 'change_group'),
(15, 'Can delete group', 5, 'delete_group'),
(16, 'Can add user', 6, 'add_user'),
(17, 'Can change user', 6, 'change_user'),
(18, 'Can delete user', 6, 'delete_user'),
(19, 'Can add permission', 7, 'add_permission'),
(20, 'Can change permission', 7, 'change_permission'),
(21, 'Can delete permission', 7, 'delete_permission'),
(22, 'Can add content type', 8, 'add_contenttype'),
(23, 'Can change content type', 8, 'change_contenttype'),
(24, 'Can delete content type', 8, 'delete_contenttype'),
(25, 'Can add session', 9, 'add_session'),
(26, 'Can change session', 9, 'change_session'),
(27, 'Can delete session', 9, 'delete_session'),
(28, 'Can add abastecer', 10, 'add_abastecer'),
(29, 'Can change abastecer', 10, 'change_abastecer'),
(30, 'Can delete abastecer', 10, 'delete_abastecer'),
(31, 'Can add categoria', 11, 'add_categoria'),
(32, 'Can change categoria', 11, 'change_categoria'),
(33, 'Can delete categoria', 11, 'delete_categoria'),
(34, 'Can add medicamento', 12, 'add_medicamento'),
(35, 'Can change medicamento', 12, 'change_medicamento'),
(36, 'Can delete medicamento', 12, 'delete_medicamento'),
(37, 'Can add detalle_ facturas', 13, 'add_detalle_facturas'),
(38, 'Can change detalle_ facturas', 13, 'change_detalle_facturas'),
(39, 'Can delete detalle_ facturas', 13, 'delete_detalle_facturas'),
(40, 'Can add factura', 14, 'add_factura'),
(41, 'Can change factura', 14, 'change_factura'),
(42, 'Can delete factura', 14, 'delete_factura'),
(43, 'Can add abastecimiento', 10, 'add_abastecimiento'),
(44, 'Can change abastecimiento', 10, 'change_abastecimiento'),
(45, 'Can delete abastecimiento', 10, 'delete_abastecimiento');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$100000$95Upu1Cg5ZJ6$6wBoRRDA2CPIMpOlGdEZBWVyRv54yOUDitdgWSiqKDs=', '2018-06-25 15:08:08.266036', 1, 'liluisjose1', '', '', 'liluisjose1@gmail.com', 1, 1, '2018-06-24 04:21:29.092120');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `dashboard_userdashboardmodule`
--

CREATE TABLE `dashboard_userdashboardmodule` (
  `id` int(11) NOT NULL,
  `title` varchar(255) NOT NULL,
  `module` varchar(255) NOT NULL,
  `app_label` varchar(255) DEFAULT NULL,
  `user` int(10) UNSIGNED NOT NULL,
  `column` int(10) UNSIGNED NOT NULL,
  `order` int(11) NOT NULL,
  `settings` longtext NOT NULL,
  `children` longtext NOT NULL,
  `collapsed` tinyint(1) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `dashboard_userdashboardmodule`
--

INSERT INTO `dashboard_userdashboardmodule` (`id`, `title`, `module`, `app_label`, `user`, `column`, `order`, `settings`, `children`, `collapsed`) VALUES
(1, 'Enlaces Rápidos', 'jet.dashboard.modules.LinkList', NULL, 1, 0, 0, '{"layout": "inline", "deletable": false, "collapsible": false, "draggable": false}', '[{"url": "/", "title": "Volver al sitio"}, {"url": "/admin/password_change/", "title": "Cambiar contrase\\u00f1a"}, {"url": "/admin/logout/", "title": "Cerrar sesi\\u00f3n"}]', 0),
(2, 'Aplicaciones', 'jet.dashboard.modules.AppList', NULL, 1, 1, 0, '{"models": null, "exclude": ["auth.*"]}', '', 0),
(3, 'Administración', 'jet.dashboard.modules.AppList', NULL, 1, 2, 0, '{"models": ["auth.*"], "exclude": null}', '', 0),
(4, 'Acciones recientes', 'jet.dashboard.modules.RecentActions', NULL, 1, 0, 1, '{"user": null, "limit": 10, "exclude_list": null, "include_list": null}', '', 0),
(5, 'Últimas Noticias de Django', 'jet.dashboard.modules.Feed', NULL, 1, 1, 1, '{"feed_url": "http://www.djangoproject.com/rss/weblog/", "limit": 5}', '', 0),
(6, 'Soporte', 'jet.dashboard.modules.LinkList', NULL, 1, 2, 1, '{"layout": "stacked", "deletable": true, "collapsible": true, "draggable": true}', '[{"external": true, "url": "http://docs.djangoproject.com/", "title": "Documentaci\\u00f3n Django"}, {"external": true, "url": "http://groups.google.com/group/django-users", "title": "Lista de correos Django \\"django-users\\""}, {"external": true, "url": "irc://irc.freenode.net/django", "title": "Canal IRC de Django"}]', 0),
(7, 'Modelos de la aplicación', 'jet.dashboard.modules.ModelList', 'inventario', 1, 0, 0, '{"models": ["inventario.*"], "exclude": null}', '', 0),
(8, 'Acciones recientes', 'jet.dashboard.modules.RecentActions', 'inventario', 1, 1, 0, '{"user": null, "limit": 10, "exclude_list": null, "include_list": ["inventario.*"]}', '', 0),
(9, 'Modelos de la aplicación', 'jet.dashboard.modules.ModelList', 'ventas', 1, 0, 0, '{"models": ["ventas.*"], "exclude": null}', '', 0),
(10, 'Acciones recientes', 'jet.dashboard.modules.RecentActions', 'ventas', 1, 1, 0, '{"user": null, "limit": 10, "exclude_list": null, "include_list": ["ventas.*"]}', '', 0);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2018-06-24 04:22:15.668681', '1', 'Suplementos', 1, '[{"added": {}}]', 11, 1),
(2, '2018-06-24 04:22:53.962862', '1', 'ANIMAL', 1, '[{"added": {}}]', 12, 1),
(3, '2018-06-24 04:23:08.446005', '1', 'ANIMAL', 1, '[{"added": {}}]', 10, 1),
(4, '2018-06-24 04:23:51.461009', '1', '0022', 1, '[{"added": {}}, {"added": {"name": "detalle_ facturas", "object": "ANIMAL"}}]', 14, 1),
(5, '2018-06-24 22:20:42.218837', '2', 'ANIMAL', 1, '[{"added": {}}]', 10, 1),
(6, '2018-06-24 22:20:49.973245', '1', 'ANIMAL', 3, '', 10, 1),
(7, '2018-06-25 15:08:36.704933', '3', 'ANIMAL', 1, '[{"added": {}}]', 10, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(4, 'admin', 'logentry'),
(5, 'auth', 'group'),
(7, 'auth', 'permission'),
(6, 'auth', 'user'),
(8, 'contenttypes', 'contenttype'),
(1, 'dashboard', 'userdashboardmodule'),
(10, 'inventario', 'abastecimiento'),
(11, 'inventario', 'categoria'),
(12, 'inventario', 'medicamento'),
(2, 'jet', 'bookmark'),
(3, 'jet', 'pinnedapplication'),
(9, 'sessions', 'session'),
(13, 'ventas', 'detalle_facturas'),
(14, 'ventas', 'factura');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2018-06-24 04:21:03.382876'),
(2, 'auth', '0001_initial', '2018-06-24 04:21:03.798129'),
(3, 'admin', '0001_initial', '2018-06-24 04:21:03.901315'),
(4, 'admin', '0002_logentry_remove_auto_add', '2018-06-24 04:21:03.924584'),
(5, 'contenttypes', '0002_remove_content_type_name', '2018-06-24 04:21:03.997950'),
(6, 'auth', '0002_alter_permission_name_max_length', '2018-06-24 04:21:04.040559'),
(7, 'auth', '0003_alter_user_email_max_length', '2018-06-24 04:21:04.090323'),
(8, 'auth', '0004_alter_user_username_opts', '2018-06-24 04:21:04.114533'),
(9, 'auth', '0005_alter_user_last_login_null', '2018-06-24 04:21:04.145403'),
(10, 'auth', '0006_require_contenttypes_0002', '2018-06-24 04:21:04.149647'),
(11, 'auth', '0007_alter_validators_add_error_messages', '2018-06-24 04:21:04.169614'),
(12, 'auth', '0008_alter_user_username_max_length', '2018-06-24 04:21:04.242150'),
(13, 'auth', '0009_alter_user_last_name_max_length', '2018-06-24 04:21:04.293400'),
(14, 'dashboard', '0001_initial', '2018-06-24 04:21:04.318905'),
(15, 'inventario', '0001_initial', '2018-06-24 04:21:04.482342'),
(16, 'jet', '0001_initial', '2018-06-24 04:21:04.562996'),
(17, 'jet', '0002_delete_userdashboardmodule', '2018-06-24 04:21:04.575473'),
(18, 'sessions', '0001_initial', '2018-06-24 04:21:04.618086'),
(19, 'ventas', '0001_initial', '2018-06-24 04:21:04.791378'),
(20, 'inventario', '0002_auto_20180624_1619', '2018-06-24 22:19:51.414800');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('47tdh5r8g2zerizt147u9ce24v1fi3o6', 'ODA3ZmY1NWE4ZmQ3NmQ4OWZlNmJmM2Y4ZmVkZTcxMmZmMjM2MTAxNTp7Il9hdXRoX3VzZXJfaGFzaCI6Ijc0MGQyMzYzNGNhZjllYzE3ODRjMzkxZGIzMTYwM2Y3MjYyMThlODAiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaWQiOiIxIn0=', '2018-07-08 04:21:54.825001'),
('9onquyna26xpklus8fqma7n3uwbl8n5y', 'ZjE0MTFlMWFjYzFiMjUxODliOTZlZTNlNjI3MDQ2YjVmMDZjMjM3Mjp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9oYXNoIjoiNzQwZDIzNjM0Y2FmOWVjMTc4NGMzOTFkYjMxNjAzZjcyNjIxOGU4MCIsIl9hdXRoX3VzZXJfYmFja2VuZCI6ImRqYW5nby5jb250cmliLmF1dGguYmFja2VuZHMuTW9kZWxCYWNrZW5kIn0=', '2018-07-09 15:08:08.271636');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_abastecimiento`
--

CREATE TABLE `inventario_abastecimiento` (
  `id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `fecha_abastecimiento` date NOT NULL,
  `medicamento_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `inventario_abastecimiento`
--

INSERT INTO `inventario_abastecimiento` (`id`, `cantidad`, `fecha_abastecimiento`, `medicamento_id`) VALUES
(2, 20, '2018-06-24', 1),
(3, 40, '2018-06-25', 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_categoria`
--

CREATE TABLE `inventario_categoria` (
  `id` int(11) NOT NULL,
  `nombre` varchar(60) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `inventario_categoria`
--

INSERT INTO `inventario_categoria` (`id`, `nombre`) VALUES
(1, 'Suplementos');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `inventario_medicamento`
--

CREATE TABLE `inventario_medicamento` (
  `id` int(11) NOT NULL,
  `codigo` varchar(10) NOT NULL,
  `nombre` varchar(200) NOT NULL,
  `fecha_creacion` date NOT NULL,
  `descripcion` longtext NOT NULL,
  `precio_Compra` decimal(5,2) NOT NULL,
  `precio_venta` decimal(5,2) NOT NULL,
  `stock` smallint(5) UNSIGNED NOT NULL,
  `categoria_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `inventario_medicamento`
--

INSERT INTO `inventario_medicamento` (`id`, `codigo`, `nombre`, `fecha_creacion`, `descripcion`, `precio_Compra`, `precio_venta`, `stock`, `categoria_id`) VALUES
(1, '000023-33', 'ANIMAL', '2018-06-23', 'Proteina', '20.00', '80.00', 80, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jet_bookmark`
--

CREATE TABLE `jet_bookmark` (
  `id` int(11) NOT NULL,
  `url` varchar(200) NOT NULL,
  `title` varchar(255) NOT NULL,
  `user` int(10) UNSIGNED NOT NULL,
  `date_add` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `jet_pinnedapplication`
--

CREATE TABLE `jet_pinnedapplication` (
  `id` int(11) NOT NULL,
  `app_label` varchar(255) NOT NULL,
  `user` int(10) UNSIGNED NOT NULL,
  `date_add` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_detalle_facturas`
--

CREATE TABLE `ventas_detalle_facturas` (
  `id` int(11) NOT NULL,
  `cantidad` int(11) NOT NULL,
  `Factura_id` int(11) DEFAULT NULL,
  `medicamento_id` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `ventas_detalle_facturas`
--

INSERT INTO `ventas_detalle_facturas` (`id`, `cantidad`, `Factura_id`, `medicamento_id`) VALUES
(1, 20, 1, 1);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `ventas_factura`
--

CREATE TABLE `ventas_factura` (
  `id` int(11) NOT NULL,
  `codigo` varchar(10) NOT NULL,
  `cliente` varchar(10) NOT NULL,
  `fecha` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- Volcado de datos para la tabla `ventas_factura`
--

INSERT INTO `ventas_factura` (`id`, `codigo`, `cliente`, `fecha`) VALUES
(1, '0022', 'Juanito', '2018-06-24 04:23:51.458172');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indices de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indices de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indices de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indices de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indices de la tabla `dashboard_userdashboardmodule`
--
ALTER TABLE `dashboard_userdashboardmodule`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk` (`user_id`);

--
-- Indices de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indices de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indices de la tabla `inventario_abastecimiento`
--
ALTER TABLE `inventario_abastecimiento`
  ADD PRIMARY KEY (`id`),
  ADD KEY `inventario_abastecer_medicamento_id_f4736096_fk_inventari` (`medicamento_id`);

--
-- Indices de la tabla `inventario_categoria`
--
ALTER TABLE `inventario_categoria`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `inventario_medicamento`
--
ALTER TABLE `inventario_medicamento`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`),
  ADD UNIQUE KEY `nombre` (`nombre`),
  ADD KEY `inventario_medicamen_categoria_id_29ab8241_fk_inventari` (`categoria_id`);

--
-- Indices de la tabla `jet_bookmark`
--
ALTER TABLE `jet_bookmark`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `jet_pinnedapplication`
--
ALTER TABLE `jet_pinnedapplication`
  ADD PRIMARY KEY (`id`);

--
-- Indices de la tabla `ventas_detalle_facturas`
--
ALTER TABLE `ventas_detalle_facturas`
  ADD PRIMARY KEY (`id`),
  ADD KEY `ventas_detalle_facturas_Factura_id_b8e94592_fk_ventas_factura_id` (`Factura_id`),
  ADD KEY `ventas_detalle_factu_medicamento_id_af22e2f6_fk_inventari` (`medicamento_id`);

--
-- Indices de la tabla `ventas_factura`
--
ALTER TABLE `ventas_factura`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `codigo` (`codigo`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=46;
--
-- AUTO_INCREMENT de la tabla `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `dashboard_userdashboardmodule`
--
ALTER TABLE `dashboard_userdashboardmodule`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;
--
-- AUTO_INCREMENT de la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;
--
-- AUTO_INCREMENT de la tabla `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;
--
-- AUTO_INCREMENT de la tabla `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=21;
--
-- AUTO_INCREMENT de la tabla `inventario_abastecimiento`
--
ALTER TABLE `inventario_abastecimiento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=4;
--
-- AUTO_INCREMENT de la tabla `inventario_categoria`
--
ALTER TABLE `inventario_categoria`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `inventario_medicamento`
--
ALTER TABLE `inventario_medicamento`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `jet_bookmark`
--
ALTER TABLE `jet_bookmark`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `jet_pinnedapplication`
--
ALTER TABLE `jet_pinnedapplication`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;
--
-- AUTO_INCREMENT de la tabla `ventas_detalle_facturas`
--
ALTER TABLE `ventas_detalle_facturas`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- AUTO_INCREMENT de la tabla `ventas_factura`
--
ALTER TABLE `ventas_factura`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;
--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Filtros para la tabla `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Filtros para la tabla `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Filtros para la tabla `inventario_abastecimiento`
--
ALTER TABLE `inventario_abastecimiento`
  ADD CONSTRAINT `inventario_abastecer_medicamento_id_f4736096_fk_inventari` FOREIGN KEY (`medicamento_id`) REFERENCES `inventario_medicamento` (`id`);

--
-- Filtros para la tabla `inventario_medicamento`
--
ALTER TABLE `inventario_medicamento`
  ADD CONSTRAINT `inventario_medicamen_categoria_id_29ab8241_fk_inventari` FOREIGN KEY (`categoria_id`) REFERENCES `inventario_categoria` (`id`);

--
-- Filtros para la tabla `ventas_detalle_facturas`
--
ALTER TABLE `ventas_detalle_facturas`
  ADD CONSTRAINT `ventas_detalle_factu_medicamento_id_af22e2f6_fk_inventari` FOREIGN KEY (`medicamento_id`) REFERENCES `inventario_medicamento` (`id`),
  ADD CONSTRAINT `ventas_detalle_facturas_Factura_id_b8e94592_fk_ventas_factura_id` FOREIGN KEY (`Factura_id`) REFERENCES `ventas_factura` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
