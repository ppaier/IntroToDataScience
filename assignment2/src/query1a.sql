SELECT count(*) FROM (
  SELECT term FROM frequency
  WHERE docid = "10398_txt_earn" and count = 1
);