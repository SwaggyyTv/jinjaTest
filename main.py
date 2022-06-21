from flask import Flask, render_template, flash
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import data_required


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
@app.route("/form",methods=["GET","POST"])
def form():

    name = None
    form = NamerForm()
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ""
        flash("Form submitted succesfully")
    return render_template("Name.html",
                           name = name,
                           form = form)

#page not found error
@app.errorhandler(404)
def page_not_found(e):
    return render_template("Error pages/404.html"), 404

#internal server error
@app.errorhandler(500)
def internalServerError(e):
    return render_template("Error pages/500.html"),500

#create a Form Class
app.config["SECRET_KEY"] = "tirocinioFBK!"

class NamerForm(FlaskForm):
    name = StringField("What's your name",validators=[data_required()])
    submit = SubmitField("Submit")

