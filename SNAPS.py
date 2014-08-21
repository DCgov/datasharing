__author__ = 'Kaiqun'

from datetime import datetime
from DatabaseConn import DBConnector

def SNAPSfileGen(TimeRange, ACISA=None, laneDir=None, laneNum=None):
	"""

	@param TimeRange: Time range, represented by the format: '%m/%d/%Y %I:%M %p - %m/%d/%Y %I:%M %p'
	@param ACISA: A list of ACISAs
	@param laneDir: lane directions
	@param laneNum: lane number
	@return: a CSV formatted plain text
	"""
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