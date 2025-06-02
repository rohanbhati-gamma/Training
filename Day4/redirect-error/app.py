from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success')
def success():
    return 'Successfully Login'

@app.route('/login', methods= ['POST', 'GET'])
def login():
    if request.method == "POST" and request.form['username']=='admin':
        return redirect((url_for('success')))
    return redirect(url_for('home'))

# abort
from flask import abort
@app.route('/<uname>')
def username(uname):
    if uname[0].isdigit():
        abort(400)
    return '<h2>Welcome %s </h2>' %uname

if __name__ == '__main__':
    app.run(host='192.168.0.105', port=8888, debug = True)