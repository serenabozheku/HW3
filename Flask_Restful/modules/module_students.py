from flask_restful import Resource
from flask import jsonify

students_list = [
    {'id': 1, 'student': 'Lil Fame'},
    {'id': 2, 'student': 'Jacopo Sala'},
    {'id': 3, 'student': 'Ilda Duke'}
]

class First(Resource):
    

    
    def put(self,student_id,name):   
        id_exist = False

        for m in students_list:
            if m['id'] == student_id:
                a.update({'name': name})
                id_exist = True
                return jsonify(a)

        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)

        return jsonify(students_list)

def post(self,student_id,name): 

        id_exist = False
        for n in range(len(students_list)):
            if students_list[n-1]['id'] == student_id:
                id_exist = True
    
        if id_exist == False:
            students_list.append(dict({'id': student_id, 'name': name}))
            return jsonify(students_list)
        else:
            return 'ID already exist'

    

class Second(Resource):

    def get(self, student_id):  
        flag = False
        for student in students_list:
            if student['id'] == student_id:
                flag = True
                return jsonify(student)
        if flag == False:    
            return 'Not able to find ID!'
       
    def delete(self, student_id):     
        flag = False
        for i in range(len(students_list)): 
            if students_list[i]['id'] == student_id: 
                del students_list[i]
                flag = True
                return 'Student deleted successfully!'

        if flag == False:
            return 'Not able to find ID!'

class students(Resource):
    def get(self):
        return jsonify(students_list)
