from flask import Flask, redirect, url_for, render_template, request
import json
from pathlib import Path

app = Flask(__name__, template_folder=Path(__file__).resolve().parent)

@app.route("/")
def home():
    # call db
    # databasedata
    return render_template("home.html")
# , databasedata="data"

@app.route("/matches")
def matches():
    return render_template("matches.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/profile")
def profile():
    return render_template("profile.html")

@app.route("/messages")
def messages():
    return render_template("messages.html")

@app.route("/profileeditor", methods=["POST", "GET"])
def profileeditor():
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        data = {
            "name": request.form['nameInput'],
            "age": request.form['ageInput'],
            "gender": request.form['genderInput'],
            "orientation": request.form['orientationInput'],
            "major": request.form['majorInput'],
            "bio": request.form['bioInput'],
            "pfp": request.form['pfpInput']
        }


        try:
            with open("template/userData.json", 'r') as file:
                existing_data = json.loads(file.read())
                
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            existing_data = {
                "current":{

                },
                "users": [

                ]
            }
        existing_data["users"].append(data)
        existing_data["current"] = data
        with open('template/userData.json', 'w') as file:
            users = json.dumps(existing_data)
            file.write(users)


        return redirect(url_for('home'))

    return render_template("profileeditor.html")



@app.route("/register", methods=["POST", "GET"])
def register():
    if request.method == "POST":
        # import pdb; pdb.set_trace()
        data = {
            "email": request.form['emailInput'],
            "password": request.form['passwordInput'],
            "name": None,
            "age": None,
            "gender": None,
            "orientation": None,
            "major": None,
            "bio": None,
            "pfp": None
        }


        try:
            with open("template/userData.json", 'r') as file:
                existing_data = json.loads(file.read())
                
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            existing_data = {
                "current":{

                },
                "users": [

                ]
            }
        existing_data["users"].append(data)
        existing_data["current"] = data
        with open('template/userData.json', 'w') as file:
            users = json.dumps(existing_data)
            file.write(users)


        return redirect(url_for('profileeditor'))

    return render_template("register.html")




if __name__ == "__main__":
    app.run(debug=True, port=5501)
