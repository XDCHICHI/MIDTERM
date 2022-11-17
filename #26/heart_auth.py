from flask import Flask, jsonify, request
from flask import request, Response
from flask_jwt_extended import create_access_token
from flask_restful import Resource
from flask_bcrypt import generate_password_hash, check_password_hash
import datetime

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
    user = {"email":"lorencechichi@gmail.com", "password":"lorencechi9"}

    heart_rate = request.get_json()
    
    password = generate_password_hash(heart_rate['password']).decode('utf-8')
    
    
    authorized = check_password_hash(password, "lorencechi9")
    if(not authorized or not heart_rate['email']=="lorencechichi@gmail.com"):
        return {'error': "Email or password is invalid"}, 401
    else:
         heart_rate.pop("email")
         heart_rate.pop("password")
         heart_info.append(heart_rate)
         return {'id': len(heart_info)}, 200
         
         
    
if __name__ == '__main__':
    app.run()
