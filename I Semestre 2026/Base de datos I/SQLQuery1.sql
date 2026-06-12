use curso;
select * from empleado;

CREATE TABLE departamento(
	idDepartamento int, 
	nombre varchar(20),
	PRIMARY KEY(idDepartamento));

INSERT INTO departamento VALUES (1,'Informatica');
INSERT INTO departamento VALUES (2,'Compras');
INSERT INTO departamento VALUES (3,'RH');

select * from departamento;

select * from empleado;

-- sin integridad referencial
insert into empleado(idEmpleado, nombre, salario, provincia, idDepartamento)
values(5, 'prueba sin IR', 100, 'Puntarenas', 10);

-- lo inserta porque no se ha levantado la integridad referencial
-- lo cual no deberia pasar
-- siempre debe estar arriba la integridad referencial

-- vamos a borrarlo
-- para borrar un registro se utiliza el comando DELETE

DELETE from empleado
where idEmpleado=6;


-- levantar la integridad referencial
-- se coloca en la tabla hija

alter table Empleado add foreign key(idDepartamento)
references Departamento(idDepartamento)

insert into empleado(idEmpleado, nombre, salario,provincia,idDepartamento)
values(6,'prueba sin ir',100,'Puntarenas',10)

--grupo by
--agrupar registros
--se agrupan por campos repetidos
select * from empleado;

--mostrar la cantidad de empelados que existen

select count(*) from empleado;

-- mostarr la cantidad de empleados por provincia

select provincia, count(*)
from empleado
group by provincia;

-- mostrar cuantos empleados ganan mas de 100 colones en cada provincia
select provincia, count(*)
from empleado
where salario>100
group by provincia;


select provincia, idDepartamento, count(*)
from empleado
group by provincia, idDepartamento
order by provincia;

-- mostrar el salario maximo por departamento
select nombre, max(salario)
from empleado
group by nombre;
order by nombre;

--no se agrupo
--no tiene sentido

-- esto da error
selec idDepartamento, count(*)
from empleado;


--Esto si funciona
select count(*)
from empleado;

--having 

--having es el where del group by se aplica luego de agrupar
-- mostrar los departamentos que tengan mas de un empleado

select idDepartamento, count(*)
from empleado
group by idDepartamento;
having count(*)>2;

-- en el having si se puede usar funciones de agrupamiento en el where no

-- FULL JOIN
--Producto cartesiano
--muy peligroso
--es relacionar todos los datos de una tabla contra todos los datos de otra tabla

select *
from empleado e, departamento d;
order by e.nombre;