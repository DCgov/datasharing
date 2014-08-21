__author__ = 'Kaiqun'

from DatabaseConn import DBConnector
from datetime import datetime

def commentInsertion(name, agency, comment):
	"""

	@param name: inputted user name
	@param agency: user agency
	@param comment: user generated comments
	"""
	db = DBConnector()
	cur = db.cursor()
	nowtime = datetime.now()

	Values = "'" + str(name) + "', '" + str(agency) + "', '" + str(comment) + "', '" + str(nowtime) + "'"

	#insertion SQL command
	SQLcmd = "INSERT INTO snaps.user_comments (userName, userAgen, userComment, cmtDatetime) VALUES (" + Values + ")"

	#execute and commit
	cur.execute(SQLcmd)
	db.commit()