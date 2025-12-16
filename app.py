from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Simple chatbot brain
def chatbot_reply(user_message):
    msg = user_message.lower()

    if "hi" in msg or "hello" in msg:
        return "Hi! I'm Shelten's AI Avatar. Nice to meet you."

    elif "who are you" in msg:
        return (
            "I am an AI Avatar representing Shelten Eali Jack, "
            "a Computer Science student."
        )

    elif "skills" in msg:
        return (
            "My skills include Python, Java, HTML, CSS, SQL, "
            "Artificial Intelligence, and Web Development."
        )

    elif "technologies" in msg:
        return (
            "I work with Python, Flask, Java, SQL, HTML, CSS, "
            "basic JavaScript, and AI-based systems."
        )

    elif "projects" in msg:
        return (
            "I have worked on chatbot systems, web applications, "
            "academic mini projects, and a technology-based short film."
        )

    elif "goal" in msg:
        return (
            "My goal is to become a professional software engineer "
            "and contribute to real-world AI solutions."
        )

    elif "student" in msg:
        return (
            "I am a Computer Science student, continuously learning "
            "new technologies and improving my skills."
        )

    elif "favorite" in msg or "language" in msg:
        return (
            "My favorite programming language is Python because "
            "it is powerful, simple, and widely used in AI."
        )

    elif "learn" in msg or "help" in msg:
        return (
            "Yes! I can help you learn programming concepts, "
            "coding basics, and guide you step-by-step."
        )

    elif "what can you do" in msg:
        return (
            "I can answer questions about skills, projects, goals, "
            "technologies, and help beginners learn programming."
        )

    else:
        return (
            "I'm still learning! Try asking about my skills, "
            "projects, goals, or technologies."
        )

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    reply = chatbot_reply(user_message)
    return jsonify({"reply": reply})

if __name__ == "__main__":
    app.run(debug=True)
