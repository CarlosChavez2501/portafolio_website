from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("index.htm")


@app.route("/contact")
def contact():
    return render_template("contact.htm")


if __name__ == "_main_":
    app.run(debug=True)
