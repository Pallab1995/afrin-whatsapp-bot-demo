from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.form.get("Body").strip().lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "hi" in incoming_msg or "hello" in incoming_msg:
        reply = ("👋 Welcome to Afrin Electronics!\n"
                 "Please choose an option:\n"
                 "1️⃣ View Products\n"
                 "2️⃣ Talk to Support\n"
                 "3️⃣ Request a Callback")
    elif incoming_msg == "1":
        reply = ("📦 Product List:\n"
                 "- LED Bulbs 💡\n"
                 "- Inverters 🔋\n"
                 "- Switch Boards ⚡")
    elif incoming_msg == "2":
        reply = ("💬 Our support team is available!\n"
                 "Please call us at +91-9876543210\n"
                 "Or reply here and we'll get back to you.")
    elif incoming_msg == "3":
        reply = ("📞 Please share your *name* and *phone number*.\n"
                 "We will call you back shortly.")
    else:
        reply = ("Sorry, I didn't understand that.\n"
                 "Please reply with 1, 2, or 3.")

    msg.body(reply)
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
