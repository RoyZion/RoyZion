from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)
@app.route('/')
def main():
    print('Welcome to main Page!')
    return redirect('/home')

@app.route('/home')
def my_Page():
    print('URL to use for')
    return redirect(url_for('my_function'))

@app.route('/my_page')
def my_function():
    print('Welcome to My Page!')
    return 'This is my first use in flack'

if __name__ == '__main__':
    app.run(debug=True)