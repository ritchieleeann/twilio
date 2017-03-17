from flask import Flask
from twilio import twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_call():
    """Handle incoming call and give instructions"""
    response = twiml.Response()
    response.say("Welcome to the Fizz Buzz hotline.", voice='woman')
    with response.gather(action="/play_game", method="POST") as g:
        g.say("Please enter a number and press pound to continue.", voice='woman')

    return str(response)

@app.route("/play_game", methods=['GET', 'POST'])
def play_game():
    """Handle key press from player and respond"""

    number = request.values.get('Digits', None)
    fizz_buzz = get_response(number)

    response = twiml.Response()
    response.say(fizz_buzz, voice='woman')
    return str(response)

def get_response(entered_number):
    fizzy_response = ""
    for n in range(entered_number):
        if n % 3 == 0:
            fizzy_response += "Fizz"
        elif n % 5 == 0:
            fizzy_response += "Buzz"
        else:
            fizzy_response += str(entered_number)
    return fizzy_response

if __name__ == "__main__":
    app.run(debug=True)
