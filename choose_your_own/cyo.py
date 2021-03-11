from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/throw')
def throw():
    return render_template('throw.html')


@app.route('/open_box')
def open_box():
    return render_template('open_box.html')


@app.route('/police')
def police():
    return render_template('police.html')


@app.route('/take_home')
def take_home():
    return render_template('take_home.html')


if __name__ == "__main__":
    app.run(debug=True)
