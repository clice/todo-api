def test_register_new_user(client):
    response = client.post(
        "/auth/register", json={"email": "clice@example.com", "password": "senha123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "clice@example.com"
    assert "hashed_password" not in data  # nunca deve vazar a senha


def test_register_duplicate_email_fails(client):
    client.post("/auth/register", json={"email": "clice@example.com", "password": "senha123"})
    response = client.post(
        "/auth/register", json={"email": "clice@example.com", "password": "outrasenha"}
    )
    assert response.status_code == 400


def test_login_with_correct_credentials(client):
    client.post("/auth/register", json={"email": "clice@example.com", "password": "senha123"})
    response = client.post(
        "/auth/login", data={"username": "clice@example.com", "password": "senha123"}
    )
    assert response.status_code == 200
    assert "access_token" in response.json()


def test_login_with_wrong_password_fails(client):
    client.post("/auth/register", json={"email": "clice@example.com", "password": "senha123"})
    response = client.post(
        "/auth/login", data={"username": "clice@example.com", "password": "errada"}
    )
    assert response.status_code == 401


def test_me_requires_valid_token(client):
    response = client.get("/auth/me")
    assert response.status_code == 401  # sem token, deve barrar


def test_me_returns_current_user_with_valid_token(client):
    client.post("/auth/register", json={"email": "clice@example.com", "password": "senha123"})
    login_response = client.post(
        "/auth/login", data={"username": "clice@example.com", "password": "senha123"}
    )
    token = login_response.json()["access_token"]

    response = client.get("/auth/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == "clice@example.com"
