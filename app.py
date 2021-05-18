import json
import random
import time
import flask
import ast
from flask import request, jsonify

app = flask.Flask(__name__)


@app.route('/', methods=['GET','POST'])
def Ec2pi_estimator():
    start = time.time()
    print("outside request: ",request)

    if request.method == "POST":
        print("inside request",request.get_data().decode("utf-8"))
        response = request.get_data().decode("utf-8")
        # print(type(ast.literal_eval(response)))
        response = ast.literal_eval(response)
        # print(response)

        s = int(response["S"])
        pid = int(response["pid"])
        d = int(response["D"])
        q = int(response["Q"])
        
        values=[]    
        shots = s
        incircle = 0
        for i in range(1, shots+1):
            random1 = random.uniform(-1.0, 1.0)  
            random2 = random.uniform(-1.0, 1.0)  
            if( ( random1*random1 + random2*random2 ) < 1 ):
                incircle += 1
            if i % q == 0:
                values.append([incircle,i])
        elapsed_time = time.time() - start
        return jsonify({
            "thread_id":json.dumps(pid),
            "values":json.dumps(values),
            "elapsed_time": json.dumps(elapsed_time),
        })
    else:
        return jsonify({
            "message":"The api works bro!!",
        })


app.run()

# curl -d '{"pid": 2,"D": 4,"Q": 10000,"S": 200000}' http://127.0.0.1:5000

# curl -d '{"pid": 2,"D": 4,"Q": 10000,"S": 200000}' http://172.17.0.3:5000

# curl -d '{"pid": 2,"D": 4,"Q": 10000,"S": 200000}' https://54.236.34.139/