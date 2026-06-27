-- Crear base de datos
CREATE DATABASE IF NOT EXISTS videojuegos_db
CHARACTER SET utf8mb4
COLLATE utf8mb4_unicode_ci;

USE videojuegos_db;

-- ==========================
-- Tabla jugadores
-- ==========================
CREATE TABLE jugadores (
    identificacion VARCHAR(20) PRIMARY KEY,
    nombre_completo VARCHAR(100) NOT NULL,
    correo_electronico VARCHAR(100) NOT NULL,
    pais VARCHAR(50) NOT NULL
);

-- ==========================
-- Tabla videojuegos
-- ==========================
CREATE TABLE videojuegos (
    codigo VARCHAR(20) PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    desarrollador VARCHAR(100) NOT NULL,
    categoria VARCHAR(50) NOT NULL,
    licencias_disponibles INT NOT NULL DEFAULT 0
);
