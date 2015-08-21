SELECT count(*) FROM (
  	SELECT *
	FROM ( Select docid from frequency WHERE term="transactions") as t1 
	INNER JOIN ( Select docid from frequency WHERE term="world") as t2 
	on t1.docid = t2.docid
	
);