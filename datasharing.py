from flask import Flask, render_template, request, make_response, jsonify, url_for
from SNAPS import SNAPSfileGen
from ACISA_locations import RetrieveACISA
from CommentSection import commentInsertion


app = Flask(__name__, static_folder = 'static', static_url_path = '')


#Main website index page.
@app.route('/')
def hello_world():
	return render_template('index.html', ACISAList = RetrieveACISA())


#This function prepares the organized CSV File. It calls the SNAPSfileGen() function.
@app.route('/report')
def generate_large_csv():
	acisa = request.args.get('acisa', None, type = str)
	TimeString = request.args.get('TRange', 'Nothing', type = str)
	LaneDir = request.args.get('LDir', None, type = str)

	#get the CSV formatted plain text from SNAPSfileGen()
	response = make_response(SNAPSfileGen(TimeString, ACISA = acisa, laneDir = LaneDir))
	#send the data to browser.
	response.headers["Content-Disposition"] = 'attachment; filename="report.csv"'
	return response


#Retrieve ACISA list from the database
@app.route('/_add_numbers')
def add_numbers():
	return jsonify(result = RetrieveACISA())


#Abandoned function
@app.route('/goRequest', methods = ['POST'])
def goRequest():
	name = request.form['uname']
	agency = request.form['uagen']
	comment = request.form['ucomment']
	#commentInsertion(name, agency, comment)
	return "OK"


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 4567, debug = True)