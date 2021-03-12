from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/play/<num>/<color>')
def play(num, color):
    return render_template(
        'play.html',
        some_num=int(num),
        greeting="Welcome",
        box_color=color
    )


if __name__ == '__main__':
    app.run(debug=True)
