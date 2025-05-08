from flask import Blueprint, render_template, request
from .models import User

main = Blueprint('main', __name__)

@main.route('/')
def index():
    users = User.query.all()
    return render_template('index.html', user=users)


@main.route('/test')
def test():
    return render_template('test.html')

@main.route('/form')
def form():
    return render_template('form.html')

@main.route('/submit', methods=['POST'])
def submit():
    first_name = request.form['fname']
    last_name = request.form['lname']
    email = request.form['email']
    # save to db here
    return f"Received data: {first_name} {last_name}, Email: {email}"
