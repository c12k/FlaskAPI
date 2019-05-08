from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    # default response for Get method
    text = 'Flask API example version 0.2.0'
    if request.method == 'POST':
        # get text from form
        text = request.form.get('sometext')
        # format as json for api call
        data = {"sometext": text}
        # call the api
        response = requests.post('http://localhost:5000/api1', json=data)
        # get the api response output
        text = response.text
    return render_template('index2.html', output=text)

if __name__ == "__main__":
    app.run("0.0.0.0", port=80)
