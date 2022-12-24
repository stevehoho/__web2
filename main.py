from flask import Flask,render_template,request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def index():    
    return render_template('index.html')

@app.route('/name/<username>')
def show_user(username):
    return f"<h3>您的姓名是<strong>{username}</strong></h3>"

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method == "POST":
        print('由表單傳送過來的')
        print(f"email:{request.form['email']}")
        print(f"email:{request.form['password']}")
    return render_template('login.html')