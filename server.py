from flask import Flask, render_template

app = Flask(__name__)


@app.route("/1", methods=['GET'])
def route_1():
	return render_template("1.html")

@app.route('/2', methods=['GET'])
def route_2():
	return render_template("2.html")

@app.route('/3', methods=['GET'])
def rotue_3():
	return render_template("3.html")

@app.route('/4', methods=['GET'])
def route_4():
	return render_template("4.html")

if __name__ == "__main__":
	app.debug = True
	app.run()