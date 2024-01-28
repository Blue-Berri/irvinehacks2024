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

@app.route("/profileeditor")
def profileeditor():
    return render_template("profileeditor.html")

@app.route("/register", methods=["POST"])
def register():
    print("Hi")
    if request.method == "POST":
        data = {
            "email": request.form['Email'],
            "password": request.form['Password']
            # "name": request.form['Name'],
            # "age": request.form['Age'],
            # "gender": request.form['Gender'],
            # "orientation": request.form['Orientation'],
            # "major": request.form['Major'],
            # "bio": request.form['Bio'],
            # "pfp": request.form['Pfp']
        }
        print(data)

        try:
            with open("userData.json", 'r') as file:
                existing_data = json.load(file)
        except FileNotFoundError:
            existing_data = []
        existing_data["users"].append(data)
        with open('userData.json', 'w') as file:
            json.dump(existing_data, file)
    
# put data in db
    return redirect(url_for('home'))

# @app.route('/home')
# def home():
#     return render_template('home.html')

if __name__ == "__main__":
    app.run(debug=True)