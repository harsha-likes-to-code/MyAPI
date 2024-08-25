from flask import Flask, request, jsonify

app = Flask(__name__)

# User details
USER_ID = "john_doe_17091999"
EMAIL = "john@xyz.com"
ROLL_NUMBER = "ABCD123"


@app.route('/bfhl', methods=['POST'])
def process_data():
    data = request.json.get('data', [])

    # Separate numbers and alphabets
    numbers = [item for item in data if item.isdigit()]
    alphabets = [item for item in data if item.isalpha()]

    # Find the highest lowercase alphabet
    lowercase_alphabets = [char for char in alphabets if char.islower()]
    highest_lowercase_alphabet = max(lowercase_alphabets) if lowercase_alphabets else ""

    response = {
        "is_success": True,
        "user_id": USER_ID,
        "email": EMAIL,
        "roll_number": ROLL_NUMBER,
        "numbers": numbers,
        "alphabets": alphabets,
        "highest_lowercase_alphabet": [highest_lowercase_alphabet] if highest_lowercase_alphabet else []
    }

    return jsonify(response), 200


@app.route('/bfhl', methods=['GET'])
def get_operation_code():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200


if __name__ == '__main__':
    app.run(debug=True)

