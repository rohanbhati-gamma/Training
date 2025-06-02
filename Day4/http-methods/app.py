from flask import Flask, request, render_template
app = Flask(__name__)

from flask import redirect, url_for
@app.route('/')
def home():
    return redirect('hello')

@app.route('/hello')
def hello():
    return 'Rohan Bhati'

@app.route('/demo')
def demo():
    return redirect(url_for('rohan'))

@app.route('/contact')
def rohan():
    return 'This is contact page'

@app.route('/square', methods = ['GET', 'POST'])
def squareofnum():
    if request.method=='POST':
        num = request.form.get('num')

        # if num is None:
        #     return render_template('squarenum.html')
        if num.strip()=='':
            return 'Invalid number'

        sq = int(num)**2
        return render_template('answer.html',squareofnum=sq, num=num)
    return render_template('squarenum.html')

@app.route('/squarewithget', methods = ['GET'])
def squarewithget():
    num = request.args.get('num2')

    if num is None:
        return render_template('squarenum.html')
    elif num.strip()=='':
        return 'Invalid number'
    try:
        sq = int(num)**2
        return render_template('answer.html',squareofnum=sq, num=num)
    except ValueError:
        return 'Enter valid Number'
    else:
        return request.method

if __name__== '__main__':
    app.run(debug=True)

    # get : request data from server
    # post : submit data to be processed to the server
    # put : replaces entire resource with new data. if not exist, create new
    # patch : update specific part of the resource
    # delete : deleted data on the server at a specified location