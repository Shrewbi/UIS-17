CREATE TABLE studerende(
  id CHAR(6),
  name VARCHAR,
  birthday DATE,
  best_friend_id CHAR(6)
);

CREATE TABLE venner(
  studerende_id_1 CHAR(6),
  studerende_id_2 CHAR(6)
);

CREATE TABLE kurser(
  id INT,
  name VARCHAR
);

CREATE TABLE tilmelding(
  studerende_id CHAR(6),
  kursus_id INT,
  vurdering INT,
  karakter CHAR
);

CREATE TABLE periode(
  id INT,
  year INT,
  block INT
);

CREATE TABLE udbud(
  kursus_id INT,
  periode_id INT
);

CREATE TABLE undervisere(
  id INT,
  email VARCHAR,
  name VARCHAR
);

CREATE TABLE tilknyttet(
  kursus_id INT,
  underviser_id INT
);

CREATE TABLE forelæsning(
  kursus_id INT,
  ugenummer INT,
  uge INT,
  start_time TIME,
  end_time TIME
);

CREATE TABLE ansvarlig(
  underviser_id INT,
  forelæsning_id INT
);
