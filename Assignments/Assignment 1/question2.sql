CREATE TABLE students(
  kuid           CHAR(6),
  name           VARCHAR,
  birthday       DATE,
  best_friend_kuid CHAR(6) REFERENCES students(kuid),
  PRIMARY KEY (kuid)
);

CREATE TABLE friends(
  student_id_1 CHAR(6) REFERENCES students(kuid),
  student_id_2 CHAR(6) REFERENCES students(kuid),
  PRIMARY KEY (student_id_1, student_id_2)
);

CREATE TABLE courses(
  id   INT,
  name VARCHAR,
  PRIMARY KEY (id)
);

CREATE TABLE registration(
  student_id CHAR(6) REFERENCES students(kuid),
  course_id  INT REFERENCES kurser(id),
  year       INT,
  block      INT,
  semester   BOOLEAN,
  evaluation INT,
  grade      INT,
  FOREIGN KEY (course_id, year, block, semester) REFERENCES offered(course_id, year, block, semester),
  PRIMARY KEY (student_id, course_id)
 );

CREATE TABLE period(
  year     INT,
  block    INT,
  semester BOOLEAN, /* For courses streching two blocks */
  PRIMARY KEY (year, block, semester)
);

CREATE TABLE offered(
  course_id INT REFERENCES courses(id),
  year      INT,
  block     INT,
  semester  BOOLEAN,
  FOREIGN KEY (year, block, semester) REFERENCES period(year, block, semester),
  PRIMARY KEY (course_id, year, block, semester)
);

CREATE TABLE lecturers(
  email VARCHAR(100),
  name  VARCHAR(100),
  PRIMARY KEY (email)
);

CREATE TABLE associated(
  course_id        INT REFERENCES courses(id),
  lecturer_email VARCHAR(100) REFERENCES lecturers(email),
  PRIMARY KEY (course_id, lecturer_email)
);

CREATE TABLE lectures(
  lecture_id  INT,
  course_id   INT REFERENCES courses(id),
  responsible_email VARCHAR(100) REFERENCES lecturers(email),
  weekno      INT, /* ISO 8601 */
  Weekday     INT, /* Mon = 1, Tue = 2, ... */
  start_time  TIME,
  end_time    TIME,
  PRIMARY KEY (course_id)
);
