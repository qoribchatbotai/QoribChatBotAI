from flask import Flask, request
import requests

app = Flask(__name__)

# Data dari UltraMSG kamu
INSTANCE_ID = "instance131460"
TOKEN = "47029yujudomow1i"

# Alamat API untuk kirim pesan
URL_SEND = f"https://api.ultramsg.com/{INSTANCE_ID}/messages/chat"

# Fungsi untuk kirim pesan balik
def send_message(phone, message):
    data = {
        "token": TOKEN,
        "to": phone,
        "body": message
    }
    requests.post(URL_SEND, data=data)

# Fungsi terima pesan masuk dari WhatsApp
@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    if data and "body" in data and "from" in data:
        message = data["body"]
        phone = data["from"]

        # Balasan otomatis
        reply = f"Halo! Kamu berkata: {message}"
        send_message(phone, reply)

    return "OK"

# Jalankan server Flask
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
