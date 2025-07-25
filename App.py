from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allows your HTML file to access this backend

@app.route("/digit-root", methods=["POST"])
def digit_root():
    data = request.get_json()
    number = data.get("number")

    if not isinstance(number, int) or number < 0 or number > 9999:
        return jsonify({"error": "Number must be an integer between 0 and 9999"}), 400

    steps = []
    while number >= 10:
        digits = [int(d) for d in str(number)]
        steps.append(digits)
        number = sum(digits)
    steps.append([number])

    return jsonify({"result": number, "steps": steps})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
