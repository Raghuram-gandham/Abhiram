from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

def digit_root(n):
    while n >= 10:
        n = sum(int(d) for d in str(n))
    return n

@app.route('/get_numbers', methods=['POST'])
def get_numbers():
    data = request.get_json()
    target_root = int(data['digit_root'])

    result = [i for i in range(1, 10000) if digit_root(i) == target_root]
    return jsonify({
        'digit_root': target_root,
        'numbers': result
    })

if __name__ == '__main__':
    app.run(debug=True)
