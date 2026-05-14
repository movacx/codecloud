create database curso;
drop dataBase curso;
USE curso;

--crear base de datos
create table empleado
(idEmpleado int,
nombre varchar(40),
salario int,
provincia varchar(20),
idDepartamento int, primary key(idEmpleado));





INSERT INTO empleado(idEmpleado, nombre, salario, provincia, idDepartamento)
values(1, 'juan', 100, 'puntarenas', 1);

INSERT INTO empleado(idEmpleado, nombre, salario, provincia, idDepartamento)
values(2, 'fabian', 150, 'san jose', 2);


insert into empleado(idEmpleado, nombre, salario, provincia, idDepartamento)
values(3, 'maria',200,'Puntarenas',1);

insert into empleado(idEmpleado, nombre, salario, provincia, idDepartamento)
values(4, 'Ana',150,'Alajuela',2);

insert into empleado(idEmpleado, nombre, salario, provincia, idDepartamento)
values(5, 'Jose',150,'Puntarenas',2);


select * from empleado;

-- SELECT 
Select --> Campos
from --> Tablas
where --> Condiciones


--> nota: Las condiciones se aplican de manera individual registro por registro
-- mostrar el codigo y el nombre de todos los empleados

Select idEmpleado, nombre
from empleado;

-- listar el nombr de los empleados
-- que trabajan en el departamento 1

Select nombre
from empleado
where idDepartamento = 1

-- listar los empleados que viven en Puntarenas y trabajen en el departamento 2
Select nombre
from empleado
where provincia= 'Puntarenas' and idDepartamento=2


-- funciones de agrupamiento
-- SUM, COUNT, MAX, MIN, AVG

-- mostrar cuantos empleados existen

select count(*)
from empleado;

select count(*) as 'conteo'
from empleado;

select count(idEmpleado) as 'pene'
from empleado;
-- si usamos campos dentro del count, no se toman en cuenta los nulos

-- mostrar el monto del salario maximo que se paga
select max(salario)
from empleado;

-- mostrar el monto minimo que se paga
select min(salario)
from empleado;

-- mostrar el salario promedio que se paga
select avg(salario)
from empleado;

--mostrar cuanto se paga en total
select sum(salario)
from empleado

-- listar el salario maximno y minimo de los empleados de puntarenas

selec max(salario), min(salario)
from empleado
where provincia='puntarenas'

--IN, NOT IN 
--Se utilizan para buscar en conjuntos de datos

--listar los empleados que viven en puntarenas o alajuela

select *
from empleado
where provincia IN ('Puntarenas', 'Alajuela')

-- listar los empleados que no vivan en puntarenas o alajuela

select *
from empleado
where provincia NOT IN ('Puntarenas','Alajuela')

--Listar los empleados cuyo nombre inicie con la letra j

select *
from empleado
where nombre like 'j%';

--listar los empleados que tengan la U en la segunda posicion

select *
from empleado
where nombre like '_u%';

-- listar los empleados que no vivan en Puntarenas

select *
from empleado
where provincia <> 'Puntarenas';

--mostrar los empleados que ganan mas de 200 colones

select *
from empleado
where salario > 100;

--operadores: > < <> = 
--se compara contra un unico valor
-- por lo tanto esto noes posible:
select *
from empleado
where salario=(100,200) -- da error

-- En sql
-- where campo - valor, constante, select


-- mostrar los empleados que viven en la misma provincia que vive juan
select *
from empleados
where provincia = 'Puntarenas' -- no lo hagan asi

-- seria asi:

select *
from empleado
where provincia = (select provincia from empleado where nombre = 'juan');

--ojo si se usa el = el subselect debe retornar un solo valor

-- probemos el error
select *
from empleado
where provincia = (select provincia from empleado);

--igual daria error asi:
select *
from empleado
where provincia = (select * from empleado where nombre = 'juan');

-- mostrar el nombre del empleado que gana mas
select nombre
from empleado
where salario = (select max(salario) from empleado);

--el sexo es una mentira eso no existe

--Error comun que comenten

select nombre
from empleado
where salario = max(salario);
--Nota: No se pueden usar funciones de agrupamiento directamente en el where por eso esto da error, pero si se puede dentro de un subselect si se puede!


-- listar los empleados que vivane en el mismo departamento de juan

select *
from empleado
where idDepartamento = (select idDepartamento from empleado where nombre = 'juan');

--listar los empleados que vivan en el mismo departamento de juan pero no muestren a juan
select *
from empleado
where idDepartamento = (select idDepartamento from empleado where nombre = 'juan' and nombre <> 'juan');

