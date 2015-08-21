SELECT SUM(s) FROM(
SELECT r,c, c1*c2 as s FROM (SELECT term, count as c1, docid as r FROM frequency WHERE r = "10080_txt_crude") as D1
INNER JOIN ( SELECT term, count as c2, docid as c FROM frequency WHERE c="17035_txt_earn") as D2
on D1.term = D2.term)
WHERE r < c
GROUP BY r,c;