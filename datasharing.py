from flask import Flask, render_template, request, make_response, jsonify, url_for
from SNAPS import SNAPSfileGen
from ACISA_locations import RetrieveACISA
from CommentSection import commentInsertion


app = Flask(__name__, static_folder = 'static', static_url_path = '')


@app.route('/')
def hello_world():
	return render_template('index.html', ACISAList = RetrieveACISA())


@app.route('/report')
def generate_large_csv():
	acisa = request.args.get('acisa', None, type = str)
	TimeString = request.args.get('TRange', 'Nothing', type = str)
	LaneDir = request.args.get('LDir', None, type = str)
	response = make_response(SNAPSfileGen(TimeString, ACISA = acisa, laneDir = LaneDir))
	response.headers["Content-Disposition"] = 'attachment; filename="report.csv"'
	return response


@app.route('/_add_numbers')
def add_numbers():
	return jsonify(result = RetrieveACISA())


@app.route('/goRequest', methods = ['POST'])
def goRequest():
	name = request.form['uname']
	agency = request.form['uagen']
	comment = request.form['ucomment']
	#commentInsertion(name, agency, comment)
	return "OK"


if __name__ == '__main__':
	app.run(host = '0.0.0.0', port = 4567, debug = True)