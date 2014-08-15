__author__ = 'Kaiqun'

from datetime import datetime
from DatabaseConn import DBConnector

def SNAPSfileGen(TimeRange, ACISA=None, laneDir=None, laneNum=None):
	db = DBConnector()
	cur = db.cursor()

	StartTime = str(datetime.strptime(TimeRange.split(' - ')[0], '%m/%d/%Y %I:%M %p'))
	EndTime = str(datetime.strptime(TimeRange.split(' - ')[1], '%m/%d/%Y %I:%M %p'))

	tempfile = 'Time,ACISA,laneDir,laneNum,volume,occupancy,speed\n'
	if not ACISA and not laneDir and not laneNum:
		SQLcmd = "SELECT * FROM snaps.SNAPs_history WHERE Time > '" + StartTime + "' and Time < '" + EndTime + "'"
	elif ACISA:
		SQLcmd = "SELECT * FROM snaps.SNAPs_history WHERE Time > '" + StartTime + "' and Time < '" + EndTime + "'" + " and ACISA in (" + ACISA + ")"
	cur.execute(SQLcmd)
	tempfile += '\n'.join([','.join([str(every) for every in i]) for i in cur.fetchall()])
	return tempfile