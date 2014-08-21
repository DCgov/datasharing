__author__ = 'Kaiqun'

import os
import MySQLdb

def DBConnector():
	"""

	This function generates a Database connection object
	@return: a database connection
	"""
	MySQLInfo = open(os.path.dirname(os.path.realpath(__file__)) + '/Logins/MySQL', 'r').readline()
	db = MySQLdb.connect(
		host=MySQLInfo.split('|')[0],
		user=MySQLInfo.split('|')[1],
		passwd=MySQLInfo.split('|')[2],
		db=MySQLInfo.split('|')[3]
	)
	return db