from flask import Flask
from flask_restful import Api, Resource, reqparse, abort
from flask_sqlalchemy import SQLAlchemy
from csv import reader
import markdown
import os

app = Flask(__name__)
api = Api(app)

course_required_args = reqparse.RequestParser()

course_required_args.add_argument(
    "identifier", type=str, help="Course code is required", required=True)
course_required_args.add_argument(
    "name", type=str, help="Full course name is required", required=True)
course_required_args.add_argument(
    "units", type=int, help="Number of units is required", required=True)
course_required_args.add_argument(
    "description", type=str, help="Course description is required", required=True)
course_required_args.add_argument(
    "other", type=str, help="Other content is required", required=True)


courses, counter = {}, 0
with open("final.csv", "r") as fl:
    csv_reader = reader(fl)
    for row in csv_reader:
        if counter == 0:
            counter += 1
            pass
        else:
            x = row[0].split()
            courses[row[0]] = {"identifier": x[1],
                               "name": row[0],
                               "units": row[1],
                               "description": row[2],
                               "other": row[3]}


def abort_if_not_exits(course_id):
    if course_id not in courses:
        abort(404, message="course id is not valid or doesnt exist")


def abort_if_exists(course_id):
    if course_id in courses:
        abort(409, message="course exists already, make a put request")


class Courses(Resource):

    def get(self, course_id=None):
        if course_id != None:
            abort_if_not_exits(course_id)
            return courses[course_id], 200
        else:
            return courses, 200

    # edit a selected course tha already exits
    def put(self, course_id):
        abort_if_not_exits(course_id)
        args = course_required_args.parse_args()
        courses[course_id] = args
        return courses[course_id], 201

    # post will not work on existing
    def post(self):
        args = course_required_args.parse_args()
        abort_if_exists(args[next(iter(args))])
        courses[args[next(iter(args))]] = args
        return courses[args[next(iter(args))]], 201

    def delete(self, course_id):
        abort_if_not_exits(course_id)
        del courses[course_id]
        return "", 204


api.add_resource(Courses, "/courses", "/courses/<string:course_id>")
