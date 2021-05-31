def test_it_returns_status_code_401_on_latters_router(client):
    """
    401 StatusCode without authorization
    """
    response = client.get("/api/letters")
    assert response.status_code == 401