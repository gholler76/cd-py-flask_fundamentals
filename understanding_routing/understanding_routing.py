from flask import Flask
app = Flask(__name__)


@app.route('/')
def index():
    return 'Hello World!'


@app.route('/dojo')
def dojo():
    return 'Dojo!'


@app.route('/<name>')
def hiName(name):
    return f'Hi, {name}!'


@app.route('/rpt/<word>/<num>')
def repeat(word, num):
    return word*int(num)


if __name__ == "__main__":
    app.run(debug=True)
