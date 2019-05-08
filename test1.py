from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # default response for Get method
    text = 'Flask API example version 0.1.0'
    if request.method == 'POST':
        # call the api
        response = requests.get('http://localhost:5000')
        # get the api response output
        text = response.text
    return render_template('index1.html', output=text)

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
