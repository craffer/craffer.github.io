"""Display the projects view."""
import flask
import conorrafferty


@conorrafferty.app.route("/projects")
def show_projects():
    """Display /projects route."""
    return flask.render_template("projects.html")
