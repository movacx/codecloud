create database dept
use dept;

USE curso;

CREATE TABLE dept(
    deptno INT NOT NULL,
    dname CHAR(10) NOT NULL,
    loc CHAR(8) NOT NULL,
    PRIMARY KEY(deptno)
);

CREATE TABLE emp(
    eno INT NOT NULL,
    ename CHAR(6) NOT NULL,
    job CHAR(9) NOT NULL,
    mgr INT NULL,
    hiredate DATE NOT NULL,
    sal INT NOT NULL,
    comm INT NULL,
    deptno INT NOT NULL,
    PRIMARY KEY(eno)
);

ALTER TABLE emp
ADD FOREIGN KEY (deptno)
REFERENCES dept(deptno);

ALTER TABLE emp
ADD FOREIGN KEY (mgr)
REFERENCES emp(eno);

--insetar departamentos
INSERT INTO dept(deptno, dname, loc) 
VALUES (10, 'ACCOUNTING', 'NEW YORK');


INSERT INTO dept(deptno, dname, loc) 
VALUES (20, 'RESEARCH',  'DALLAS');

INSERT INTO dept(deptno, dname, loc) 
VALUES (30, 'SALES',     'CHICAGO');

INSERT INTO dept(deptno, dname, loc) 
VALUES (40, 'OPERATIONS','BOSTON');


INSERT INTO emp(eno, ename, job, mgr, hiredate, sal, comm, deptno) VALUES
(7369, 'SMITH',  'CLERK',    7902, '1980-12-17',  800, NULL, 20),
(7499, 'ALLEN',  'SALESMAN', 7698, '1981-02-20', 1600,  300, 30),
(7521, 'WARD',   'SALESMAN', 7698, '1981-02-22', 1250,  500, 30),
(7566, 'JONES',  'MANAGER',  7839, '1981-04-02', 2975, NULL, 20),
(7654, 'MARTIN', 'SALESMAN', 7698, '1981-09-28', 1250, 1400, 30),
(7698, 'BLAKE',  'MANAGER',  7839, '1981-05-01', 2850, NULL, 30),
(7782, 'CLARK',  'MANAGER',  7839, '1981-06-09', 2450, NULL, 10),
(7788, 'SCOTT',  'ANALYST',  7566, '1982-12-09', 3000, NULL, 20),
(7839, 'KING',   'PRESIDENT',NULL, '1981-11-17', 5000, NULL, 10),
(7844, 'TURNER', 'SALESMAN', 7698, '1981-09-08', 1500,    0, 30),
(7876, 'ADAMS',  'CLERK',    7788, '1983-01-12', 1100, NULL, 20),
(7900, 'JAMES',  'CLERK',    7698, '1981-12-03',  950, NULL, 30),
(7902, 'FORD',   'ANALYST',  7566, '1981-12-03', 3000, NULL, 20),
(7934, 'MILLER', 'CLERK',    7782, '1982-01-23', 1300, NULL, 10);

--1. Seleccionar toda la tabla de departamento 
select * from dept;
--2. Seleccionar toda la tabla de empleados
select * from emp;

--3. Seleccionar aquellos empleados que sean 'salesman'
select emp
