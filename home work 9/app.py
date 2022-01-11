from flask import Flask, redirect, url_for, render_template, request, session
from interact_db import interact_db, query_to_json
import json
import requests

app = Flask(__name__)

my_users = {'user1': {'name': 'Yossi', 'email': 'yoss@gmail.com'},
         'user2': {'name': 'David', 'email': 'davi@gmail.com'},
         'user3': {'name': 'Shlomi', 'email': 'shlomi@gmail.com'},
         'user4': {'name': 'Roy', 'email': 'roy@gmail.com'},
         'user5': {'name': 'Avi', 'email': 'avi@gmail.com'},
         'user6': {'name': 'Moshe', 'email': 'moshe@gmail.com'}
         }

# all these routes will lead to the same page (GET is the default method)
@app.route("/home_page")
@app.route("/home")
@app.route("/")
def home_func():
    # DB
    found = False
    if found: # theoretically - if a user was found, return the HTML with the following parameters
        return render_template('index.html',
                               name='Roy',
                               last_name='Zion')
    else:
        return render_template('index.html')


@app.route("/about", methods=['GET'])
def about_func():
    if session['new_name'] == '': # if the user didn't log in yet / logged out
        return render_template('about.html')
    else: # else - return the page "tailored" according to the user details
        return render_template('about.html',
                               uni='Ben Gurion University',
                               profile={'First name': 'Roy',
                                        'Last name': 'Zion'},
                               degrees=['BSc.', 'Msc.'],
                               hobbies=('Football', 'Music', 'Dogs')
                               )

@app.route("/try_request")
def try_request_func():
    return request.method  # this way we can see which method a page uses


@app.route("/assignment9", methods=['GET', 'POST'])
def assignment9_func():
    # search form
    if 'name' in request.args:
        name = request.args['name']
        if name == '':
            return render_template('assignment9.html', users_list=my_users)

        for key, value in my_users.items():
            if value.get('name') == name:
                return render_template('assignment9.html',
                                       user_name=value.get('name'), user_email=value.get('email'))

    # Registration form
    if request.method == 'POST':
        new_name = request.form['new_name']
        session['new_name'] = new_name
    return render_template('assignment9.html')

@app.route("/logout_assignment9")
def logout_assignment9_func():
    session['new_name'] = '' # removing the global variable
    return render_template('assignment9.html') # returns to the log in page

from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route("/assignment11/users")
def assignment11_page():
    query = "select * from users"
    query_result = query_to_json(query=query)
    return json.dumps(query_result)

@app.route("/assignment11/outer_source", methods=['GET'])
def assignment11_os_page():
    if 'number' in request.args:
        number = request.args['number']
        res = requests.get(url=f"https://reqres.in/api/users/{number}")
        res = res.json()
        return render_template('assignment11_outer_source.html', user=res['data'])
    return render_template('assignment11_outer_source.html')


if __name__ == '__main__':
        app.secret_key = '123'  # we need a secret key when we import and use flask session
        app.run(debug=True)