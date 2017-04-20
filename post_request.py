from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('form.html')


@app.route('/handle_request', methods=['POST'])
def print_name():
    name = request.form['name']
    return name


if __name__ == '__main__':
    app.run()
