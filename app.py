import requests
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/menu")
def menu():
    return render_template("menu.html")


@app.route("/grounding")
def grounding():
    return render_template("grounding.html")


@app.route("/breathing")
def breathing():
    return render_template("breathing.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/needs")
def needs():
    return render_template("needs.html")


@app.route("/send_need", methods=["POST"])
@app.route("/send_need", methods=["POST"])
def send_need():

    message = request.form["message"]

    TOKEN = "8580066687:AAFMqZXHVbitPfs0pE7SKTt0Tp95OFi-3PY"
    CHAT_ID = "5948437090"

    testo = f"Noela ha bisogno di:\n\n{message}"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(
        url,
        data={
            "chat_id": CHAT_ID,
            "text": testo
        }
    )

    return """
    <h1>Va bene amore ❤️</h1>
    <p>Ho ricevuto il tuo messaggio.</p>
    <a href="/">Torna alla home</a>
    """

@app.route("/message")
def message():
    return render_template("message.html")

if __name__ == "__main__":
    app.run(debug=True)