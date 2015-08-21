-- CREATE VIEW frequency_query AS
-- SELECT * FROM frequency
-- UNION
-- SELECT 'q' as docid, 'washington' as term, 1 as count 
-- UNION
-- SELECT 'q' as docid, 'taxes' as term, 1 as count
-- UNION 
-- SELECT 'q' as docid, 'treasury' as term, 1 as count;

SELECT r, SUM(s) as score FROM(
SELECT r,c, c1*c2 as s FROM (SELECT term, count as c1, docid as r FROM frequency_query) as D1
INNER JOIN ( SELECT term, count as c2, docid as c FROM frequency_query WHERE c="q") as D2
on D1.term = D2.term)
GROUP BY r,c;