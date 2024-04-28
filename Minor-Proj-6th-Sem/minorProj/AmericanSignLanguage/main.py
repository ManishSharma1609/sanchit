from flask import Flask, jsonify, request, render_template
from webcam import webcam

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")

@app.route('/open_webcam')
def open_webcam():
    # Call the function from webcam.py
    result = webcam()
    return jsonify(result=result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)