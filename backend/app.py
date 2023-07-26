from flask import Flask, request, jsonify
from my_chat_basics import *
from flask_cors import CORS
app = Flask(__name__)
CORS(app)

@app.route('/get_response', methods=['POST'])
def get_chat_response():
    try:
        input_prompt = request.json['input_prompt']
        response = get_response(input_prompt)
        return jsonify({'response': response})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
