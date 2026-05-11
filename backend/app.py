from flask import Flask, request, jsonify, send_file
from flask_cors import CORS
from utils.analyzer import analyze_text
from utils.data_analyzer import analyze_data
import os

app = Flask(__name__)
CORS(app)

@app.route("/analyze", methods=["POST"])
def analyze():
    data = request.json
    text = data.get("text")
    result = analyze_text(text)
    return jsonify({"response": result})

@app.route("/ask-data", methods=["POST"])
def ask_data():
    data = request.json
    question = data.get("question")

    file_path = "uploads/sales_data_sample.csv"

    result = analyze_data(file_path, question)

    return jsonify({"response": result})

@app.route("/chart")
def get_chart():
    return send_file("static/chart.png", mimetype='image/png')

if __name__ == "__main__":
    app.run(debug=True)