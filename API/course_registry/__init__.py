from flask import Flask
import markdown
import os

# instance of flask
app = Flask(__name__)


@app.route('/')
def index():
    """open documentation"""

    # open the readmee
    with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

        content = markdown_file.read()

        return markdown.markdown(content)
