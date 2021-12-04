import numpy as np
from flask import Flask,request,jsonify,render_template
import pickle

from google_trans_new import google_translator
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

translator = google_translator()

app= Flask(__name__)
@app.route('/',methods=['GET','POST'])

def main():
    if request.method=="POST":
        sentence=request.form.get("inp")
        translation = translator.translate(sentence.encode('unicode-escape').decode('ASCII'), lang_tgt='en')
        analyser = SentimentIntensityAnalyzer()
        result = analyser.polarity_scores(translation)
        if(result["compound"] < 0):
            return render_template("index.html",message="Negative☹")
        if(result["compound"] == 0):
            return render_template("index.html",message="Neutral😐")
        if(result["compound"] > 0):
            return render_template("index.html",message="Positive😊  ")
    return render_template("index.html")


