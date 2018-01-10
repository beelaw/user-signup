from flask import Flask, request, redirect
import cgi
import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir), autoescape=True)

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route("/")
def index():
    template = jinja_env.get_template('form.html')
    return template.render()

@app.route("/", methods = ['POST'])
def sign():
    name = request.form['username']
    password = request.form['password']
    verify_password = request.form['verify_password']
    email = request.form['email']

    username_error = ''
    password_error = ''
    email_error = ''


    if ' ' in name or len(name) < 3 or len(name) >20:
        username_error = "Username must have no spaces and be between 3 and 20 characters long"
    if ' ' in password or len(password) < 3 or len(password) >20:
        password_error = "Password must have no spaces and be between 3 and 20 characters long"

    if not password == verify_password:
        password_error = "Passwords must match"

    if ' ' in email or '@' not in email or '.' not in email or len(email) <3 or len(email) >20:
        email_error = "Invalid email"
    if email == '':
        email_error = ''

    if username_error == '' and password_error == '' and email_error == '':
        template = jinja_env.get_template('welcome.html')
        return template.render(user=name)
    template = jinja_env.get_template('form.html')
    return template.render(username_error = username_error, password_error = password_error, email_error = email_error, name = name, password = password, verify_password = verify_password, email = email)




app.run()