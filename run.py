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

    digit_pressed = request.values.get('Digits', None)
    if digit_pressed == "1":
        response = twiml.Response()
        response.say("Your number was {}".format(digit_pressed), voice='woman')
        return str(response)

if __name__ == "__main__":
    app.run(debug=True)
