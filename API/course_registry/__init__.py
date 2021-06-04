from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy
from csv import reader
import markdown
import os

app = Flask(__name__)
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

# course model


class CourseModel(db.Model):
    identifier = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    units = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(600), nullable=False)
    other = db.Column(db.String(400), nullable=False)

    # def __repr__(self):
    #     return f"identifier = {identifier}, name = {name}, units = {units}, description = {description}, other={other}"

# db.create_all()


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


# counter = 0
# with open("final.csv", "r") as fl:
#     csv_reader = reader(fl)
#     for row in csv_reader:
#         if counter == 0:
#             counter += 1
#             pass
#         else:
#             # row[0] entire name of course including code
#             x = row[0].split()
#             y = " ".join(x[0:2])
#             courses[counter] = {"identifier": y[1],
#                                 "name": row[0],
#                                 "units": row[1],
#                                 "description": row[2],
#                                 "other": row[3]}

resouce_fields = {
    "identifier": fields.String,
    "name": fields.String,
    "units": fields.Integer,
    "description": fields.String,
    "other": fields.String
}


def abort_if_does_not_exist():
    abort(404, message="Course does not exisit")


def abort_if_exist():
    abort(409, message="Course already exits, use put req")


class Courses(Resource):
    @marshal_with(resouce_fields)
    def get(self, course_id=None):
        if course_id != None:
            # single course
            result = CourseModel.query.filter_by(identifier=course_id).first()
            if result and course_id:
                return result, 200
            else:
                abort_if_does_not_exist()
        else:
            # all courses
            print("ALL COURSES")
            test = {}
            courses = CourseModel.query.all()
            for idx, course in enumerate(courses):
                test[idx] = {"identifier": course.identifier,
                             "name": course.name,
                             "untis": course.units,
                             "description": course.description,
                             "other": course.other}
            print(test)
            return test

    @marshal_with(resouce_fields)
    def put(self, course_id):
        args = course_required_args.parse_args()
        result = CourseModel.query.filter_by(identifier=course_id).first()
        if result is not None:
            result.identifier = args["identifier"]
            result.name = args["name"]
            result.units = args["units"]
            result.description = args["description"]
            result.other = args["other"]
            db.session.commit()
        else:
            abort_if_does_not_exist()
        return result, 201

    @marshal_with(resouce_fields)
    def post(self, course_id):
        args = course_required_args.parse_args()
        result = CourseModel.query.filter_by(identifier=course_id).first()
        if result:
            abort_if_exist()

        course = CourseModel(
            identifier=course_id, name=args['name'], units=args['units'], description=args['description'], other=args['other'])
        db.session.add(course)
        db.session.commit()
        return course, 201

    def delete(self, course_id):
        result = CourseModel.query.filter_by(identifier=course_id).first()
        if result:
            db.session.delete(result)
            db.session.commit()
            return "", 204
        else:
            abort_if_does_not_exist()


api.add_resource(Courses, "/courses", "/courses/<string:course_id>")
