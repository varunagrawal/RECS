CREATE FUNCTION euclidean(query_rank INT, query_dept INT, query_institute INT, students_rank INT, students_dept INT, students_institute INT)
RETURNS INT	
	DECLARE ans INT;
	SET ans = ABS(query_rank - students_rank) + ABS(query_dept - students_dept) + ABS(query_institute - students_institute); 
RETURN ans;

