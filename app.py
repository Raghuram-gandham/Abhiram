from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def digit_root_steps(n):
    steps = []
    while n >= 10:
        digits = [int(d) for d in str(n)]
        n = sum(digits)
        steps.append(n)
    return steps, n

@app.route("/digitroot", methods=["POST"])
def get_digit_root():
    data = request.get_json()
    try:
        number = int(data["number"])
        if number > 9999:
            return jsonify({"error": "Number must be 9999 or less"}), 400
        steps, root = digit_root_steps(number)
        return jsonify({"steps": steps, "digit_root": root})
    except:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/", methods=["GET"])
def home():
    return "Digit Root API is running!"
