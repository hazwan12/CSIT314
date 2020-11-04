import flask

app = flask.Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return flask.render_template("content/home.html")

@app.route("/aboutus")
def aboutus():
    return flask.render_template("content/about.html")

@app.route("/newbug")
def newbug():
    return flask.render_template("content/newbug.html")

@app.route("/logout")
def logout():
    return flask.render_template("auth/login.html")

@app.route("/login")
def login():
    return flask.render_template("auth/login.html")

@app.route("/register")
def register():
    return flask.render_template("auth/register.html")

@app.route("/search/<value>")
def search(value):
    return "Searching {}".format(value)

@app.route("/do_login", methods=['POST'])
def do_login():
    #Validate Login
    pass

if __name__ == '__main__':
    app.run(debug=True)