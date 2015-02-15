""" The flask app """
from flask import Flask
APP = Flask(__name__)

@APP.route('/', methods=['GET'])
def home_page():
    """
    Generates an unauthenticated page.
    """
    return """
    <html>
        <title>Python OpenID Connect library (pyoidc) test site</title>
        <body>
            There's nothing to see here.
        </body>
    </html>
    """