
from flask import Flask,jsonify

app = Flask(__name__)


@app.route("/calculator/greeting", methods=['GET'])
def greeting():
    return 'Hello world'
    #return the greeting message
    return message

@app.route("/calculator/add", methods=['POST'])
def add():
    data = request.get_json()
    #retrive the number to be added
    num1 = data['num1']
    num2 = data['num2']

    #perform the addition operation
    result= num1+num2

    #create response object with the result
    response={
        'result':result
    }
    return jsonify(response)

@app.route("/calculator/subtract", methods=['POST'])
def subtract():
    data = request.get_json()

    #perform the subtraction operation
    result= data['num1']-data['num2']

    #create a response object with the result
    response={
        'result':result
    }

    #create a response as JSON
    return jsonify(response)
    

if __name__ == '__main__':
    app.run(port=8080,host='0.0.0.0')
