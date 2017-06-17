from flask import Flask,request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = ''' 
<!DOCTYPE html>
<html>
    <head>
        
        <style>
        form {{
            background-color: #eee;
            padding: 20px;
            margin: 0 auto;
            width: 540px;
            font: 16px sans-serif;
            border-radius: 10px;
        }}
        textarea {{
            margin: 10px 0;
            width: 540px;
            height: 120px;
        }}
        </style>
    </head>
    <body>
        <form action="/encrypt" method="post">
            <label for="original-message">How many characters would you like to rotate by?</label>
            <input id="original-message" type="text" name="rot" value="0" />
            <textarea name="text" rows="10" columns="30"> {0} </textarea>
            <input type="submit" />

        </form>
    </body>
</html>
'''

@app.route("/")
def index():
    return form.format("")

@app.route("/encrypt", methods=["POST"])
def encrypt():
    raw_message = request.form["text"]
    rotate = int(request.form["rot"])

    cryptic = rotate_string(raw_message, rotate)
    return form.format(cryptic)

@app.route("/message", methods=["POST"])
def message():
    raw_message = request.form["text"]
    return "<h1>Your original message is:" + raw_message + "</h1>"


app.run()