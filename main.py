"""
To run our app, we will use uvicorn in our shell: uvicorn main:app --reload.

The --reload allows you to make changes to your code and have them instantly 
deployed without restarting uvicorn.

By default, our app will be available locally at http://127.0.0.1:8000.
The output of the above snippet will return a 
JSON response as {"greeting": "Hello World!"} 
on the browser (URL http://127.0.0.1:8000).

"""


from fastapi import FastAPI

# Instantiate the app.
app = FastAPI()

# Define a GET on the specified endpoint.
@app.get("/")
async def say_hello():
    return {"greeting": "Hello World!"}

