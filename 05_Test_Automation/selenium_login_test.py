"""UI test. Needs: pip install selenium, Chrome, and the app running on :5000."""
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_login_shows_dashboard():
    d = webdriver.Chrome()
    try:
        d.get("http://127.0.0.1:5000/login")
        d.find_element(By.ID, "email").send_keys("student@lms.test")
        d.find_element(By.ID, "password").send_keys("Student@123")
        d.find_element(By.CSS_SELECTOR, "button[type=submit]").click()
        assert "Welcome back" in d.page_source
    finally:
        d.quit()
