#!/usr/bin/python

import MySQLdb as mdb
import sys
import RankClassifierModule as RCM


try:
	#Open the Dataset file
	f = open('Dataset.csv')

	#Read all the lines in the file
	data = f.readlines()

	#Connect to database and create cursor
	con = mdb.connect("localhost", "root", "ion", "RankClassifier")
	cur = con.cursor()


	#For all the data entries, get the corresponding values and put in database
	for i in range(len(data)):
		tup = data[i].split(',')
                
		dept = RCM.branch(tup[3])		#Store numerical value of branch
		insti = RCM.institute("")		#Store numerical value of institute

		#Get the Z value for the values passed
		z = RCM.getZValue(int(tup[1]), dept, insti)

		#Insert values into Students database
		cur.execute("Insert into Students values (%d, %d, %d, %d, %d)" % (z, int(tup[1]), dept, insti, int(tup[2])))
		
	
	#cur.execute("Select * from Students")
	#values = cur.fetchall()
	
	#print len(values)
	#for i in range(5):
	#	print values[i]
	
	con.commit()
	cur.close()

except mdb.Error, e:
	print e.args[0], e.args[1]

finally:
	if con:
		con.close()


