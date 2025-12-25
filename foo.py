# foo.py

"""
In this exercise we are applying the software engineering best practice of testing to our work with APIs. 
We do so by leveraging FastAPI's testing framework which has tight integration with the ubiquitous pytest module. 
This allows us to have confidence in the behavior of our API before deploying it to production.

Install FastAPI and uvicorn in a conda environment if you haven't already. 

Run API Server: uvicorn foo:app --reload

"""

from fastapi import FastAPI

app = FastAPI()

@app.get("/items/{item_id}")
async def get_items(item_id: int, count: int = 1):
    return {"fetch": f"Fetched {count} of {item_id}"}

# Usage
#   GET: http://127.0.0.1:8000/items/10?count=2
#   RETURNS: Fetched 2 of 10