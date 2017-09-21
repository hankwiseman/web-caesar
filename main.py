from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)

app.config['DEBUG'] = True      # displays runtime errors in the browser, too

page_header = """
<!DOCTYPE html>
<html>
    <head>
        <title>Web-Caesar</title>
        <style>
            form {
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>

    </body>
</html>
"""
form = """
    <form action="/" method="post">
        <p>
        <label for="rot">
            Rotate by:
            <input type="text" id="rot" name="rot" value="0"/>
            
        </label>
        </p>
        <p>
        <textarea name="text">{0}</textarea>
        </p>
        <p>
        <input type="submit" value="Submit"/>
        </p>
    </form>
"""
@app.route("/", methods=['POST'])
def encrypt():
    rot_value = int(request.form['rot'])
    text = str(request.form['text'])
    new_text = rotate_string(text,rot_value)

    return form.format(new_text)


@app.route("/", )
def index():

    return form.format("")


app.run()