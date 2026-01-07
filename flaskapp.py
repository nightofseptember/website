from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def slash():
    return redirect("/index")
