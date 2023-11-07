from flask import Flask, render_template, request

from db.db_connection import create_database

app = Flask(__name__)


@app.route('/', methods=["GET"])    # renderizare template
def home():
    return render_template("home.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":                  # check method
        return render_template("login.html")
    # next steps logic of POST method


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=7001)


