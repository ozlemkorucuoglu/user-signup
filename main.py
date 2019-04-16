from flask import Flask, request, redirect

import os
import jinja2

template_dir = os.path.join(os.path.dirname(__file__),'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir))

app = Flask(__name__)
app.config['DEBUG'] = True


@app.route("/")
def index():
    template=jinja_env.get_template('HomePage.html')
    return template.render()


@app.route("/", methods=['POST'])
def validate_input():
    username= request.form['username']
    password= request.form['password']
    password2= request.form['password2']
    email= request.form['email']
    username_error=''
    password_error=''
    password2_error=''
    email_error=''

    if not username:
        username_error='you need to fill this field' 
    if not password: 
        password_error='you need to fill this field'
    if not password2:
        password2_error='you need to fill this field'
    
    if len(username)<3 or len(username)>20 or (' ' in username):
        username_error='Username need to be at least 3 characters and not more than 20 characters with no spaces'
    if len(password)<3 or len(password)>20 or (' ' in password):
        password_error='Password need to be at least 3 characters and not more than 20 characters with no spaces'
        password=''
    if password != password2:
        password2_error='Password does not match'
        password2=''

    if email and (len(email)<3 or len(email)>20 or (' ' in email) or email.count('@') > 1 or email.count('.') > 1):
        email_error='Email need to be at least 3 characters and not more than 20 characters and no duplictaes of @ and .'

    if not username_error and not password_error and not password2_error and not email_error:
        template = jinja_env.get_template('WelcomePage.html')
        return template.render(user_name=username)
    else:
        password=''
        password2=''
        template=jinja_env.get_template('HomePage.html')
        return template.render(username_error=username_error,
                password_error=password_error,
                password2_error=password2_error,
                email_error= email_error,
                username=username,
                password=password,
                password2=password2,
                email=email)
        

app.run()