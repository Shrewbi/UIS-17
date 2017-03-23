-- Question 1: SQL
--   Given schema:
--     Gene(gid, name)
--     Influences(gid, pid)
--     Protein(pid, name, type)

-- Task 1: List names of proteins of type "fibrous"

SELECT name
FROM protein
WHERE type = 'fibrous';

-- Task 2: List gene names that influence proteins of both type "membrane" and "fibrous"

WITH gp AS (
  SELECT
    g.gid
    , p.pid
    , g.name AS gene_name
    , p.name AS prot_name
    , p.type AS prot_type
  FROM gene g
  JOIN influences i ON g.gid = i.gid
  JOIN protein p ON i.pid = p.pid
)
(
  SELECT gene_name
  FROM gp
  WHERE prot_type = 'membrane'
)
INTERSECT
(
  SELECT gene_name
  FROM gp
  WHERE prot_type = 'fibrous'
)

-- Task 3: List names of proteins influenced by gene "TP53", but not gene "BCO2"

WITH gp AS (
  SELECT
    g.gid
    , p.pid
    , g.name AS gene_name
    , p.name AS prot_name
    , p.type AS prot_type
  FROM gene g
  JOIN influences i ON g.gid = i.gid
  JOIN protein p ON i.pid = p.pid
)
(
  SELECT prot_name
  FROM gp
  WHERE gene_name = 'TP53'
)
EXCEPT
(
  SELECT prot_name
  FROM gp
  WHERE gene_name = 'BCO2'
)

-- Task 4: List names of genes and protein counts that influence more than 42 proteins

SELECT
  g.name
  , COUNT(*) AS protein_count
FROM gene g
JOIN influences i ON g.gid = i.gid
GROUP BY g.name
HAVING COUNT(*) > 42

-- Task 5: List pairs of proteins that influence precisely the same genes

WITH genes_for_prot AS (
  SELECT pid, COUNT(*)
  FROM influences
  GROUP BY pid
)
SELECT i1.pid, i2.pid
FROM influences i1
JOIN influences i2 ON i1.gid = i2.gid
WHERE i1.pid != i2.pid
GROUP BY i1.pid, i2.pid
HAVING (i1.pid, COUNT(*)) IN genes_for_prot
  AND (i2.pid, COUNT(*)) IN genes_for_prot
