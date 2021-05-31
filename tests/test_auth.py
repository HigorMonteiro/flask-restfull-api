def test_register(client):
    data = {
      "email": "higorvmonteiro2@gmail.com",
      "password": "12345"
    }

    response = client.post("/api/auth/register", data=data)
    result = response.get_json()
    assert result['message'] == "User successfully registered"