"""Display the main view."""
import flask
import conorrafferty


@conorrafferty.app.route("/")
def show_index():
    """Display / route."""
    return flask.render_template("index.html")
