from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')



students_list = [
    {'id': 1, 'name': 'Lil Fame'},
    {'id': 2, 'name': 'Jacopo Sala'},
    {'id': 3, 'name': 'Ilda Duka'}
]


def get_student(student_id):
    flag = False
    for student in students_list:
        if student['id'] == student_id:
            flag = True
            return jsonify(student)
    if flag == False:    
        return 'Not able to find ID!'


def delete_student(student_id):
    flag = False
    for i in range(len(students_list)): 
        if students_list[i]['id'] == student_id: 
            del students_list[i]
            flag = True 
            return 'Student deleted successfully!'

    if flag == False:
        return 'Not able to find ID!'


def put_student(student_id, name):
    id_exist = False

    for n in students_list:
        if n['id'] == student_id:
            n.update({'name': name})
            id_exist = True
            return jsonify(n)

    if id_exist == False:
        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)

    return jsonify(students_list)

    
def post_student(student_id, name):
    id_exist = False
    for m in range(len(students_list)):
        if students_list[m-1]['id'] == student_id:
            id_exist = True
    
    if id_exist == False:
        students_list.append(dict({'id': student_id, 'name': name}))
        return jsonify(students_list)
    else:
        return 'ID already exist'
    

def get_students():
    return jsonify(students_list)

@app.route('/')
def main():
    return 'Hello World'


@app.route('/v2/student/<int:student_id>', methods=['GET','DELETE'])
def student_crud_gd(student_id):
    if request.method == 'GET':
        return get_student(student_id)
    else:
        return delete_student(student_id)
   


@app.route('/v2/student/<int:student_id>/<name>', methods=['POST','PUT'])
def student_crud_pp(student_id, name):
    if request.method == 'POST':
        return post_student(student_id, name)
    else:
        return put_student(student_id, name)



@app.route('/v2/students', methods=['GET'])
def student_r():
    return get_students()