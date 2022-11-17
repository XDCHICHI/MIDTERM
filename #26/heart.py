from flask import Flask, jsonify, request
from flask import request, Response
from flask_jwt_extended import create_access_token
from database.models import User
from flask_restful import Resource
import datetime

class SignupApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200
        
class LoginApi(Resource):
    def post(self):
        body = request.get_json()
        user = User.objects.get(email=body.get('email'))
        authorized = user.check_password(body.get('password'))
        if not authorized:
            return {'error': "Email or password is invalid"}, 401
            
        expires = datetime.timedelta(days=7)
        access_token = create_access_token(identity=str(user.id), expires_delta=expires)
        return {'token': access_token}, 200

app = Flask(__name__)

heart_info = [{
"heart_id" : 1,
"date" : "November 17, 2022",
"heart_rate" : "60 bpm"
},
{
"temp_id" : 2,
"date" : "November 18, 2022",
"temperature" : "72 bpm"
}
]

@app.route('/heart', methods=['GET'])
def displayHeartRate():
    return jsonify(heart_info)
    

@app.route('/heart', methods=['POST'])
def addHeartRate():
    heart_rate = request.get_json()
    heart_info.append(heart_rate)
    return {'id': len(heart_info)}, 200
    
if __name__ == '__main__':
    app.run()
