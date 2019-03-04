from flask import Flask, jsonify
from flask_restful import Resource, Api
from modules.module_course import First_course, Second_course, all_courses
from modules.module_students import First_student, Second_student, all_students
from modules.module_events import First_event, Second_event, all_events


app = Flask(__name__)

api = Api(app)

@app.route('/')
def home():
    return 'Hello,  World!'

 
api.add_resource(First_course, '/course/<int:course_id>/<name>')
api.add_resource(Second_course, '/course/<int:course_id>/')

api.add_resource(First_student, '/student/<int:student_id>/<name>')
api.add_resource(Second_student, '/student/<int:student_id>/')

api.add_resource(First_event, '/event/<int:event_id>/<event_name>')
api.add_resource(Second_event, '/event/<int:event_id>/')


api.add_resource(all_courses, '/courses/')
api.add_resource(all_students, '/students/')
api.add_resource(all_events, '/events/')