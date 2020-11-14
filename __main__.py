import os
import flask
from bugzilla import sessions
from bugzilla.models import Bug, User

app = flask.Flask(__name__)
app.secret_key = os.urandom(12)
session = sessions.Sessions()

@app.route("/")
def start():
    return flask.redirect(flask.url_for('index'))

@app.route("/index")
def index():
    bug = Bug()
    return flask.render_template("content/view_bugs.html", session=session, bug_cards=bug.to_html_cards())

@app.route("/aboutus")
def aboutus():
    return flask.render_template("content/about.html", session=session)

@app.route("/logout")
def logout():
    flask.flash("Logout successfully", 'success')
    global session 
    session = sessions.Sessions()
    return flask.render_template("auth/login.html", session=session)

@app.route("/login")
def login():
    return flask.render_template("auth/login.html", session=session)

@app.route("/register")
def register():
    return flask.render_template("auth/register.html", session=session)

@app.route("/search/<value>")
def search(value):
    return "Searching {}".format(value)

@app.route("/do_register", methods=['POST'])
def do_register():
    user = User()
    result = user.registration(flask.request.form["inputEmail"], flask.request.form["inputName"], flask.request.form["inputPhone"], flask.request.form["inputPassword"])
    if result[0]:
        flask.flash(result[1], 'success')
        session.user = flask.request.form["inputEmail"]
        return flask.redirect(flask.url_for('login'))
    else:
        flask.flash(result[1], 'error')
        return flask.redirect(flask.url_for('register'))

@app.route("/do_login", methods=['POST'])
def do_login():
    user = User()
    result = user.check_login(flask.request.form["inputEmail"], flask.request.form.get("inputPassword"))

    if result[0]:
        flask.flash(result[1], 'success')
        session.user = flask.request.form["inputEmail"]
        return flask.redirect(flask.url_for('index'))
    else:
        flask.flash(result[1], 'error')
        return flask.redirect(flask.url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)