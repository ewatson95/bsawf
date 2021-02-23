from flask import Flask


def create_app():
    """
    Create a Flask application using the app factory pattern.

    Returns:
        app: Flask app
    """
    app = Flask(__name__, instance_relative_config=True)

    app.config.from_object("config.settings")
    app.config.from_pyfile("settings.py", silent=True)

    @app.route("/")
    def index():
        """
        Render a Hello World response.

        Returns:
            string: The hello world response
        """
        return app.config['HELLO']

    return app
