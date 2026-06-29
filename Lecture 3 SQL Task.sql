create database employidb;

use employidb;

CREATE TABLE employees (
    emp_id INT,
    emp_name VARCHAR(50),
    department VARCHAR(50),
    salary INT
);


INSERT INTO employees
VALUES
(1, 'Rohit', 'IT', 45000),
(2, 'Neha', 'HR', 60000),
(3, 'Arjun', 'IT', 70000),
(4, 'Simran', 'Finance', 55000),
(5, 'Rahul', 'HR', 40000);


select emp_name from employees;

select * from employees
where department = 'IT';

select * from employees
where salary > 50000;

select * from employees
where emp_name LIKE 'R%';

select * from employees
ORDER BY salary DESC;

SELECT DISTINCT department
FROM employees;

select * from employees
WHERE salary BETWEEN 30000 AND 60000;

SELECT *
FROM employees
WHERE salary >= 40000;

SELECT *
FROM employees
WHERE department = 'IT'
AND salary > 50000;

SELECT *
FROM employees
WHERE department = 'HR'
OR department = 'Finance';

SELECT *
FROM employees
WHERE NOT department = 'IT';

SELECT *
FROM employees
WHERE emp_name LIKE '%n';

SELECT *
FROM employees
WHERE emp_name LIKE '%a%';

SELECT *
FROM employees
ORDER BY salary ASC;

SELECT *
FROM employees
LIMIT 5;







