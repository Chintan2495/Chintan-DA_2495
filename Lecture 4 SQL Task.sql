create database student;

use student;

CREATE TABLE students (
  id INT PRIMARY KEY,
  name VARCHAR(50),
  course VARCHAR(20),
  marks INT
);

INSERT INTO students VALUES
(1, 'Aman', 'BCA', 75),
(2, 'Neha', 'MCA', 90),
(3, 'Karan', 'BCA', 65),
(4, 'Riya', 'BBA', 80),
(5, 'Meena', 'MCA', 88);

SELECT * FROM students;

SELECT COUNT(*) FROM students;

SELECT MAX(marks) as highest_marks,
min(marks) as lowest_marks
FROM students;

select course,
sum(marks) as total_marks
from students
group by course;

select course,
avg(marks) as average_marks
from students
group by course;

select course,
avg(marks) as average_marks
from students
group by course
having avg(marks) > 80;

SELECT name, marks
FROM students
ORDER BY marks DESC
LIMIT 3;

SELECT * FROM students
WHERE course IN ('BCA', 'MCA')
AND marks BETWEEN 60 AND 90;

SELECT * FROM students
WHERE course IN ('BCA', 'MCA');

SELECT count(Distinct course) as total_unique_course
from students;


SELECT * FROM students
WHERE name LIKE 'N%';














