from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Enables CORS

@app.route('/digit-root', methods=['POST'])
def digit_root():
    data = request.get_json()
    number = int(data.get('number'))
    steps = []
    while number >= 10:
        number = sum(int(d) for d in str(number))
        steps.append(number)
    return jsonify({'digit_root': number, 'steps': steps})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
