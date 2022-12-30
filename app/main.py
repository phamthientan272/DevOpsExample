import logging

import uvicorn
from division import divide
from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from log import get_logger

app = FastAPI()
logger = get_logger()



class InputPayload(BaseModel):
    number_1 : float
    number_2: float

@app.post("/divide")
async def divide_number(input: InputPayload):
    number_1 = input.number_1
    number_2 = input.number_2
    result = divide(number_1, number_2)
    logger.info(f"Request: {input}. Response: {result}")
    
    if number_2 == 0:
        return JSONResponse(result, status_code=400)
    return JSONResponse(result, status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="localhost", port=5001, reload=True)
