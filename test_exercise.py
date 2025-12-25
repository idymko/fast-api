import json 
from fastapi.testclient import TestClient
import warnings 
import pytest 

from exercise import app # import our app
client = TestClient(app)

@pytest.mark.anyio
async def test_post():
    warnings.filterwarnings("ignore", category=DeprecationWarning)
    data = json.dumps({"value": 10})
    r = client.post("/42?query=5", data=data)
    print(r.json())
    assert r.json()["path"] == 42
    assert r.json()["query"] == 5
    assert r.json()["body"] == {"value": 10}