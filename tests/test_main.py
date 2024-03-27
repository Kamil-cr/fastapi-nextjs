from fastapi.testclient import TestClient
from fastapi_nextjs.api.main import app

client = TestClient(app=app)

def test_read_root():
    response = client.get("/api/python")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}