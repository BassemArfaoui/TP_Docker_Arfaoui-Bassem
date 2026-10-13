from unittest.mock import patch
from fastapi.testclient import TestClient
import app as app_module

client = TestClient(app_module.app)

def test_index_increments_counter_and_shows_message():
    with patch.object(app_module.cache, "incr", return_value=7) as incr:
        response = client.get("/")
    incr.assert_called_once_with("hits")
    assert response.status_code == 200
    assert "vue 7 fois" in response.text
    assert "Je suis le conteneur" in response.text


    