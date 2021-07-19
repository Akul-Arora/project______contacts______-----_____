from flask import Flask,jsonify,Request
from flask.json import jsonify
from flask.wrappers import Request
from werkzeug.wrappers import request 
app=Flask(__name__)
tasks=[
{
    "id":1,
    "name": "Akul Arora",
    "number":"9876543210",
    "done":False
},
{
    "id":2,
    "name": "Koel Ma'am",
    "number":"0123456789",
    "done":False
},
{
    "id":3,
    "name": "Mom",
    "number":"1234567890",
    "done":False
},
{
    "id":4,
    "name": "Dad",
    "number":"0987654321",
    "done":False
}
]

@app.route("/")
def hello_world():
    return "Hello World!!!!"

@app.route("/add-data",methods=["POST"])
def addingtask():
    if not request.json:
        return jsonify({'status':'error',
        "message":"please provide valid contact details"},400)

    task={'id':tasks[-1]['id']+1,
    'title':request.json['title'],
    'description':request.json.get('description',""),
    'done':False
    }    
    tasks.append(task)
    return jsonify({
        'status':'success',
        "message":"contact is added succesfully"})
        
            
@app.route("/get-data")
def gettask():
    return jsonify({"data":tasks})



if(__name__ == "__main__"):
    app.run(debug=True)