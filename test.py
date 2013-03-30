#!/usr/bin/python

import MySQLdb as mdb

def transfer():
	try:
		con = mdb.connect("localhost", "root", "ion", "RankClassifier")

		cur = con.cursor()

		cur.execute("create table Test(point integer, rank integer, dept integer, institute integer, year integer);")

                transferQuery = """insert into Test (point, rank, dept, institute, year) 
				select S.point, S.rank, S.dept, S.institute, S.year 
				from Students as S where year = 2011;"""
                
                cur.execute(transferQuery)
		#cur.execute("insert into Test values (point, rank, dept, institute, year) select * from Students where year = 2011;")
		cur.execute("delete from Students where year = 2011;")
		
		
		con.commit()

	except mdb.Error, e:
		print e
	finally:
		con.close()


def run(con, cur, point, rank, branch, insti, year):

	cur.execute("INSERT INTO Query values (%d, %d, %d, %d, %d);" % (point, rank, branch, insti, year))

	con.commit()

	statement = """
		(SELECT C.point, C.rank, C.dept, C.institute, C.year FROM
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

	cur.execute(statement)

	ans = cur.fetchall()

	cur.execute("DELETE FROM Query");
	con.commit()
	
	return ans


def test():
        #transfer()
	result = 0
	deviation = 0

	try:
		con = mdb.connect("localhost", "root", "ion", "RankClassifier")

		cur = con.cursor()
		
		cur.execute("SELECT * FROM Test;")
		testData = cur.fetchall()

		for d in testData: 

			ans = run(con, cur, d[0], d[1], d[2], d[3], d[4])
			
			minTemp = -1
			tempRes = ()

			for a in ans:
				if a[2] == d[2]:
					if minTemp < 0:
						minTemp = abs(d[1] - a[1])
						tempRes = a
					elif minTemp > abs(d[1] - a[1]):
						minTemp = abs(d[1] - a[1])
						tempRes = a
					
					result += 1
					
					#print d, a
					#break

			deviation += minTemp
			print d[1], minTemp

		print result*100.0/(len(testData)*10)
		print deviation/float(len(testData))

	except mdb.Error, e:
		print e
	finally:
		con.close()



test()


"""
try:
	con = mdb.connect("localhost", "root", "ion", "RankClassifier")
	cur = con.cursor()
	
	ans =  run(con, cur, 994198L, 23445, 4, 1, 2011)

	for a in ans:
		#print a
		if a[2] == 4:
			print a
			break

except mdb.Error, e:
	print e
finally:
	con.close()
"""
