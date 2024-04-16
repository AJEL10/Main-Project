# import unittest
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.options import Options

# # Path to your Chrome WebDriver executable
# chrome_driver_path = r'C:\Users\ajelv\Downloads\chromedriver-win64\chromedriver.exe'

# # URL of the HTML page to be tested
# url = r'C:\Users\ajelv\OneDrive\Documents\SmileSphereApp[1]\template\clinic_login.html'

# # Initialize ChromeOptions
# chrome_options = Options()

# # Initialize Chrome WebDriver with ChromeOptions
# driver = webdriver.Chrome(options=chrome_options)

# # Open the HTML page
# driver.get(url)

# try:
#     # Find input fields and buttons
#     clinic_name_input = driver.find_element(By.ID, 'clinic_name')
#     password_input = driver.find_element(By.ID, 'password')
#     submit_button = driver.find_element(By.XPATH, '//button[contains(text(), "Submit")]')
#     cancel_button = driver.find_element(By.XPATH, '//button[contains(text(), "Cancel")]')

#     # Enter clinic name and password
#     clinic_name_input.send_keys("your_clinic_name")
#     password_input.send_keys("your_password")

#     # Click the Submit button
#     submit_button.click()

#     # Wait for redirection to clinic dashboard (assuming successful login)
#     # You can add assertions or further actions here to verify login success

#     # Print success message
#     print("Login successful!")

# except Exception as e:
#     # Print error message if login fails
#     print("Error:", e)

# finally:
#     # Close the browser window
#     driver.quit()





# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

# # Initialize the Chrome driver
# chrome_driver_path = r'C:\Users\ajelv\Downloads\chromedriver-win64\chromedriver.exe'
# driver = webdriver.Chrome()


# # Open the web page
# url = r'file:///C:/Users/ajelv/OneDrive/Documents/SmileSphereApp[1]/template/patient_login.html'
# driver.get(url)

# # Find the email and password input fields
# email_input = driver.find_element(By.NAME, "email")
# password_input = driver.find_element(By.NAME, "password")

# # Enter test credentials
# email_input.send_keys("test@example.com")
# password_input.send_keys("testpassword")

# # Find and click the login button
# login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
# login_button.click()

# # Wait for the page to load after login (replace "Expected Title After Login" with the actual title)
# try:
#     WebDriverWait(driver, 10).until(EC.title_contains("Patient Login"))
#     print("Login successful!")
# except:
#     print("Login failed!")

# # Close the browser
# driver.quit()



import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestAppointmentForm(unittest.TestCase):
    def setUp(self):
        # Initialize the Chrome driver
        self.driver = webdriver.Chrome()
        # Open the web page
        self.driver.get("file:///C:/Users/ajelv/OneDrive/Documents/SmileSphereApp[1]/template/new_appointment.html")
    


    def test_fill_form(self):
        # Find form elements
        name_input = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.ID, "name")))
        date_input = self.driver.find_element(By.ID, "date")
        clinic_select = self.driver.find_element(By.ID, "clinic")
        description_textarea = self.driver.find_element(By.NAME, "description")
        submit_button = self.driver.find_element(By.XPATH, "//button[@type='submit']")

        # Fill out the form
        name_input.send_keys("John Doe")
        date_input.send_keys("2024-04-16")  # Change to a valid date
        clinic_select.send_keys("Clinic 1")  # Choose a clinic option
        description_textarea.send_keys("Description of the problem")

        # Submit the form
        submit_button.click()

        # Wait for the confirmation page or element
        WebDriverWait(self.driver, 10).until(EC.title_contains("Confirmation"))

        # Assertion to check if the confirmation page is loaded successfully
        self.assertIn("Appointment Created", self.driver.title)

    def tearDown(self):
        # Close the browser
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()



