from flask import Flask, request, jsonify
import builtins

app = Flask(__name__)

def find_numbers_with_digit_root(target_root):
    def digit_root(n):
        while n >= 10:
            n = builtins.sum(int(d) for d in str(n))
        return n

    results = []
    for num in range(10000):
        num_str = f"{num:04d}"
        digit_sum = builtins.sum(int(d) for d in num_str)
        if digit_root(digit_sum) == target_root:
            results.append(num_str)
    return results

@app.route('/run', methods=['GET'])
def run():
    try:
        x = int(request.args.get('x'))
        if not (1 <= x <= 9):
            return jsonify({"error": "x must be between 1 and 9"}), 400
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid x"}), 400

    results = find_numbers_with_digit_root(x)
    return jsonify({"results": results})

if __name__ == '__main__':
    app.run(debug=True)
