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


class CourseModel(db.Model):
    identifier = db.Column(db.String(100), primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    units = db.Column(db.String(50), nullable=False)
    description = db.Column(db.String(600), nullable=False)
    other = db.Column(db.String(400), nullable=False)

    def __repr__(self):
        return f"identifier = {identifier}, name = {name}, units = {units}, description = {description}, other={other}"


course_required_args = reqparse.RequestParser()

course_required_args.add_argument(
    "identifier", type=str, help="Course code is required", required=True)
course_required_args.add_argument(
    "name", type=str, help="Full course name is required", required=True)
course_required_args.add_argument(
    "units", type=str, help="Number of units is required", required=True)
course_required_args.add_argument(
    "description", type=str, help="Course description is required", required=True)
course_required_args.add_argument(
    "other", type=str, help="Other content is required", required=True)

# Used to add all courses from csv to database ---------------------------

# courses, counter = {}, 0
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
#             print(y)
#             course = CourseModel(
#                 identifier=y, name=row[0], units=row[1], description=row[2], other=row[3])
#             db.session.add(course)
#             db.session.commit()
#             counter += 1

# ----------------------------------------------------------------------------

resouce_fields = {
    "identifier": fields.String,
    "name": fields.String,
    "units": fields.String,
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
            all_courses = []
            courses = CourseModel.query.all()
            for course in enumerate(courses):
                all_courses += [{"identifier": course[1].identifier,
                                 "name": course[1].name,
                                 "units": course[1].units,
                                 "description": course[1].description,
                                 "other": course[1].other}]
            return all_courses, 200

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
    def post(self):
        args = course_required_args.parse_args()
        result = CourseModel.query.filter_by(
            identifier=args["identifier"]).first()
        if result:
            abort_if_exist()

        course = CourseModel(
            identifier=args["identifier"], name=args['name'], units=args['units'], description=args['description'], other=args['other'])
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
