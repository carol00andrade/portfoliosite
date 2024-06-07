from flask import Flask, request, render_template
import requests

app = Flask(__name__)  

@app.route("/")
def home():
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)
