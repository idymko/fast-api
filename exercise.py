"""
Write a simple script that creates a FastAPI app 
and defines a POST method that takes one path parameter, 
one query parameter, 
and a request body containing a single field. 

Have this function return all three in a dict. 

To get started, you can use the following snippet 
-- note the missing imports:

@app.post(...)
async def exercise_function(...):
  return {"path": path, "query": query, "body": body}

"""

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Value(BaseModel):
    value: int

@app.post("/{path}")
async def exercise_function(path: int, query: int, body: Value):
  return {"path": path, "query": query, "body": body}