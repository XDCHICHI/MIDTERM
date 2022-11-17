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
"heart_id" : 2,
"date" : "November 18, 2022",
"heart_rate" : "72 bpm"
}
]

@app.route('/heart', methods=['GET'])
def displayHeartRate():
    return jsonify(heart_info)
    
@app.route('/heart/insert', methods=['POST'])
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
         
@app.route('/heart/delete', methods=['DELETE','POST'])
def deleteIdHearts():
    delete_info = request.get_json()
    index = 0
    user = {"email":"lorencechichi@gmail.com", "password":"lorencechi9"}


    
    password = generate_password_hash(delete_info['password']).decode('utf-8')
    
    
    authorized = check_password_hash(password, "lorencechi9")
    if(not authorized or not delete_info['email']=="lorencechichi@gmail.com"):
        return {'error': "Email or password is invalid"}, 401
    else:
    
        for i in heart_info:
           if(i['heart_id'] == delete_info['id_to_delete']):
              heart_info.pop(index)
              return 'Temperature was successfully deleted', 200
           index += 1
        return 'NON EXISTING ID, DELETE FAILED'
    
@app.route('/heart/update', methods=['GET','POST'])
def updateIdHearts():
    update_info = request.get_json()
    user = {"email":"lorencechichi@gmail.com", "password":"lorencechi9"}


    
    password = generate_password_hash(update_info['password']).decode('utf-8')
    
    
    authorized = check_password_hash(password, "lorencechi9")
    if(not authorized or not update_info['email']=="lorencechichi@gmail.com"):
        return {'error': "Email or password is invalid"}, 401
    else:
        for i in heart_info:
          if(i['heart_id'] == update_info['updated_id']):
               i['heart_id']= update_info['heart_id']
               i['date'] = update_info['date']
               i['heart_rate']= update_info['heart_rate']
               return {'id': len(heart_info)}, 200
        return 'UPDATE FAILED'
    
if __name__ == '__main__':
    app.run()
