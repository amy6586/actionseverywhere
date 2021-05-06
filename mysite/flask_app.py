
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import git
import hmac
import hashlib
import os

w_secret = os.environ['SECRET_TOKEN']

app = Flask(__name__)

def is_valid_signature(x_hub_signature, data, private_key):
    """Verify webhook signature with private key."""
    hash_algorithm, github_signature = x_hub_signature.split('=', 1)
    algorithm = hashlib.__dict__.get(hash_algorithm)
    encoded_key = bytes(private_key, 'latin-1')
    mac = hmac.new(encoded_key, msg=data, digestmod=algorithm)

    return hmac.compare_digest(mac.hexdigest(), github_signature)


@app.route('/update_server', methods=['POST'])
def webhook():


    x_hub_signature = request.headers.get('X-Hub-Signature')
    if not is_valid_signature(x_hub_signature, request.data, w_secret):
        print('Deploy signature failed: {sig}'.format(sig=x_hub_signature))
        abort(418)


    if request.method == 'POST':
        repo = git.Repo('/home/amy6586/actionseverywhere')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/')
def hello_world():
    return 'Hello, Are we done yet? 1 2 3'

