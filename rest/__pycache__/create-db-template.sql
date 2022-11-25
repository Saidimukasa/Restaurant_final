-- Active: 1667978734897@@127.0.0.1@3306@school
CREATE DATABASE School;

-- Creating TABLE

CREATE TABLE Student (
SID VARCHAR(10) NOT NULL PRIMARY KEY,
SName VARCHAR(20) NOT NULL,
Age INT CHECK (Age >= 18),
Sex VARCHAR(1) check(Sex in ('M', 'F')),
Address VARCHAR(50) DEFAULT 'Mukono',
Course VARCHAR(10),
LID VARCHAR(10) NOT NULL,
CID VARCHAR(10),
-- PRIMARY KEY (SID),

);
-- DROP TABLE Student;
-- DROP DATABASE School;
-- DROP VIEW StudentView;
-- DROP PROCEDURE StudentProc;

-- ADDING FOREIGN KEY CONSTRAINTS IN STUDENT TABLE
ALTER TABLE Student 
ADD CONSTRAINT LID
FOREIGN KEY (LID) 
REFERENCES Lecturer(LID);

-- alter table Student
-- DROP FOREIGN KEY LID;

-- ALTER TABLE Student DROP FOREIGN KEY CID;




-- ALTER TABLE Student
-- -- DROP FOREIGN KEY LID;
-- -- Creating CID FOREIGN KEY CONSTRAINT
-- ALTER TABLE Student
-- ADD CONSTRAINT CID
-- FOREIGN KEY (CID)
-- REFERENCES Course(CID);

CREATE TABLE Lecturer(
LID VARCHAR(10) PRIMARY KEY NOT NULL,
Lname VARCHAR(10) NOT NULL,
Age INT CHECK(Age >=25),
PhoneNumber INT UNIQUE,
Address VARCHAR(50) DEFAULT 'Mukono',
CID VARCHAR(10)
);
ALTER TABLE Lecturer
ADD CONSTRAINT CID
FOREIGN KEY (CID)
REFERENCES Course(CID);

CREATE TABLE Course(
CID VARCHAR(10) PRIMARY KEY NOT NULL,
CName VARCHAR(10) NOT NULL,
LID VARCHAR(10) NOT NULL
);

-- ADDING FOREIGN KEY CONSTRAINTS IN COURSE TABLE
ALTER TABLE Course  
ADD CONSTRAINT LID
FOREIGN KEY (LID)
REFERENCES Lecturer(LID);


-- inserting Data into Student Table
INSERT INTO student VALUES('S001', 'John', 20, 'M', 'Mukono', 'C001', 'L001', 'C001');
INSERT INTO student VALUES('S002', 'Jane', 21, 'F', 'Mukono', 'C001', 'L001', 'C001');
INSERT INTO student VALUES('S003', 'James', 22, 'M', 'Mukono', 'C001', 'L001', 'C001'); 
INSERT INTO student VALUES('S004', 'Judy', 23, 'F', 'Mukono', 'C001', 'L001', 'C001');
INSERT INTO student VALUES('S005', 'Jude', 24, 'M', 'Mukono', 'C001', 'L001', 'C001');
INSERT INTO student VALUES('S006', 'Juma', 25, 'M', 'Mukono', 'C001', 'L001', 'C001');

-- Insert rows into table 'TableName'
-- Inserting Data into Lecturer Table
INSERT INTO Lecturer VALUES('L001', 'John Mark ', 30, 0777777771, 'Mukono', 'C001');
INSERT INTO Lecturer VALUES('L002', 'Jane Rose ', 31, 0777777772, 'Mukono', 'C001');
INSERT INTO Lecturer VALUES('L003', 'James Hanninngton', 32, 0777777773, 'Mukono', 'C001');
INSERT INTO Lecturer VALUES('L004', 'Judy Mark', 33, 0777777774, 'Mukono', 'C001');

-- Inserting Data into Course Table
INSERT INTO Course(CID) VALUES('C001', 'Computer Science', 'L001');
INSERT INTO Course VALUES('C002', 'Mathematics', 'L002');
INSERT INTO Course VALUES('C003', 'Physics', 'L003');

-- updating Data in Student Table
UPDATE Student 
SET SName = 'Mukasa Saidi',Age =25
WHERE SID = 'S001';

-- CALL ALLSTS();

SELECT SID,SName,student.Age,course.CID,CName,lecturer.LID,LName
FROM Student
RIGHT JOIN Course ON Student.CID = Course.CID
LEFT JOIN Lecturer ON Student.LID = Lecturer.LID;

SELECT COUNT(SID) AS 'Number of Students'
FROM Student;

