import os
import openai
from cityItinerary import saveAttractions
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        location = request.form["location"]
        attractions = saveAttractions(location)
        return redirect(url_for("index", result=attractions))

    result = request.args.get("result")
    return render_template("index.html", result=result)
