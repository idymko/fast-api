# test_foo.py

"""
When running tests with pytest, especially in the context of testing a FastAPI 
application using TestClient, you do not need to run the Uvicorn server with 
the command uvicorn foo:app --reload. 

TestClient Usage: 
The TestClient from FastAPI is designed to simulate requests to your application without needing to run a separate server. 
It creates an instance of your FastAPI application and allows you to make requests to it directly in your tests.

Isolation: 
Running tests with pytest using TestClient allows for isolated testing of your application logic. 
You can test various endpoints and their responses without the overhead of starting and managing an actual server.

Speed: Since you're not starting a server, the tests can run much faster. 
This is particularly useful when you have many tests to run, as it reduces the time needed for setup and teardown.

Environment: The tests run in a controlled environment where you can easily mock 
dependencies or set up specific conditions for your tests without affecting the actual running application.

"""

from fastapi.testclient import TestClient
import warnings 
import pytest

from foo import app # import our app
client = TestClient(app)

@pytest.mark.anyio
async def test_get_path() -> None:
    
    r = client.get("/items/42")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 1 of 42"}

@pytest.mark.anyio
async def test_get_path_query() -> None:
    r = client.get("/items/42?count=5")
    assert r.status_code == 200
    assert r.json() == {"fetch": "Fetched 5 of 42"}
    
@pytest.mark.anyio
async def test_get_malformed():
    r = client.get("/items")
    assert r.status_code != 200