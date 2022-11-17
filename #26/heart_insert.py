from flask import Flask, jsonify, request


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
    print(type(heart_rate))
    heart_info.append(heart_rate)
    return {'id': len(heart_info)}, 200
    
if __name__ == '__main__':
    app.run()
