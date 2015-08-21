SELECT r,c, sum(v) FROM(
SELECT r,c, v1*v2 as v FROM(
SELECT * FROM (SELECT col_num, value as v1, row_num as r FROM A WHERE r=2) as A2
INNER JOIN ( SELECT row_num, value as v2, col_num as c FROM B WHERE c=3) as B3
on A2.col_num = B3.row_num
))
GROUP BY r,c;