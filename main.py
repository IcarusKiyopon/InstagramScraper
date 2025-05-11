import time
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import config  

# === Configuration ===
USERNAME = config.INSTAGRAM_USERNAME
PASSWORD = config.INSTAGRAM_PASSWORD
TARGET_ACCOUNT = config.TARGET_ACCOUNT
CHROMEDRIVER_PATH = config.CHROMEDRIVER_PATH
MAX_FOLLOWERS = config.MAX_FOLLOWERS  # Maximum number of followers to collect

# === Setup ===
options = Options()
# options.add_argument("--headless")  # Uncomment to run in headless mode
options.add_argument("--disable-notifications")
options.add_argument("--disable-popup-blocking")
options.add_argument("--start-maximized")
options.add_argument("--enable-unsafe-swiftshader")  # Helps with WebGL errors

# Add a user agent to appear more like a normal browser
options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36")

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)
wait = WebDriverWait(driver, 15)

# Function to take screenshots for debugging
def take_screenshot(filename):
    try:
        driver.save_screenshot(f"{filename}.png")
        print(f"Saved screenshot: {filename}.png")
    except Exception as e:
        print(f"Failed to save screenshot: {e}")

print("Starting Instagram follower scraper...")

try:
    # === Log into Instagram ===
    print("Navigating to Instagram login page...")
    driver.get("https://www.instagram.com/accounts/login/")
    time.sleep(5)
    
    # Take screenshot of login page
    take_screenshot("1_login_page")
    
    print("Entering credentials...")
    username_field = wait.until(EC.presence_of_element_located((By.NAME, "username")))
    password_field = wait.until(EC.presence_of_element_located((By.NAME, "password")))
    
    # Clear fields first (in case they're pre-filled)
    username_field.clear()
    password_field.clear()
    
    # Enter credentials with random delays to appear more human-like
    for char in USERNAME:
        username_field.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))
    
    time.sleep(random.uniform(0.5, 1.5))
    
    for char in PASSWORD:
        password_field.send_keys(char)
        time.sleep(random.uniform(0.05, 0.2))
    
    time.sleep(random.uniform(0.5, 1.5))
    
    # Click login button instead of pressing Enter
    try:
        login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
        login_button.click()
    except NoSuchElementException:
        # Fall back to pressing Enter if button not found
        password_field.send_keys(Keys.RETURN)
    
    print("Logging in...")
    time.sleep(8)  # Wait longer for login to complete
    
    # Take screenshot after login attempt
    take_screenshot("2_after_login")
    
    # === Dismiss popups if they appear ===
    print("Checking for popups...")
    popups = [
        "//button[contains(text(), 'Save Info')]",
        "//button[contains(text(), 'Not Now')]",
        "//button[contains(text(), 'Not now')]",
        "//button[contains(text(), 'Skip')]",
        "//button[contains(text(), 'Cancel')]"
    ]
    
    for popup in popups:
        try:
            popup_button = wait.until(EC.element_to_be_clickable((By.XPATH, popup)))
            popup_button.click()
            print(f"Dismissed popup: {popup}")
            time.sleep(2)
        except (TimeoutException, NoSuchElementException):
            pass
    
    # === Navigate to target profile ===
    print(f"Navigating to {TARGET_ACCOUNT}'s profile...")
    driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
    time.sleep(5)
    
    # Take screenshot of profile page
    take_screenshot("3_profile_page")
    
    # === Open followers popup ===
    print("Attempting to open followers list...")
    
    # (Continue with the rest of your scraping logic...)
    # ...
    
except Exception as e:
    print(f"An error occurred: {e}")
    take_screenshot("error_screenshot")

finally:
    print("Closing browser...")
    driver.quit()
