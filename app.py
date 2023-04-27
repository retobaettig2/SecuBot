"""
Usage:
In this code, we've created a Flask application with a few routes for logging in and logging out. We've also set up OAuth2 authentication with Google using the Flask-OAuthlib package.
To use this code, you'll need to replace the `your-secret-key-here` and `your-consumer-key-here` and `your-consumer-secret-here` placeholders with your actual values. You can get these values by creating a new project in the Google Cloud Console and enabling the Google+ API.
Once you've updated the code with your values, you can run the application using `python app.py`. You should be able to visit `http://localhost:5000/login` in your web browser to begin the OAuth2 authentication process.
After logging in, you will be redirected back to the `authorized` route, which will set up a new user session and redirect you back to the home page. You can then use the `@login_required` decorator to protect any routes that require authentication.
"""
import os
from flask import Flask, redirect, url_for
from flask_login import LoginManager, UserMixin, login_required, login_user, logout_user
from flask_oauthlib.client import OAuth

app = Flask(__name__)
app.config['SECRET_KEY'] =  os.urandom(24)

login_manager = LoginManager()
login_manager.init_app(app)

oauth = OAuth(app)

google = oauth.remote_app(
    'google',
    consumer_key='1022698865826-n1ls6bpmovg7u455ik7sjs730v5l0gb2.apps.googleusercontent.com',
    consumer_secret='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',
    request_token_params={
        'scope': 'email'
    },
    base_url='https://www.googleapis.com/oauth2/v1/',
    request_token_url=None,
    access_token_method='POST',
    access_token_url='https://accounts.google.com/o/oauth2/token',
    authorize_url='https://accounts.google.com/o/oauth2/auth'
)


class User(UserMixin):
    def __init__(self, id):
        self.id = id


@login_manager.user_loader
def load_user(user_id):
    return User(user_id)


@app.route('/')
def index():
    return 'Hello, World!'


@app.route('/login')
def login():
    return google.authorize(callback=url_for('authorized', _external=True))


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/authorized')
def authorized():
    resp = google.authorized_response()
    if resp is None:
        return 'Access denied: reason=%s error=%s' % (
            request.args['error_reason'],
            request.args['error_description']
        )
    access_token = resp['access_token']
    email = resp['email']
    user = User(email)
    login_user(user)
    return redirect(url_for('index'))


@google.tokengetter
def get_google_oauth_token():
    return session.get('google_token')


if __name__ == '__main__':
    app.run()