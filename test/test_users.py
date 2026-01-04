import jwt
from jwt.exceptions import InvalidTokenError
from app import schemas,models
# from .database import client, session
import pytest
from app.config import settings

# def test_root(client):
#     res = client.get("/")
#     print(res.json().get('Hello'))
#     assert res.json().get('Hello') == 'Wellcom to FastApi updated'
#     assert res.status_code == 200

    
# we use /users/ not /users because prefix is /user and path is /
def test_create_user(client):
    res = client.post(
        "/users/", json={"email": "abdullah@gmail.com", "password": "abc123"}
    )
    new_user = schemas.UserOut(**res.json())
    assert new_user.email == "abdullah@gmail.com"
    assert res.status_code == 201
    
    
def test_login_user(client, test_user):
    res = client.post(
        "/login", data={"username": test_user['email'], "password": test_user['password']}
    )
    login_res = schemas.Token(**res.json())
    payload = jwt.decode(login_res.access_token,settings.secret_key, algorithms=[settings.algorithm])
    id = payload.get("user_id")
    assert id == test_user['id']
    assert login_res.token_type == "bearer"
    assert res.status_code == 200
    

# @pytest.mark.parametrize("email, password, status_code",[
#     ('abdullah@gmail.com', 'abc123', 200),
#     ('saadi@outlook.com', 'pwd123', 403),
#     (None, 'pwd123', 422)
# ])    
# def test_incorrect_login(test_user, client, email, password, status_code):
#     res = client.post("/login", data={"username": email, "password": password})
    
#     assert res.status_code == status_code
    # assert res.json().get('detail') == 'Invalid Credentials'
    
    