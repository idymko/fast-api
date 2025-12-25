## Create Virtual Environment 

Steps:
* `conda create --name fast-api`
* `conda activate fast-api`
* `conda install pip`
* `pip install -r requirements.txt`

## Execution

To run our app, we will use uvicorn in our shell: 
`uvicorn main:app --reload`
* Name of the function: `main`
* Name of the app in that function: `app`
* The `--reload` allows you to make changes to your code and have them instantly 
deployed without restarting uvicorn.

By default, our app will be available locally at http://127.0.0.1:8000.


## API Methods

### GET Method

* Purpose: The GET method is used to retrieve data from the server. It requests data from a specified resource.
* Idempotent: GET requests are idempotent, meaning that making the same request multiple times will not change the state of the resource on the server.
* Data in URL: Any parameters or data sent with a GET request are included in the URL (as query parameters). For example: `/items?item_id=123`.
* Caching: Responses to GET requests can be cached by browsers and intermediate proxies, which can improve performance for frequently requested resources.
* No Body: GET requests do not have a body. Any data sent is included in the URL.

### POST Method

* Purpose: The POST method is used to send data to the server to create or update a resource. It submits data to be processed to a specified resource.
* Not Idempotent: POST requests are not idempotent, meaning that making the same request multiple times may result in different outcomes (e.g., creating multiple entries in a database).
* Data in Body: Data sent with a POST request is included in the body of the request, allowing for larger amounts of data to be sent compared to GET.
* No Caching: Responses to POST requests are generally not cached, as they often result in changes to the server state.
* Use Cases: Common use cases for POST include submitting forms, uploading files, or creating new resources.

## Testing 


When running tests with pytest, especially in the context of testing a FastAPI application using TestClient, you do not need to run the Uvicorn server with the command `uvicorn foo:app --reload`. 

* TestClient Usage: The TestClient from FastAPI is designed to simulate requests to your application without needing to run a separate server. It creates an instance of your FastAPI application and allows you to make requests to it directly in your tests.

* Isolation: Running tests with pytest using TestClient allows for isolated testing of your application logic. 
You can test various endpoints and their responses without the overhead of starting and managing an actual server.

* Speed: Since you're not starting a server, the tests can run much faster. 
This is particularly useful when you have many tests to run, as it reduces the time needed for setup and teardown.

* Environment: The tests run in a controlled environment where you can easily mock 
dependencies or set up specific conditions for your tests without affecting the actual running application.
