import os
from flask import Flask, request, jsonify, render_template
from google import genai

# Temporary fix: set API key directly
os.environ["GEMINI_API_KEY"] = "AIzaSyCeXQogzk7vNQc-509xxxxxxx6Ow7KsLI"

api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    raise ValueError("Please set GEMINI_API_KEY environment variable.")
client = genai.Client(api_key=api_key)

# Create chat session
chat = client.chats.create(model="gemini-2.5-flash-lite")

# Flask routes
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat_with_gemini():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    response = chat.send_message(user_message)
    bot_reply = response.text
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
