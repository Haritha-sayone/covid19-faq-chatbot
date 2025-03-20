from flask import Flask, request, jsonify
# from flask_cors import CORS, cross_origin
from chatbot import get_chat_response

app = Flask(__name__)
# CORS(app,resources={r'/*':{origins:'http://localhost:3001'}})

@app.route('/ask', methods=['POST'])
# @cross_origin()
def ask():
    data = request.get_json()
    user_query = data.get("query")
    response = get_chat_response(user_query)
    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
