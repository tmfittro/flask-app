# module 10
# taryn fittro 4/5/26
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/about")
def about_page():
    return render_template('about.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)