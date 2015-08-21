SELECT count(*) FROM (
  	SELECT 	docid, 
		sum(count) as cnt 
	FROM frequency
	GROUP BY docid
	HAVING cnt > 300
	
);