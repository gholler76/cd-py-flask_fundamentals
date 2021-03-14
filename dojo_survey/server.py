from flask import Flask, render_template, redirect, request
app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/result', methods=["POST"])
def result():
    print("*"*50)
    print(request.form['student_name'])
    return render_template('result.html', name=request.form['student_name'], st=request.form['state'], comments=request.form['comments'])


if __name__ == '__main__':
    app.run(debug=True)
