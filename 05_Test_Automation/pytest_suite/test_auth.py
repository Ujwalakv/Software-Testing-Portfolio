import pytest
from conftest import register, login


# Boundary value analysis: minimum password length is 8
@pytest.mark.parametrize("pw,status", [("a" * 7, 400), ("a" * 8, 302), ("a" * 9, 302)])
def test_password_boundary(client, pw, status):
    assert register(client, password=pw).status_code == status


def test_register_duplicate_email(client):
    register(client)
    assert register(client).status_code == 400


@pytest.mark.parametrize("email", ["", "no-at-sign", "a@b"])
def test_register_invalid_email(client, email):
    assert register(client, email=email).status_code == 400


# Decision table: valid/invalid email x valid/invalid password
@pytest.mark.parametrize("email,pw,status", [
    ("student@lms.test", "Student@123", 302),
    ("student@lms.test", "wrong-pass", 401),
    ("nobody@lms.test", "Student@123", 401),
    ("nobody@lms.test", "wrong-pass", 401),
    ("", "", 401),
])
def test_login_decision_table(client, email, pw, status):
    assert login(client, email, pw).status_code == status


def test_protected_page_redirects_when_logged_out(client):
    r = client.get("/dashboard")
    assert r.status_code == 302 and "/login" in r.headers["Location"]


def test_logout_ends_session(client):
    login(client)
    client.get("/logout")
    assert client.get("/courses").status_code == 302
