"""Selenium UI tests. Needs: pip install selenium, Chrome, and the app running on port 5000."""
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

BASE = "http://127.0.0.1:5000"


def _login(d, email, password):
    d.get(f"{BASE}/login")
    d.find_element(By.ID, "email").send_keys(email)
    d.find_element(By.ID, "password").send_keys(password)
    d.find_element(By.CSS_SELECTOR, "button[type=submit]").click()


def test_login_shows_dashboard():
    d = webdriver.Chrome()
    try:
        _login(d, "student@lms.test", "Student@123")
        WebDriverWait(d, 30).until(EC.url_contains("/dashboard"))
        assert "Welcome back" in d.page_source
    finally:
        d.quit()


def test_wrong_password_shows_error():
    d = webdriver.Chrome()
    try:
        _login(d, "student@lms.test", "wrongpass1")
        msg = WebDriverWait(d, 30).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".flash.error")))
        assert "Invalid email or password." in msg.text
    finally:
        d.quit()