__author__ = 'Kaiqun'

from DatabaseConn import DBConnector

def RetrieveACISA():
	db = DBConnector()
	cur = db.cursor()

	SQLcmd = "SELECT * FROM snaps.SNAPsLocation"
	cur.execute(SQLcmd)
	returnList = []
	count = 0
	for item in cur.fetchall():
		count += 1
		tmplist = [item[1], item[2], count, str(item[0])]
		returnList.append(tmplist)
	return returnList