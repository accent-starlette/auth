def test_get(client):
    response = client.get("/auth/password/reset/done")
    assert response.status_code == 200
    assert "request" in response.context
