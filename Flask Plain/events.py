from flask import Flask, request, jsonify

app = Flask(__name__, static_url_path='/static')



event_list = [
    {"id": 1, "event_name": "Spring Fest"},
    {"id": 2, "event_name": "Colors Festival"},
    {"id": 3, "event_name": "Carnivals"}
]


def get_event(event_id):
    flag = False
    for name in event_list:
        if event["id"] == event_id:
            flag = True
            return jsonify(event)
    if flag == False:    
        return "Not able to find ID"


def delete_event(event_id):
    flag = False
    for i in range(len(event_list)): 
        if event_list[i]['id'] == event_id: 
            del event_list[i] 
            flag = True
            return "Event deleted successfully!"

    if flag == False:
        return "Not able to find ID"


def put_event(event_id, name):
    id_exist = False

    for a in event_list:
        if a["id"] == event_id:
            a.update({'event_name': name})
            id_exist = True
            return jsonify(a)

    if id_exist == False:
        event_list.append(dict({'id': event_id, 'event_name': name}))
        return jsonify(event_list)

    return jsonify(event_list)


def post_event(event_id, event):
    id_exist = False
    for i in range(len(event_list)):
        if event_list[i-1]['id'] == event_id:
            id_exist = True
    
    if id_exist == False:
        event_list.append(dict({'id': event_id, 'event_name': name}))
        return jsonify(event_list)
    else:
        return "ID already exist"
    

def get_events():
    return jsonify(event_list)




@app.route('/')
def main():
    return "Hello World"



@app.route('/v1/event/<int:event_id>', methods=["GET","DELETE"])
def event_crud_gd(event_id):
    if request.method == "GET":
        return get_event(event_id)
    else:
        return delete_event(event_id)
   


@app.route('/v1/event/<int:event_id>/<event>', methods=["POST","PUT"])
def event_crud_pp(event_id, event):
    if request.method == "POST":
        return post_event(event_id, event)
    else:
        return put_event(event_id, event)



@app.route('/v1/events', methods=["GET"])
def event_retrieve():
return get_events()