from flask import Flask, request, jsonify

app = Flask(__name__)

def calculator(num1, num2):
    return num1 + num2

@app.route('/calculate', methods=['GET'])
def calculate():
    num1 = request.args.get('num1')
    num2 = request.args.get('num2')

    if num1 is None or num2 is None:
        return jsonify({'error': 'Missing data'})

    result = calculator(float(num1), float(num2))

    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)
