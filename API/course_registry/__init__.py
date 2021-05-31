from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from csv import reader
import markdown
import os

# instance of flask
app = Flask(__name__)
api = Api(app)

# rename this
course_put_args = reqparse.RequestParser()

course_put_args.add_argument(
    "identifier", type=str, help="Course code is required", required=True)
course_put_args.add_argument(
    "name", type=str, help="Full course name is required", required=True)
course_put_args.add_argument(
    "units", type=int, help="Number of units is required", required=True)
course_put_args.add_argument(
    "description", type=str, help="Course description is required", required=True)
course_put_args.add_argument(
    "other", type=str, help="Other content is required", required=True)


courses = {}
counter = 0

with open("final.csv", "r") as fl:
    csv_reader = reader(fl)

    for row in csv_reader:
        if counter == 0:
            counter += 1
        elif counter < 15:
            x = row[0].split()
            courses[x[1]] = {"identifier": x[1],
                             "name": row[0],
                             "units": row[1],
                             "description": row[2],
                             "other": row[3]}
            counter += 1
        else:
            break


def abort_if_not_exits(course_id):
    if course_id not in courses:
        abort("course id is not valid")


class Courses(Resource):
    # get all courses first index, second index is desired course
    def get(self, course_id=None):
        if course_id != None:
            return courses[course_id]
        else:
            return courses

    # created sucessfully, edit a selected course
    def put(self, course_id):
        args = course_put_args.parse_args()
        courses[course_id] = args
        return courses[course_id], 201

    def post(self, course_id):
        args = course_put_args.parse_args()
        courses[next(iter(args))] = args
        return courses[next(iter(args))], 201


# if you pass something in <> you will be able to access it within your request
# api.add_resource(HelloWorld, "/helloworld/<string:course>/<int:test>")
api.add_resource(Courses, "/courses/", "/courses/<string:course_id>")

# api.add_resource(Courses, "/courses/<string:course>", endpoint="course")
