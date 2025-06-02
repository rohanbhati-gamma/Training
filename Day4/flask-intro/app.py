from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return 'This is About Page'


# Variables in Flask
@app.route('/name/<fname>')
def name(fname):
    return 'Your Name is %s' % fname

@app.route('/vint/<int:age>')
def vint(age):
    return 'Your age is %d' % age

@app.route('/vfloat/<float:num>')
def vfloat(num):
    return 'Float number : %f' % num

# dynamic url
from flask import redirect, url_for
@app.route('/admin')
def admin():
    return 'This is admin page'

@app.route('/guest/<guest>')
def guest(guest):
    return 'Guest Name : %s' % guest

@app.route('/user/<yname>')
def user(yname):
    if yname=='admin':
        return redirect(url_for('admin'))
    else:
        return redirect(url_for('guest',guest=yname))

from flask import request, make_response
# set cookie
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method=='POST':
        user = request.form['nm']
        resp = make_response(render_template('cookie.html'))
        resp.set_cookie('UserID', user)
        return resp
    else:
        return request.method
@ app.route('/getcookie')
def getcookie():
    name = request.cookies.get('UserID')
    return '<h1>welcome '+name+'</h1>'

if __name__=='__main__':
    app.run(debug=True)