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
    
if __name__ == '__main__':
    app.run()
    
