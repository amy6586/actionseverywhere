
# A very simple Flask Hello World app for you to get started with...

from flask import Flask, request
import git

app = Flask(__name__)

x_hub_signature = request.headers.get(‘X - Hub - Signature’)

if not is_valid_signature(x_hub_signature, request.data, w_secret):

@app.route('/update_server', methods=['POST'])
def webhook():
    if request.method == 'POST':
        repo = git.Repo('../amy6586/actionseverywhere')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400

@app.route('/')
def hello_world():
    return 'Hello from Flask! Is it working??'

