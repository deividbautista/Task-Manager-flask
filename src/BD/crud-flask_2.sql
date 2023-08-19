-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 19-08-2023 a las 16:03:22
-- Versión del servidor: 10.4.28-MariaDB
-- Versión de PHP: 8.0.28

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `crud-flask_2`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `asignaciones`
--

CREATE TABLE `asignaciones` (
  `Id_asignaciones` int(11) NOT NULL,
  `id` int(11) DEFAULT NULL,
  `id_proceso` int(11) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `asignaciones`
--

INSERT INTO `asignaciones` (`Id_asignaciones`, `id`, `id_proceso`) VALUES
(26, 1, 125974386),
(27, 1, 574983621),
(28, 3, 574983621),
(29, 6, 574983621),
(30, 3, 684153927),
(31, 6, 684153927);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `procesos`
--

CREATE TABLE `procesos` (
  `id_proceso` int(11) NOT NULL,
  `Titulo` varchar(20) NOT NULL,
  `Descripcion` longtext DEFAULT NULL,
  `Fecha_creacion` date NOT NULL DEFAULT curdate(),
  `Fecha_terminación` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `procesos`
--

INSERT INTO `procesos` (`id_proceso`, `Titulo`, `Descripcion`, `Fecha_creacion`, `Fecha_terminación`) VALUES
(125974386, 'comer', 'tengo hambre we', '2023-08-16', '2023-08-16'),
(574983621, 'comer', 'tengo hambre we', '2023-08-17', '2023-08-17'),
(657981423, 'comer', 'tengo hambre we', '2023-08-16', '2023-08-16'),
(684153927, 'programar', '\"Desde la fundación de su Legión cuando nació el Imperio, los Marines Espaciales de los Ángeles Oscuros han sido temidos por sus enemigos y respetados por aquellos a los que han protegido. Perseverantes y eficientes en combate, siempre permanecen alerta y cumplen con celo aquellas funciones que les son asignadas. Los Ángeles Oscuros se cuentan entre los sirvientes más leales del Emperador. Pero no siempre ha sido así. Durante diez milenios los Ángeles Oscuros han ocultado un siniestro secreto, un acto tan terrible y vergonzoso que pone en peligro aquello que los Ángeles Oscuros más aman, algo que puede conducirles a la condenación eterna.\"', '2023-08-17', '2023-08-18');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `users`
--

CREATE TABLE `users` (
  `id` int(11) NOT NULL,
  `NDI` int(20) NOT NULL,
  `password` char(102) NOT NULL,
  `fullname` varchar(50) NOT NULL,
  `Direccion` varchar(30) NOT NULL,
  `Telefono` int(15) NOT NULL,
  `Empresa` varchar(35) NOT NULL,
  `Cargo` varchar(25) NOT NULL,
  `Area_locativa` varchar(30) NOT NULL,
  `Email` varchar(35) NOT NULL,
  `Fecha_nacimiento` date DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci COMMENT='Stores the user''s data.';

--
-- Volcado de datos para la tabla `users`
--

INSERT INTO `users` (`id`, `NDI`, `password`, `fullname`, `Direccion`, `Telefono`, `Empresa`, `Cargo`, `Area_locativa`, `Email`, `Fecha_nacimiento`) VALUES
(1, 21474836, '12345678', 'deivid bautista', 'calle siempre viva109', 31212287, 'Americana de servicios L.T.D.A', 'Aprendiz', 'Oficina', 'debautist15@gmail.com', '2023-05-02'),
(3, 101016642, 'arnulfo', 'hernesto', '', 0, '', '', '', '', NULL),
(6, 10986287, 'owbeuf993', 'armin torres', 'wndnowbdo', 0, '', '', '', '', NULL);

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  ADD PRIMARY KEY (`Id_asignaciones`),
  ADD KEY `fk_asignaciones_users` (`id`),
  ADD KEY `id_proceso` (`id_proceso`);

--
-- Indices de la tabla `procesos`
--
ALTER TABLE `procesos`
  ADD PRIMARY KEY (`id_proceso`);

--
-- Indices de la tabla `users`
--
ALTER TABLE `users`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  MODIFY `Id_asignaciones` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=32;

--
-- AUTO_INCREMENT de la tabla `procesos`
--
ALTER TABLE `procesos`
  MODIFY `id_proceso` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2147483648;

--
-- AUTO_INCREMENT de la tabla `users`
--
ALTER TABLE `users`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `asignaciones`
--
ALTER TABLE `asignaciones`
  ADD CONSTRAINT `asignaciones_ibfk_1` FOREIGN KEY (`id_proceso`) REFERENCES `procesos` (`id_proceso`) ON DELETE CASCADE ON UPDATE CASCADE,
  ADD CONSTRAINT `fk_asignaciones_users` FOREIGN KEY (`id`) REFERENCES `users` (`id`) ON DELETE CASCADE;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
