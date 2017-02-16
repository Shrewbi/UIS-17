DROP TABLE IMG_BLNGS_TO;
DROP TABLE STONES;
DROP TABLE IMAGES;

CREATE TABLE STONES(id int, name varchar(50), lat float, long float, location varchar(50), PRIMARY KEY(id));
CREATE TABLE IMAGES(id int, path varchar(100), PRIMARY KEY(id));
CREATE TABLE IMG_BLNGS_TO(stoneid int REFERENCES STONES(id), imgid int REFERENCES IMAGES(id));