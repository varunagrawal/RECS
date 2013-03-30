#!/usr/bin/python

import MySQLdb as mdb
import RankClassifierModule as rcm

def readDb():
	
	con = mdb.connect("localhost", "root", "ion", "RankClassifier")

	cur = con.cursor()

	dept = rcm.branch("Electronics Engineering")

	cur.execute("Select rank from Students where dept=%d and year=2010 order by rank asc;" % dept)

	data = cur.fetchall()

	return data



data = readDb()

f = open("cluster.txt", "w")

for d in data:
	f.write("%d\n" % d[0])

