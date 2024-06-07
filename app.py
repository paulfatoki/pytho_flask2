from flask import Flask,render_template,jsonify,redirect
 
import os
import socket
app=Flask(__name__)
 
#find the hostname and machine ip
 
 
def findhostname():
    hostname=socket.gethostname()
    hostip=socket.gethostbyname_ex(hostname)
    return str(hostname),str(hostip)

def findaddress():
    phone_number="09083456788"
    emailaddress="df@gmail.com"
    comp="4 Ojo road Ogba,Lagos"
    
    return str(phone_number),str(emailaddress),str(comp)


@app.route("/")
def home():
    return "Welcome to my page"

@app.route("/score")
def score():
    a=1000
    b=150
    result=a+b
    name = "paul"
    return render_template("index.html",name=name)
    #return str(result)


    
@app.route("/details")
def hostname():
    myhost,myip=findhostname()
    return render_template('show.html',host=myhost,IP=myip)

if __name__ == '__main__':
    app.run(debug=True, port=5004
            ,host="127.0.0.1")
