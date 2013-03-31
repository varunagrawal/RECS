#!/usr/bin/python

import MySQLdb as mdb
import sys
import RankClassifierModule as RCM


try:

	# Create the Database connection
	con = mdb.connect("localhost", "root", "ion", "RankClassifier")
	cur = con.cursor()

	# Get Inputs
	rank = int(raw_input("Please enter your rank: "))
	branch = RCM.branch(raw_input("Please input your desired branch if any[default None]: "))
	insti = 1	# Get this input if more than one institute

	# Get the Z value of the input
	point = RCM.getZValue(rank, branch, insti)

	# Insert values into input table
	cur.execute("INSERT INTO Query values (%d, %d, %d, %d, 2012);" % (point, rank, branch, insti))

	# Commit the transaction
	con.commit()

	# The kNN query statement
	statement = """
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
					WHERE Students.point < Query.point
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
	
"""
	
	# Execute the kNN query
	cur.execute(statement)

	# The the answer tuples
	ans = cur.fetchall()

	#print ans
	for i in ans:
		print i
	
	# Clear the input values
	cur.execute("DELETE FROM Query");
	con.commit()

except mdb.Error, e:
	print e.args[0], e.args[1]

finally:
	if con:
		con.close()
	
