from flask import Flask, render_template, request, redirect, session, url_for

from db.db_connection import create_database
from models.user import User

app = Flask(__name__)      # define app

app.secret_key = b'_5#y2L"F4Q8z\n\xec)'


@app.route('/', methods=["GET"])    # renderizare template
def home():
    return render_template("home.html", user=session.get("user", False))


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "GET":                  # check method
        return render_template("login.html")     # next steps logic of POST method
    user_data = dict(request.form)   # => dictionary with info, from form

    # {"email": "client@gmail.com", "password":"123"}
    # user_obj = User(email=user_data["email"], password=user_data["password"])

    try:                            # User(email="client@gmail.com", password="123")
        user_obj = User(**user_data)
        user_obj.check_in_db()
        session["user"] = user_obj.email
    except Exception as e:
        return render_template("login.html", error=f"{e}")
    # print(user_data)
    # logic processing of a date comes from form
    # interactive with business layer with users class
    return redirect('/bio.html')


# @app.route("/logout", method=['GET'])
# def logout():
#     session.pop("user", None)
#     return redirect('/')


# @app.route("/users", method=['GET'])
# def get_all_users():
#     pass


# @app.route("/users/<user_id>", method=['GET'])
# def get_user_by_id():
#     pass

@app.route("/bio", methods=['GET'])
def bio():
    return render_template("bio.html")


@app.route("/media", methods=['GET'])
def media():
    return render_template("media.html")


@app.route("/sport", methods=['GET'])
def sport():
    return render_template("sport.html")


@app.route("/users/add", methods=["GET", "POST"])
def add_user():
    if request.method == "GET":
        return render_template('sign_up.html')
    user_data = dict(request.form)
    try:
        user_obj = User(**user_data)
        user_obj.add()
    except Exception as e:
        return render_template('sign_up.html', error=f'{e}')
    return redirect("/")


@app.route("/users/update/<user_id>", methods=["PUT", "PATCH"])
def update_user(user_id):
    pass


@app.route("/users/delete/<user_id>", methods=["DELETE"])
def delete_user(user_id):
    pass


# @app.route('/demo', methods=['GET'])
# def demo():
#     render_template('demo.html')


if __name__ == '__main__':
    create_database()
    app.run(debug=True, port=7000)


