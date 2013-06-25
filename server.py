from flask import Flask, render_template, session, redirect, url_for, abort, request, flash, send_from_directory

app = Flask(__name__)


@app.route("/", methods=['GET'])
def route_base():
	return render_template("home.html")

if __name__ == "__main__":
	app.debug = True
	app.run()