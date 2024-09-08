DROP DATABASE IF EXISTS maquinaextensiones;
-- Crear la base de datos
CREATE DATABASE maquinaextensiones;
USE maquinaextensiones;

-- Crear la tabla para los tipos de trenza
CREATE TABLE trenza (
    id_trenza INT PRIMARY KEY AUTO_INCREMENT,  -- Llave primaria con auto incremento
    tipo_trenza VARCHAR(50) NOT NULL  -- Nombre del tipo de trenza, no puede ser nulo
);

-- Crear la tabla para las extensiones de máquina
CREATE TABLE maquina_extensiones (
    id_maquina INT PRIMARY KEY AUTO_INCREMENT,  -- Llave primaria para la máquina
    id_trenza INT,  -- Llave foránea que hace referencia a la tabla trenza
    longitud INT,  -- Longitud, sin validación aquí (ver nota)
    FOREIGN KEY (id_trenza) REFERENCES trenza(id_trenza)  -- Relación con la tabla trenza
    -- Validación de longitud se puede manejar en la aplicación o mediante un trigger si el SGBD lo permite
);

-- Insertar datos en la tabla trenza
INSERT INTO trenza (tipo_trenza) VALUES ('trenza simple'); 
INSERT INTO trenza (tipo_trenza) VALUES ('trenza espiga');
INSERT INTO trenza (tipo_trenza) VALUES ('trenza africana');

-- Insertar datos en la tabla maquina_extensiones
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (1, 50);  -- trenza simple, 50 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (2, 30);  -- trenza espiga, 30 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (3, 40);  -- trenza africana, 40 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (1, 60);  -- trenza simple, 60 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (2, 20);  -- trenza espiga, 20 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (3, 80);  -- trenza africana, 80 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (1, 25);  -- trenza simple, 25 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (2, 70);  -- trenza espiga, 70 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (3, 45);  -- trenza africana, 45 cm
INSERT INTO maquina_extensiones (id_trenza, longitud) VALUES (1, 55);  -- trenza simple, 55 cm

-- Consultas
-- Consulta 1: Obtener todos los registros con detalles completos
SELECT me.id_maquina, t.tipo_trenza, me.longitud
FROM maquina_extensiones me
JOIN trenza t ON me.id_trenza = t.id_trenza;

-- Consulta 2: Obtener registros con longitud mayor a 50 cm
SELECT me.id_maquina, t.tipo_trenza, me.longitud
FROM maquina_extensiones me
JOIN trenza t ON me.id_trenza = t.id_trenza
WHERE me.longitud > 50;

-- Consulta 3: Contar el número de máquinas por tipo de trenza
SELECT t.tipo_trenza, COUNT(me.id_maquina) AS total_maquinas
FROM maquina_extensiones me
JOIN trenza t ON me.id_trenza = t.id_trenza
GROUP BY t.tipo_trenza;

-- Consulta 4: Obtener registros para el tipo de trenza 'trenza espiga'
SELECT me.id_maquina, me.longitud
FROM maquina_extensiones me
JOIN trenza t ON me.id_trenza = t.id_trenza
WHERE t.tipo_trenza = 'trenza espiga';

-- Consulta 5: Obtener registros con longitud entre 20 y 60 cm
SELECT me.id_maquina, t.tipo_trenza, me.longitud
FROM maquina_extensiones me
JOIN trenza t ON me.id_trenza = t.id_trenza
WHERE me.longitud BETWEEN 20 AND 60;
