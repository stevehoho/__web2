from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():    
    return render_template('index.html')

@app.route('/name/<username>')
def show_user(username):
    return f"<h3>您的姓名是<strong>{username}</strong></h3>"

@app.route('/login')
def login():
    return render_template('login.html')