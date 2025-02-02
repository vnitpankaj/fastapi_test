""" 
fask in sysncronas designed 
when we call route seperatly then it will work parallay by creating differant thred (see funtion printme1 to printme4) BUT 
when in same route if multiple process are ther then each fun will exictue one after another (see funtion printme5)
as we need parralel work in ml mostly in llm hence  its better to use falsk for ml and for llm use fastapi
"""

from flask import Flask, request, jsonify
import time 
from datetime import datetime
app = Flask(__name__)

@app.route("/page1",methods=["GET"])

def printme1():
    start = datetime.now()
    time.sleep(30)
    end = datetime.now()
    # timediff = end - start
    return f"this is page 1 time taken starts at {start} and end at {end}"

@app.route("/page2",methods=["GET"])
def printme2():
    start = datetime.now()
    time.sleep(10)
    end = datetime.now()
    return f"this is page 2 time taken starts at {start} and end at {end}"

@app.route("/page3",methods=["POST"])
def printme3():
    payload = request.get_json()
    
    start = datetime.now()
    time.sleep(30)
    end = datetime.now()
    # timediff = end - start
    return f"this is page 3 time taken starts at {start} and end at {end}.\n {payload}"

@app.route("/page4",methods=["POST"])
def printme4():
    payload = request.get_json()
    start = datetime.now()
    time.sleep(10)
    end = datetime.now()
    return f"this is page 4 time taken starts at {start} and end at {end}. \n {payload}"


database_query = lambda x : sum(x)
api_call = lambda x : sum(x)
file_operation = lambda x : sum(x)

@app.route("/page5",methods=["GET"])
def printme5():
    # This entire sequence runs synchronously
    start1 = datetime.now()
    time.sleep(10)
    result1 = database_query(range(10000)) 
    
    start2 = datetime.now() 
    time.sleep(10)
    result2 = api_call(range(100))  
    
    start3 = datetime.now()   
    time.sleep(10)    
    result3 = file_operation(range(1000))  
    
    return f" first start at : {start1}\n scond start at : {start2}\n  third start at : {start3}\n "

if __name__ == "__main__":
    app.run()
 