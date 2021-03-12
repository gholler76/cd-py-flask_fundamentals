from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/rows/<x>')
def rows(x):
    return render_template('rows.html', rows=int(x))


@app.route('/board/<x>/<y>')
def board(x, y):
    return render_template('board.html', rows=int(x), cols=int(y))


@app.route('/sensei/<x>/<y>/<x_color>/<y_color>')
def sensei(x, y, x_color, y_color):
    return render_template('sensei.html', rows=int(x), cols=int(y), color0=x_color, color1=y_color)


if __name__ == '__main__':
    app.run(debug=True)
