from flask_restful import Resource
from flask import jsonify

courses_list = [
    {'id': 1, 'name': 'ECO311'},
    {'id': 2, 'name': 'ECO400'},
    {'id': 3, 'name': 'INF310'}
]

class First(Resource):
    

    
    def put(self,course_id,name): 
        id_exist = False

        for m in courses_list:
            if m['id'] == course_id:
                m.update({'name': name})
                id_exist = True
                return jsonify(m)

        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)

        return jsonify(courses_list)

def post(self,course_id,name): 

        id_exist = False
        for n in range(len(courses_list)):
            if courses_list[n-1]['id'] == course_id:
                id_exist = True
    
        if id_exist == False:
            courses_list.append(dict({'id': course_id, 'name': name}))
            return jsonify(courses_list)
        else:
            return 'ID already exists'

    

class Second(Resource):

    def get(self, course_id):  
        flag = False
        for courses in courses_list:
            if courses['id'] == course_id:
                flag = True
                return jsonify(courses)
        if flag == False:    
            return 'Not able to find ID!'
       
    def delete(self, course_id):     
        flag = False
        for a in range(len(courses_list)): 
            if courses_list[a]['id'] == course_id: 
                del courses_list[a]
                flag = True
                return 'Course deleted successfully!'

        if flag == False:
            return 'Not able to find ID!'

class all_courses(Resource):
    def get(self):
return jsonify(courses_list)