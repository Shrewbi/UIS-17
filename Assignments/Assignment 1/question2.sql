CREATE TABLE studerende(
  id CHAR(6),
  name VARCHAR,
  birthday DATE,
  best_friend_id CHAR(6),
  PRIMARY KEY(id)
);

CREATE TABLE venner(
  studerende_id_1 CHAR(6) REFERENCES studerende(id),
  studerende_id_2 CHAR(6) REFERENCES studerende(id)
);

CREATE TABLE kurser(
  id INT,
  name VARCHAR,
  PRIMARY KEY(id)
);

CREATE TABLE tilmelding(
  studerende_id CHAR(6) REFERENCES studerende(id),
  kursus_id INT REFERENCES kurser(id),
  vurdering INT,
  karakter INT
 );

CREATE TABLE periode(
  year INT,
  block INT,
  semester BOOLEAN,
  PRIMARY KEY(year, block, semester)
);

CREATE TABLE udbud(
  kursus_id INT,
  year INT,
  block INT,
  semester BOOLEAN, /* Reserved for courses streching more than 2 blocks */
  udbudt BOOLEAN, /* Is the course offered? */
  FOREIGN KEY(kursus_id) REFERENCES kurser(id),
  FOREIGN KEY(year)      REFERENCES periode(year),
  FOREIGN KEY(block)     REFERENCES periode(block),
  FOREIGN KEY(semester)    REFERENCES periode(semester)
);

CREATE TABLE undervisere(
  email VARCHAR(100),
  name VARCHAR(100),
  PRIMARY KEY(email)
);

CREATE TABLE tilknyttet(
  kursus_id INT REFERENCES kurser(id),
  underviser_email VARCHAR(100) REFERENCES undervisere(email)
);

CREATE TABLE forelæsning(
  forelæsning_id INT,
  kursus_id INT REFERENCES kurser(id),
  ugenummer INT,
  ugedag INT, /* 1: mandag, 2: tirsdag, etc. */
  start_time TIME,
  end_time TIME
);

CREATE TABLE ansvarlig(
  underviser_email VARCHAR(100) REFERENCES undervisere(email),
  forelæsning_id INT REFERENCES forelæsning(forelæsning_id)
);
