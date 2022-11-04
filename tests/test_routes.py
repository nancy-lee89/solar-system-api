def test_get_all_planets_with_empty_db_returns_empty_list(client):
    response = client.get("/planet")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == []

def test_get_one_planet_with_populated_db_returns_planet_json(client, two_planets):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 200
    assert response_body == {
        "id": 1,
        "name":"Earth",
        "description":"Our planet",
        "size":1
    }


def test_get_one_planet_with_empty_db_returns_404(client):
    response = client.get("/planet/1")
    response_body = response.get_json()

    assert response.status_code == 404
    assert "message" in response_body

def test_post_one_planet_in_empty_creates_planet_id_1_in_db(client):
    response = client.post("/planet", json={
        "name":"Earth",
        "description":"Our planet",
        "size":1
    })
    response_body = response.get_json()

    assert response.status_code == 201
    assert "id" in response_body
    assert response_body["id"] == 1
