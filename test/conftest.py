from fastapi.testclient import TestClient
import pytest
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db,Base
from alembic import command
from app.auth2 import create_access_token
from app import models



# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:1234567@localhost:5432/postgres_test'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# Base = declarative_base()

# def overrid_get_db():
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# app.dependency_overrides[get_db] = overrid_get_db

@pytest.fixture(scope='function')
def session():
     #run our code before we run our test
    Base.metadata.drop_all(bind = engine)
    Base.metadata.create_all(bind = engine)
    db = TestingSessionLocal()
    try:
        yield db
    finally:
        db.close()
    # command.downgrade("base")
    # run out code after out test finishes

@pytest.fixture(scope='function')
def client(session):
    def overrid_get_db():
        try:
            yield session
        finally:
            session.close()
    app.dependency_overrides[get_db] = overrid_get_db
    yield TestClient(app)
    
    
@pytest.fixture
def test_user(client):
    user_data = {"email": "abdullah@gmail.com", "password": "abc123"}
    res = client.post("/users/", json=user_data)
    
    assert res.status_code == 201
    print(res.json())
    new_user = res.json()
    new_user['password'] = user_data['password']
    return new_user


@pytest.fixture
def token(test_user):
    #print(test_user)
    create_access_token({"user_id": test_user['id']})



@pytest.fixture    
def authorized_client(client,test_user):
    # print(**client.headers)
    # client.headers.update = {
    #     # **client.headers,
    #     "Authorization": f"Bearer {token}"
    # }
    # print(client)
    # return client
    token = create_access_token({"user_id": test_user['id']})
    # Add Authorization header to the client
    client.headers.update({
        "Authorization": f"Bearer {token}"
    })
    return client



@pytest.fixture
def test_posts(test_user, session):
    psots_data = [
        {
            "title": "first title",
            "content": "first content",
            "owner_id": test_user['id']
        },
        {
            "title": "2nd title",
            "content": "2nd content",
            "owner_id": test_user['id']
        },
        {
            "title": "3rd title",
            "content": "3rd content",
            "owner_id": test_user['id']
        }]
    
    def create_user_model(post):
        return models.Post(**post)
    
    post_map = map(create_user_model,psots_data)
    posts = list(post_map)
    
    session.add_all(posts)
    # session.add_all([models.Post(title="first title", content="first content", owner_id=test_user['id']),
    #                  models.Post(title="2nd title", content="2nd content" , owner_id=test_user['id']),
    #                  models.Post(title="3rd title", content="3rd content" , owner_id=test_user['id'])])
    session.commit()
    return session.query(models.Post).all()
    
    
    
