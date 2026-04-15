from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route("/")
def index():
    
    return redirect("websiteaugust/frontend/templates/index.html")
if __name__ == "__main__":
    app.run(debug=True)

