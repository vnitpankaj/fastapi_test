""" 
fastapi works as sync mode as defalult as we dinadt ask iyt to asyn (exp code page1)

"""

from fastapi import FastAPI
import time 
from datetime import datetime
import asyncio

app = FastAPI()


async def async_operation(operation_name: str, delay: int):
    start_time = datetime.now().strftime("%H:%M:%S.%f")
    print(f"Starting {operation_name} at {start_time}")
    await asyncio.sleep(delay)
    end_time = datetime.now().strftime("%H:%M:%S.%f")
    return {
        "operation": operation_name,
        "start_time": start_time,
        "end_time": end_time,
        "delay_seconds": delay
    }
    
@app.get("/parallel")
async def parallel_operations():
    start_time = datetime.now().strftime("%H:%M:%S.%f")
    
    # Perform three operations in parallel
    results = await asyncio.gather(
        async_operation("Operation 1", 10),
        async_operation("Operation 2", 7),
        async_operation("Operation 3", 5)
    )
    
    end_time = datetime.now().strftime("%H:%M:%S.%f")
    
    return {
        "endpoint_start_time": start_time,
        "endpoint_end_time": end_time,
        "operations": results
    }
    
@app.get("/sequence")
async def seqme():
    start_time = datetime.now().strftime("%H:%M:%S.%f")
    
    s1 =  await async_operation("Operation 1", 10)
    s2 =  await async_operation("Operation 2", 7)
    s3 =  await async_operation("Operation 3", 5)
    results = {"s1" : s1, "s2" : s2, "s3" : s3 }
    end_time = datetime.now().strftime("%H:%M:%S.%f")
    
    return {
        "endpoint_start_time": start_time,
        "endpoint_end_time": end_time,
        "operations": results
    }
    
@app.get("/mix")
async def seqme():
    start_time = datetime.now().strftime("%H:%M:%S.%f")
    
    s1 =  await async_operation("Operation 1", 10)
    
    s2 =  await asyncio.gather(async_operation("Operation 2", 7),
              async_operation("Operation 3", 5))
    
    results = {"s1":s1, "s2":s2}
    
    end_time = datetime.now().strftime("%H:%M:%S.%f")
    
    return {
        "endpoint_start_time": start_time,
        "endpoint_end_time": end_time,
        "operations": results
    }
    
@app.post("/testpost")
async def postme(dict_var : dict):
    s = time.time()
    s2 =  await asyncio.gather(async_operation(dict_var["f1"]["name"], dict_var["f1"]["time"]),
              async_operation(dict_var["f2"]["name"], dict_var["f2"]["time"]))
    e = time.time() - s
    return f"total time taken : {e}"