@app.route("/login", methods=["GET", "POST"])
def login():
    # login logic goes here
    return render_template("login.html")
