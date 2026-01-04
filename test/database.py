from fastapi.testclient import TestClient
import pytest
from app.main import app
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings
from app.database import get_db,Base
from alembic import command



# SQLALCHEMY_DATABASE_URL = f'postgresql://postgres:1234567@localhost:5432/postgres_test'
# SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}_test'

# engine = create_engine(SQLALCHEMY_DATABASE_URL)

# TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


# # Base = declarative_base()

# # def overrid_get_db():
# #     db = TestingSessionLocal()
# #     try:
# #         yield db
# #     finally:
# #         db.close()

# # app.dependency_overrides[get_db] = overrid_get_db

# @pytest.fixture(scope='function')
# def session():
#      #run our code before we run our test
#     Base.metadata.drop_all(bind = engine)
#     Base.metadata.create_all(bind = engine)
#     db = TestingSessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()
#     # command.downgrade("base")
#     # run out code after out test finishes

# @pytest.fixture(scope='function')
# def client(session):
#     def overrid_get_db():
#         try:
#             yield session
#         finally:
#             session.close()
#     app.dependency_overrides[get_db] = overrid_get_db
#     yield TestClient(app)
    
