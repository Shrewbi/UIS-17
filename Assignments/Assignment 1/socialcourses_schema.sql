DROP TABLE STUDENTS;
DROP TABLE COURSES;
DROP TABLE PROFESSORS;
DROP TABLE LECTURES;

CREATE TABLE STUDENTS(kuid char(6), sname varchar(100), birthday date, PRIMARY KEY(kuid));
CREATE TABLE COURSES(cid char(30), cname varchar(100), periodes char(30), PRIMARY KEY(cid));
CREATE TABLE PROFESSORS(email char(255), pname varchar(100) PRIMARY KEY(email, pname));
CREATE TABLE LECTURES(Weekno int, weekday char(10), start_time char(5), end_time char(5));