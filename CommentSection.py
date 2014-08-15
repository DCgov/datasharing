__author__ = 'Kaiqun'

from DatabaseConn import DBConnector
from datetime import datetime

def commentInsertion(name, agency, comment):
	db = DBConnector()
	cur = db.cursor()
	nowtime = datetime.now()

	Values = "'" + str(name) + "', '" + str(agency) + "', '" + str(comment) + "', '" + str(nowtime) + "'"
	SQLcmd = "INSERT INTO snaps.user_comments (userName, userAgen, userComment, cmtDatetime) VALUES (" + Values + ")"

	cur.execute(SQLcmd)
	db.commit()