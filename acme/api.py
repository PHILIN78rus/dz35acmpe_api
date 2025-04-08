from flask import Flask, request
import model

app = Flask(__name__)

class ApiException(Exception):
    pass

def _from_raw(raw_note: str) -> model.Note:
    parts = raw_note.split("|")
    if len(parts) == 2:
        note = model.Note()
        note.id = None
        note.title = str(parts[0])
        note.text = str(parts[1])
        return note
    elif len(parts) == 3:
        note = model.Note()
        note.id = str(parts[0])
        note.title = str(parts[1])
        note.text = str(parts[2])
        return note
    else:
        raise ApiException(f"invalid RAW note data {raw_note}")
    
def _to_raw(note: model.Note) -> str:
    if note.id is None:
        return f"{note.title}|{note.text}"
    else:
        return f"{note.id}|{note.title}|{note.text}"
API_ROOT = "/api/v1"
NOTE_API_ROOT = API_ROOT + "/note"

@app.route(NOTE_API_ROOT + '/', methods = ['POST'])
def create():
    data = str(request.get_data())
    note = _from_raw(data)
    return f"create {note.id} / {note.title} / {note.text}", 201

@app.route(NOTE_API_ROOT + '/', methods = ['GET'])
def list():
    return "list", 200

@app.route(NOTE_API_ROOT + '/<_id>/', methods = ['GET'])
def read(_id: str):
    note = model.Note
    note.id = 1
    note.title = "title_1"
    note.text = "text_1"
    raw_note = _to_raw(note)
    return raw_note, 200

@app.route(NOTE_API_ROOT + '/<_id>/', methods = ['PUT'])
def update(_id: str):
    return "update", 200

@app.route(NOTE_API_ROOT + '/<_id>/', methods = ['DELETE'])
def delete(_id: str):
    return "delete", 200


if __name__ == "__main__":
    app.run(debug=True)
