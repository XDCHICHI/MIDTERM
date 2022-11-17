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
    
@app.route('/heart', methods=['DELETE','POST'])
def deleteIdHearts():
    delete_info = request.get_json()
    index = 0
    for i in heart_info:
        if(i['heart_id'] == delete_info['id_to_delete']):
            heart_info.pop(index)
            return 'Temperature was successfully deleted', 200
        index += 1
    return 'NON EXISTING ID, DELETE FAILED'
    
    
if __name__ == '__main__':
    app.run()
