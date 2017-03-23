DROP TABLE Influences;
DROP TABLE Gene;
DROP TABLE Protein;

CREATE TABLE Gene(
	gid int,
	name char(30), 
	PRIMARY KEY(gid)
);

CREATE TABLE Protein(
	pid int,
	name char(30),
	type char(30),
	PRIMARY KEY(pid)
);

CREATE TABLE Influences(
	gid int REFERENCES Gene(gid),
	pid int REFERENCES Protein(pid),
	PRIMARY KEY(gid, pid)
);

INSERT INTO Gene VALUES(1, 'gennavn1');
INSERT INTO Gene VALUES(2, 'gennavn2');
INSERT INTO Gene VALUES(3, 'gennavn3');
INSERT INTO Gene VALUES(4, 'gennavn4');
INSERT INTO Gene VALUES(5, 'gennavn5');
INSERT INTO Gene VALUES(6, 'gennavn6');
INSERT INTO Gene VALUES(7, 'gennavn7');
INSERT INTO Gene VALUES(8, 'gennavn8');
INSERT INTO Gene VALUES(9, 'gennavn9');
INSERT INTO Gene VALUES(10, 'gennavn10');
INSERT INTO Gene VALUES(11, 'gennavn11');
INSERT INTO Gene VALUES(12, 'gennavn12');
INSERT INTO Gene VALUES(13, 'gennavn13');
INSERT INTO Gene VALUES(14, 'gennavn14');
INSERT INTO Gene VALUES(15, 'gennavn15');
INSERT INTO Gene VALUES(16, 'gennavn16');
INSERT INTO Gene VALUES(17, 'gennavn17');
INSERT INTO Gene VALUES(18, 'gennavn18');
INSERT INTO Gene VALUES(19, 'gennavn19');
INSERT INTO Gene VALUES(20, 'gennavn20');
INSERT INTO Gene VALUES(21, 'gennavn21');
INSERT INTO Gene VALUES(22, 'gennavn22');
INSERT INTO Gene VALUES(23, 'gennavn23');
INSERT INTO Gene VALUES(24, 'gennavn24');
INSERT INTO Gene VALUES(25, 'gennavn25');
INSERT INTO Gene VALUES(26, 'gennavn26');
INSERT INTO Gene VALUES(27, 'gennavn27');
INSERT INTO Gene VALUES(28, 'gennavn28');
INSERT INTO Gene VALUES(29, 'gennavn29');
INSERT INTO Gene VALUES(30, 'gennavn30');
INSERT INTO Gene VALUES(31, 'gennavn31');
INSERT INTO Gene VALUES(32, 'gennavn32');
INSERT INTO Gene VALUES(33, 'gennavn33');
INSERT INTO Gene VALUES(34, 'gennavn34');
INSERT INTO Gene VALUES(35, 'gennavn35');
INSERT INTO Gene VALUES(36, 'gennavn36');
INSERT INTO Gene VALUES(37, 'gennavn37');
INSERT INTO Gene VALUES(38, 'gennavn38');
INSERT INTO Gene VALUES(39, 'gennavn39');
INSERT INTO Gene VALUES(40, 'gennavn40');
INSERT INTO Gene VALUES(41, 'gennavn41');
INSERT INTO Gene VALUES(42, 'gennavn42');


INSERT INTO Gene VALUES(43, 'TP53');
INSERT INTO Gene VALUES(44, 'BC02');
INSERT INTO Gene VALUES(45, 'ABC2');


INSERT INTO Protein VALUES(1, 'protnavn1', 'membrane');
INSERT INTO Protein VALUES(2, 'protnavn2', 'fibrous');
INSERT INTO Protein VALUES(3, 'protnavn3', 'fibrous');
INSERT INTO Protein VALUES(4, 'protnavn4', 'membrane');
INSERT INTO Protein VALUES(5, 'protnavn5', 'membrane');
INSERT INTO Protein VALUES(6, 'protnavn6', 'fibrous');
INSERT INTO Protein VALUES(7, 'protnavn7', 'membrane');
INSERT INTO Protein VALUES(8, 'protnavn8', 'fibrous');
INSERT INTO Protein VALUES(9, 'protnavn9', 'membrane');
INSERT INTO Protein VALUES(10, 'protnavn10', 'membrane');
INSERT INTO Protein VALUES(11, 'protnavn11', 'membrane');
INSERT INTO Protein VALUES(12, 'protnavn12', 'fibrous');
INSERT INTO Protein VALUES(13, 'protnavn13', 'fibrous');
INSERT INTO Protein VALUES(14, 'protnavn14', 'membrane');
INSERT INTO Protein VALUES(15, 'protnavn15', 'membrane');
INSERT INTO Protein VALUES(16, 'protnavn16', 'fibrous');
INSERT INTO Protein VALUES(17, 'protnavn17', 'membrane');
INSERT INTO Protein VALUES(18, 'protnavn18', 'fibrous');
INSERT INTO Protein VALUES(19, 'protnavn19', 'membrane');
INSERT INTO Protein VALUES(20, 'protnavn20', 'membrane');
INSERT INTO Protein VALUES(21, 'protnavn21', 'membrane');
INSERT INTO Protein VALUES(22, 'protnavn22', 'fibrous');
INSERT INTO Protein VALUES(23, 'protnavn23', 'fibrous');
INSERT INTO Protein VALUES(24, 'protnavn24', 'membrane');
INSERT INTO Protein VALUES(25, 'protnavn25', 'membrane');
INSERT INTO Protein VALUES(26, 'protnavn26', 'fibrous');
INSERT INTO Protein VALUES(27, 'protnavn27', 'membrane');
INSERT INTO Protein VALUES(28, 'protnavn28', 'fibrous');
INSERT INTO Protein VALUES(29, 'protnavn29', 'membrane');
INSERT INTO Protein VALUES(30, 'protnavn30', 'membrane');
INSERT INTO Protein VALUES(31, 'protnavn31', 'membrane');
INSERT INTO Protein VALUES(32, 'protnavn32', 'fibrous');
INSERT INTO Protein VALUES(33, 'protnavn33', 'fibrous');
INSERT INTO Protein VALUES(34, 'protnavn34', 'membrane');
INSERT INTO Protein VALUES(35, 'protnavn35', 'membrane');
INSERT INTO Protein VALUES(36, 'protnavn36', 'fibrous');
INSERT INTO Protein VALUES(37, 'protnavn37', 'membrane');
INSERT INTO Protein VALUES(38, 'protnavn38', 'fibrous');
INSERT INTO Protein VALUES(39, 'protnavn39', 'membrane');
INSERT INTO Protein VALUES(40, 'protnavn40', 'membrane');
INSERT INTO Protein VALUES(41, 'protnavn41', 'membrane');
INSERT INTO Protein VALUES(42, 'protnavn42', 'membrane');
INSERT INTO Protein VALUES(43, 'protnavn43', 'membrane');
INSERT INTO Protein VALUES(44, 'protnavn44', 'membrane');

INSERT INTO Influences VALUES(43, 1);
INSERT INTO Influences VALUES(44, 2);
INSERT INTO Influences VALUES(43, 3);
INSERT INTO Influences VALUES(44, 4);
INSERT INTO Influences VALUES(45, 5);