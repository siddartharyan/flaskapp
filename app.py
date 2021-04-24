import json
from flask import Flask,request,jsonify,Response
from flask_cors import CORS
from models.postmodel import User
app=Flask(__name__)
CORS(app)

@app.route('/getrecords',methods=['GET'])
def get_all():
    user=User.objects.all()
    if not user:
        return jsonify({"message":"no data exists"})
    else:
        return Response(user.to_json(),mimetype="application/json", status=200)
@app.route("/createrecord",methods=['POST'])
def createrecord():
    record=json.loads(request.data)
    user=User(name=record['name'],email=record['email'])
    user.save()
    return jsonify({"message":"user created"})
@app.route("/updaterecord",methods=['PUT'])
def updaterecord():
    record=json.loads(request.data)
    user=User.objects(name=record['name']).first()
    if not user:
        user=User(name=record['name'],email=record['email'])
        user.save()
        return jsonify({"message":"record created"})
    user.update(email=record['email'])
    return jsonify({"message":"record updated"})
@app.route("/deleterecord",methods=['DELETE'])
def deleterecord():
    record=json.loads(request.data)
    user=User.objects(name=record['name']).first()
    if not user:
        return jsonify({"message":"user doesnot exist"})
    user.delete()
    return jsonify({"message":"user deleted successfully"})
if __name__=="__main__":
    app.run(debug=True)