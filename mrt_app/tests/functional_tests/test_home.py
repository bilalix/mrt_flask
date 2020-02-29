def test_home_page(test_client):
    """
    GIVEN a Flask application
    WHEN the '/' page is requested (GET)
    THEN check the response is valid
    """
    response = test_client.get('/')
    # print(response.data)
    assert response.status_code == 200
    assert b"Login" in response.data
