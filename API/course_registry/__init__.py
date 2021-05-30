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

courses = {"jeff": {"age": 19, "gender": "male"},
           "lew": {"age": 9, "gender": "blah"}}


class HelloWorld(Resource):
    def get(self, course):
        # must return something serializable
        return courses[course]

    def post(self):
        return {"data": "posted", "message": "hoiiiii"}


# if you pass something in <> you will be able to access it within your request
# api.add_resource(HelloWorld, "/helloworld/<string:course>/<int:test>")


api.add_resource(HelloWorld, "/helloworld/<string:course>")
