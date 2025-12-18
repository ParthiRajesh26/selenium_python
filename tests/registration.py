# registration.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class TestUserRegistration(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('http://example.com/registration')  # Replace with actual registration page URL
        self.wait = WebDriverWait(self.driver, 10)

    def tearDown(self):
        self.driver.quit()

    def fill_registration_form(self, name='', email='', password=''):
        name_input = self.wait.until(EC.presence_of_element_located((By.NAME, 'name')))
        email_input = self.driver.find_element(By.NAME, 'email')
        password_input = self.driver.find_element(By.NAME, 'password')
        name_input.clear()
        name_input.send_keys(name)
        email_input.clear()
        email_input.send_keys(email)
        password_input.clear()
        password_input.send_keys(password)

    def submit_form(self):
        submit_btn = self.driver.find_element(By.XPATH, "//button[@type='submit']")
        submit_btn.click()

    def test_successful_registration(self):
        """
        Scenario: Successful registration with valid details
        """
        self.fill_registration_form(name='Test User', email='testuser@example.com', password='StrongPass123!')
        self.submit_form()
        # Assert account creation (e.g., presence of welcome message or redirect)
        self.wait.until(EC.url_contains('/welcome'))
        self.assertIn('welcome', self.driver.current_url)
        welcome_text = self.driver.find_element(By.TAG_NAME, 'body').text
        self.assertIn('Welcome', welcome_text)

    def test_registration_invalid_email(self):
        """
        Scenario: Registration with invalid email format
        """
        self.fill_registration_form(name='Test User', email='invalid-email', password='StrongPass123!')
        self.submit_form()
        # Assert error message for invalid email
        error = self.wait.until(EC.visibility_of_element_located((By.ID, 'email-error')))
        self.assertIn('invalid email', error.text.lower())
        # Assert account not created (still on registration page)
        self.assertIn('/registration', self.driver.current_url)

    def test_registration_weak_password(self):
        """
        Scenario: Registration with weak password
        """
        self.fill_registration_form(name='Test User', email='testuser@example.com', password='123')
        self.submit_form()
        # Assert error message for weak password
        error = self.wait.until(EC.visibility_of_element_located((By.ID, 'password-error')))
        self.assertIn('password', error.text.lower())
        self.assertIn('strength', error.text.lower())
        # Assert account not created (still on registration page)
        self.assertIn('/registration', self.driver.current_url)

if __name__ == '__main__':
    unittest.main()
