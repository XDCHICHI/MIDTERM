from flask import Flask, jsonify, request


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
    
@app.route('/heart', methods=['GET','POST'])
def updateIdHearts():
    update_info = request.get_json()
    for i in heart_info:
        if(i['heart_id'] == update_info['updated_id']):
            i['heart_id']= update_info['heart_id']
            i['date'] = update_info['date']
            i['heart_rate']= update_info['heart_rate']
            return {'id': len(heart_info)}, 200
    return 'UPDATE FAILED'
    
    
if __name__ == '__main__':
    app.run()
