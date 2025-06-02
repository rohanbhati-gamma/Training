from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
    sites = ['twitter', 'facebook', 'instagram', 'whatsapp']
    return render_template('about.html',sites=sites)

@app.route("/contact/<role>")
def contact(role):
    role = 'Admin'
    return render_template("contact.html", person=role)

if __name__ == '__main__':
    app.run(debug=True)