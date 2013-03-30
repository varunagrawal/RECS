#!/usr/bin/python

import MySQLdb as mdb
import sys

def interweave(a, b, step=1):
	"""
	Interweaves the bits of binary strings a and b
	"""
	a = str(a)
	b = str(b)
	z = ''
	minLen = min(len(a), len(b))
	
	for i in range(minLen):
		for j in range(step):
			z = z + a[i+j]
		
		z = z + b[i]

	z = z + a[minLen:] + b[minLen:]
	
	return z


def getZValue(rank, dept=0, insti=0):
	"""
	Returns the Z value of the 3 parameters depending on which is passed
	"""

	rank = bin(rank)[2:]

	#if dept == -1 and insti == -1:
	#	return rank
	#elif dept == -1:
	#	insti = bin(insti)[2:]
	#
	#	z = interweave(rank, insti)
	#
	#elif insti == -1:
	#	dept = bin(dept)[2:]
	#
	#	z = interweave(rank, dept)
	#
	#else:
	#	dept = bin(dept)[2:]
	#	insti = bin(insti)[2:]
	#	
	#	z = interweave(rank, dept)
	#	z = interweave(z, insti, 2)
	
	dept = bin(dept)[2:]
	insti = bin(insti)[2:]

	z = interweave(rank, dept)
	z = interweave(z, insti, 2)

	return int(z, 2)


#Dictionary Mapping branches to numerical values. 
#Can be read from a file.
depts = {"None" : 0,
	 "Computer Engineering" : 1, 
	 "Electronics Engineering" : 2,
	 "Electrical Engineering" : 3,
	 "Mechanical Engineering" : 4,
	 "Chemical Engineering" : 5,
	 "Civil Engineering" : 6
	}


def institute( name ):
	"""
	Returns the numerical value of the name of the Institute passed.
	Currently 1 as only SVNIT is present.
	"""
	return 1



def branch( name ):
	"""
	Returns the numerical value of the branch name.
	"""
	return depts[name];

