import flask
import bugzilla

app = flask.Flask(__name__)

@app.route("/")
def index():
    return flask.render_template("content/view_bugs.html")

@app.route("/aboutus")
def aboutus():
    return flask.render_template("content/about.html")

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
    user = bugzilla.models.User()
    result = user.check_login(flask.request.get("inputEmail"), flask.request.get("inputPassword"))

    if result:
        return "Login Succeeded"
    else:
        return "Login Failed"

if __name__ == '__main__':
    app.run(debug=True)