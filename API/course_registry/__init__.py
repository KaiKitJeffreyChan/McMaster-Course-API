from flask import Flask
from flask_restful import Api, Resource
import markdown
import os

# instance of flask
app = Flask(__name__)
api = Api(app)

# @app.route('/')
# def index():
#     """open documentation"""

#     # open the readmee
#     with open(os.path.dirname(app.root_path) + '/README.md', 'r') as markdown_file:

#         content = markdown_file.read()

#         return markdown.markdown(content)


class HelloWorld(Resource):
    def get(self):
        # must return something serializable
        return {"data": "hello world", "message": "hoiiiii"}


api.add_resource(HelloWorld, "/helloworld")
