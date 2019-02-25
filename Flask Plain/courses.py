from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')



courses_list = [
    {"id": 1, "name": "INF310"},
    {"id": 2, "name": "ECO400"},
    {"id": 3, "name": "ECO311"}
]

def get_course(course_id):
    flag = False
    for course in courses_list:
        if course["id"] == course_id:
            flag = True
            return jsonify(course)
    if flag == False:    
        return "Could not find this ID"


def delete_course(course_id):  
    flag = False
    for m in range(len(courses_list)): 
        if courses_list[m]['id'] == course_id: 
            del courses_list[m]
            flag = True
            return "Course was deleted successfully!"

    if flag == False:
        return "ID not Found!"


def put_course(course_id, name):  
    id_exist = False

    for n in courses_list:
        if n["id"] == course_id:
            n.update({'name': name})
            id_exist = True
            return jsonify(a)

    if id_exist == False:
        courses_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(courses_list)

    return jsonify(courses_list)
           
def post_course(course_id, name): 
    id_exist = False
    for i in range(len(courses_list)):
        if courses_list[i-1]['id'] == course_id:
            id_exist = True
    
    if id_exist == False:
        courses_list.append(dict({'id': course_id, 'name': name}))
        return jsonify(courses_list)
    else:
        return "ID already exist"
    
def get_courses():
    return jsonify(courses_list)




@app.route('/')
def main():
    return "Hello World!"



@app.route('/v3/course/<int:course_id>', methods=["GET","DELETE"])
def course_get(course_id):
    if request.method == "GET":
        return get_course(course_id)
    else:
        return delete_course(course_id)
   


@app.route('/v3/course/<int:course_id>/<name>', methods=["POST","PUT"])
def course_post(course_id, name):
    if request.method == "POST":
        return post_course(course_id, name)
    else:
return put_course(course_id, name)

@app.route('/v3/courses', methods=["GET"])
def course_retrieve():
return get_courses()