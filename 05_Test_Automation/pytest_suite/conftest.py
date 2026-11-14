import pytest
from app import create_app


@pytest.fixture()
def client():
    app = create_app({"TESTING": True, "SQLALCHEMY_DATABASE_URI": "sqlite:///:memory:"})
    return app.test_client()


def register(c, name="Asha", email="asha@test.com", password="Passw0rd!", role="student"):
    return c.post("/register", data={"name": name, "email": email, "password": password, "role": role})


def login(c, email="student@lms.test", password="Student@123"):
    return c.post("/login", data={"email": email, "password": password})
