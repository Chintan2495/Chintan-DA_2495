create database  krishnadb;

use krishnadb;

select * from sales_data;



CREATE TABLE Patients (
    PatientID INT PRIMARY KEY,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    Gender CHAR(1),
    DateOfBirth DATE,
    Phone VARCHAR(15),
    Address VARCHAR(200)
);

INSERT INTO Patients VALUES
(1, 'Rahul', 'Sharma', 'M', '1990-05-15', '9876543210', 'Ahmedabad'),
(2, 'Priya', 'Patel', 'F', '1995-08-20', '9876543211', 'Surat'),
(3, 'Amit', 'Verma', 'M', '1988-12-10', '9876543212', 'Vadodara'),
(4, 'Neha', 'Shah', 'F', '1992-03-25', '9876543213', 'Rajkot'),
(5, 'Karan', 'Joshi', 'M', '1985-11-18', '9876543214', 'Ahmedabad');

select * from patients;




 
 


