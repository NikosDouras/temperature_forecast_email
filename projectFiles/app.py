# app.py
from flask import Flask, request, redirect, render_template

app = Flask(__name__)

EMAIL_LIST_FILE = 'email_list.txt'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/subscribe', methods=['POST'])
def subscribe():
    email = request.form['email']
    if email:
        with open(EMAIL_LIST_FILE, 'a') as file:
            file.write(email + '\n')
    return redirect('/thank_you')

@app.route('/thank_you')
def thank_you():
    return render_template('thank_you.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)

