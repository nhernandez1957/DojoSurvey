from crypt import methods
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)    
app.secret_key = 'keep it secret, keep it safe'



@app.route('/')          
def index():
    return render_template("index.html")

@app.route('/process', methods = ["POST"])
def user():
    session['name'] = request.form['name']
    session['email'] = request.form['email']
    session['location'] = request.form['location']
    session['language'] = request.form['language']
    session['comment'] = request.form['comment']
    return redirect('/afterpost')

@app.route('/afterpost')
def afterPost():
    return render_template("second.html", name = session['name'], email = session['email'], location = session['location'], language = session['language'], comment = session['comment'])

if __name__=="__main__":       
    app.run(debug=True, port = 5001)    