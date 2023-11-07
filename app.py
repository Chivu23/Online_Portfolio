from flask import Flask, render_template, request, redirect, session

from db.db_connection import create_database
from models.user import User

app = Flask(__name__)


@app.route('/', methods=["GET"])    # renderizare template
def home():
    return render_template("home.html", user=session.get("user", False))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":                  # check method
        return render_template("login.html")
    # next steps logic of POST method
    user_data = dict(request.form)   # => dictionary with info, from form
    # user_obj = User(email=user_data["email"], password=user_data["password"])
    try:
        user_obj = User(**user_data)
        user_obj.check_in_db()
    except Exception as e:
        return render_template("login.html", error=f"{e}")
    print("+++++++++++++++++++++")
    print(user_data)
    # logic processing of a date comes from form
    # interactive with business layer with users class
    return redirect('/bio.html')


@app.route('/home', methods=['GET'])
def get_home_page():
    return render_template('bio.html')


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=7001)


