from flask import Flask, render_template, request, jsonify
from bot.core import ChatBotCore
import os

app = Flask(__name__)
chatbot = ChatBotCore()

@app.before_first_request
def initialize():
    chatbot.train_bot()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400
    
    response = chatbot.get_response(user_message)
    return jsonify({"response": str(response)})

if __name__ == "__main__":
    app.run(debug=True)