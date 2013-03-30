DELIMITER $$

DROP PROCEDURE IF EXISTS kNN;

CREATE PROCEDURE kNN()
BEGIN

	DECLARE k INT;
	DECLARE g INT;

	SET k = 7;
	SET g = 21;
	
	(SELECT C.rank, C.dept, C.institute FROM
		(	
			(SELECT *  FROM Students, 
				(SELECT Students.point AS pt FROM Students, Query
				WHERE Students.point >= Query.point
				ORDER BY Students.point ASC
				LIMIT 1
				) T1
			WHERE Students.point >= T1.pt
			ORDER BY Students.point ASC
			LIMIT g							
			) 

			UNION
		
			(SELECT *  FROM Students, 
				(SELECT Students.point AS pt FROM Students, Query
				WHERE Students.point <= Query.point
				ORDER BY Students.point DESC			
				LIMIT 1
				) T2
			WHERE Students.point < T2.pt
			ORDER BY Students.point DESC 
			LIMIT g								
			)

		) AS C, Query
	ORDER BY euclidean(Query.rank, Query.dept, Query.institute, C.rank, C.dept, C.institute) 
	LIMIT k
	)

	UNION 
	
	(SELECT rank, dept, institute FROM ans
	);

END

$$

DELIMITER ;


/*
	
 	(SELECT C.rank, C.dept, C.institute FROM
		(	
			(SELECT *  FROM Students, 
				(SELECT Students.point AS pt FROM Students, Query
				WHERE Students.point >= Query.point
				ORDER BY Students.point ASC
				LIMIT 1
				) T1
			WHERE Students.point >= T1.pt
			ORDER BY Students.point ASC
			LIMIT 30						
			) 

			UNION
		
			(SELECT *  FROM Students, 
				(SELECT Students.point AS pt FROM Students, Query
				WHERE Students.point <= Query.point
				ORDER BY Students.point DESC			
				LIMIT 1
				) T2
			WHERE Students.point < T2.pt
			ORDER BY Students.point DESC 
			LIMIT 30						
			)

		) AS C, Query
	ORDER BY euclidean(Query.rank, Query.dept, Query.institute, C.rank, C.dept, C.institute) 
	LIMIT 10 
	)

	UNION 
	
	(SELECT ans.rank, ans.dept, ans.institute FROM ans
	);


*/

