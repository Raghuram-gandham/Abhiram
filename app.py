from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def digit_root(n):
    while n >= 10:
        n = sum([int(d) for d in str(n)])
    return n

@app.route("/digitroot", methods=["POST"])
def get_matching_numbers():
    data = request.get_json()
    try:
        target_root = int(data["number"])
        if not (1 <= target_root <= 9):
            return jsonify({"error": "Digit root must be between 1 and 9"}), 400

        matches = [i for i in range(1, 10000) if digit_root(i) == target_root]
        return jsonify({
            "digit_root": target_root,
            "matches": matches,
            "count": len(matches)
        })

    except:
        return jsonify({"error": "Invalid input"}), 400

@app.route("/", methods=["GET"])
def home():
    return "Digit Root Matcher API is running!"
