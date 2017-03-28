DROP TABLE IF EXISTS Field_blngs_to CASCADE;
DROP TABLE IF EXISTS Media_blngs_to CASCADE;
DROP TABLE IF EXISTS Field;
DROP TABLE IF EXISTS Item;
DROP TABLE IF EXISTS Media;

CREATE TABLE Field(id SERIAL PRIMARY KEY, title char(255), description char(2047), body char(2047));
CREATE TABLE Item(id SERIAL PRIMARY KEY, lat float NOT NULL, long float NOT NULL);
CREATE TABLE Field_blngs_to(iid int REFERENCES Item(id), fid int REFERENCES Field(id) ON DELETE CASCADE);
CREATE TABLE Media(id SERIAL PRIMARY KEY, type char(10) NOT NULL, path char(255) NOT NULL);
CREATE TABLE Media_blngs_to(mid int REFERENCES Media(id), fid int REFERENCES Field(id) ON DELETE CASCADE);


-- How strict are we? NOT NULL everything to prevent errors? Just the most important? nothing? --