from flask import Flask
from flask import request
from twilio import twiml

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def incoming_call():
    """Handle incoming call and give instructions"""
    response = twiml.Response()
    response.say("Welcome to the Fizz Buzz hotline.", voice='woman')
    with response.gather(action="/play_game", method="POST") as g:
        g.say("Please enter a number and press pound to continue.", voice='woman')

    response.redirect('/')

    return str(response)

@app.route("/play_game", methods=['GET', 'POST'])
def play_game():
    """Handle key press from player and respond"""

    response = twiml.Response()

    if 'Digits' in request.values:
        number = int(request.values['Digits'].strip('#'))
        fizz_buzz = get_response(number)

        response.say(fizz_buzz, voice='woman')

    response.redirect('/')

    return str(response)

def get_response(entered_number):
    fizzy_response = ""
    for n in range(1, entered_number+1):
        if n % 3 == 0 and n % 5 == 0:
            fizzy_response += "Fizz Buzz "
        elif n % 3 == 0:
            fizzy_response += "Fizz "
        elif n % 5 == 0:
            fizzy_response += "Buzz "
        else:
            fizzy_response += "{} ".format(n)
    return fizzy_response

if __name__ == "__main__":
    app.run(debug=True)
