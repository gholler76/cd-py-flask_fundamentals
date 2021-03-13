from flask import Flask, render_template, redirect
app = Flask(__name__)


@app.route('/')
def index():
    student_info = [
        {'name': 'Michael', 'age': 35},
        {'name': 'John', 'age': 30},
        {'name': 'Mark', 'age': 25},
        {'name': 'KB', 'age': 27},
    ]
    return render_template('index.html', random_numbers=[3, 1, 5], students=student_info)


@app.route('/table')
def table():
    users = [
        {'first_name': 'Michael', 'last_name': 'Choi'},
        {'first_name': 'John', 'last_name': 'Supsupin'},
        {'first_name': 'Mark', 'last_name': 'Guillen'},
        {'first_name': 'KB', 'last_name': 'Tonel'}
    ]
    return render_template('table.html', users=users)


if __name__ == '__main__':
    app.run(debug=True)
