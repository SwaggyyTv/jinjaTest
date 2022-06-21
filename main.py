from flask import Flask, render_template

#export FLASK_ENv=development
#export FLASK_APP="file da usare"
#flask run
#ssh-keygen -t rsa

# CReate Flask instance
app = Flask(__name__)

@app.route("/")
def Index():
    text = "This my website's main page!"
    return render_template("Index.html",
                           text=text)

@app.route("/settings")
def settings():
    text="Here you can customize your profile!"
    settingsList = ["customize theme","change username","verify email"]
    return render_template("settings.html",
                           text = text,
                           settingsList = settingsList)

@app.route("/user/<name>")
def user(name):
    text = "Hello "+name.capitalize()
    return render_template("user.html",
                           text = text)

#page not found error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("Error pages/404.html"), 404

#internal server error
@app.errorhandler(500)
def internalServerError(e):
    return render_template("Error pages/500.html"),500

