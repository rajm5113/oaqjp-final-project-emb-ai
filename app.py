from flask import Flask, render_template, request
from emotion_detection import emotion_detector

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    emotion = None
    scores = {}
    if request.method == "POST":
        text = request.form["text"]
        result = emotion_detector(text)
        emotion = result["dominant_emotion"]
        scores = result
        scores.pop("dominant_emotion", None)
    return render_template("index.html", emotion=emotion, scores=scores)

if __name__ == "__main__":
    app.run(debug=True)
