CREATE TABLE studerende(
  id             CHAR(6),
  name           VARCHAR,
  birthday       DATE,
  best_friend_id CHAR(6) REFERENCES studerende(id),
  PRIMARY KEY (id)
);

CREATE TABLE venner(
  studerende_id_1 CHAR(6) REFERENCES studerende(id),
  studerende_id_2 CHAR(6) REFERENCES studerende(id),
  PRIMARY KEY (studerende_id_1, studerende_id_2)
);

CREATE TABLE kurser(
  id   INT,
  name VARCHAR,
  PRIMARY KEY (id)
);

CREATE TABLE tilmelding(
  studerende_id CHAR(6) REFERENCES studerende(id),
  kursus_id     INT REFERENCES kurser(id),
  vurdering     INT,
  karakter      INT,
  PRIMARY KEY (studerende_id, kursus_id)
 );

CREATE TABLE periode(
  year     INT,
  block    INT,
  semester BOOLEAN, /* For courses streching two blocks */
  PRIMARY KEY (year, block, semester)
);

CREATE TABLE udbud(
  kursus_id INT REFERENCES kurser(id),
  year      INT,
  block     INT,
  semester  BOOLEAN,
  FOREIGN KEY (year, block, semester)
    REFERENCES periode(year, block, semester),
  PRIMARY KEY (kursus_id, year, block, semester)
);

CREATE TABLE undervisere(
  email VARCHAR(100),
  name  VARCHAR(100),
  PRIMARY KEY (email)
);

CREATE TABLE tilknyttet(
  kursus_id        INT REFERENCES kurser(id),
  underviser_email VARCHAR(100) REFERENCES undervisere(email),
  PRIMARY KEY (kursus_id, underviser_email)
);

CREATE TABLE forelæsning(
  forelæsning_id  INT,
  kursus_id       INT REFERENCES kurser(id),
  ansvarlig_email VARCHAR(100) REFERENCES undervisere(email),
  ugenummer       INT, /* ISO 8601 */
  ugedag          INT, /* Mon = 1, Tue = 2, ... */
  start_time      TIME,
  end_time        TIME,
  PRIMARY KEY (forelæsning_id)
);
