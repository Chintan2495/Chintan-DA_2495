create database analytics_db;

use analytics_db;

CREATE TABLE departments (
    department_id INT PRIMARY KEY,
    department_name VARCHAR(50)
);

CREATE TABLE employees (
    employee_id INT PRIMARY KEY,
    employee_name VARCHAR(50),
    department_id INT,
    FOREIGN KEY (department_id) REFERENCES departments(department_id)
);

INSERT INTO departments (department_id, department_name)
VALUES
(1, 'HR'),
(2, 'IT');

INSERT INTO employees (employee_id, employee_name, department_id)
VALUES
(101, 'Alice', 1),
(102, 'Bob', 2),
(103, 'Charlie', 2),
(104, 'David', NULL);

SELECT
    e.employee_name,
    d.department_name
FROM employees e
INNER JOIN departments d
    ON e.department_id = d.department_id;
    
    SELECT
    d.department_name,
    e.employee_name
FROM departments d
LEFT JOIN employees e
    ON d.department_id = e.department_id;
    
    SELECT
    e.employee_name,
    d.department_name
FROM departments d
RIGHT JOIN employees e
    ON d.department_id = e.department_id;
    
    SELECT
    e.employee_name,
    d.department_name
FROM employees e
LEFT JOIN departments d
    ON e.department_id = d.department_id

UNION

SELECT
    e.employee_name,
    d.department_name
FROM employees e
RIGHT JOIN departments d
    ON e.department_id = d.department_id;
    
    