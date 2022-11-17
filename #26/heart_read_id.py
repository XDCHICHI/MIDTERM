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


@app.route('/heart', methods=['GET','POST'])
def displayIdHearts():
    display_id = request.get_json()
    for i in heart_info:
        if(i['heart_id'] == display_id['find_id']):
            return jsonify(i)
    return 'NOT AN EXISTING ID'
    
    
if __name__ == '__main__':
    app.run()
