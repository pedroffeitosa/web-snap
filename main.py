from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import os
import time
from config import URL  # Import the URL from config.py

# Setup Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Ensure GUI is off
chrome_options.add_argument("--disable-gpu")

# Set up WebDriver with the correct path to ChromeDriver
webdriver_service = Service('X:/User/ChromeDriver_path.exe')  # Ensure this path points to chromedriver.exe
driver = webdriver.Chrome(service=webdriver_service, options=chrome_options)

# Create a folder to store screenshots
if not os.path.exists("screenshots"):
    os.makedirs("screenshots")

try:
    # Open the website using the URL from config.py
    driver.get(URL)

    # Implicitly wait for elements to be ready
    driver.implicitly_wait(10)

    # Find all sections in the page
    sections = driver.find_elements(By.CSS_SELECTOR, "section")

    # If no sections found, find common div or other elements
    if not sections:
        sections = driver.find_elements(By.CSS_SELECTOR, "div")

    # Iterate through each section
    for index, section in enumerate(sections):
        # Scroll to the section to ensure it's in view
        driver.execute_script("arguments[0].scrollIntoView();", section)

        # Pause briefly to allow any dynamic content to load
        time.sleep(1)

        # Check if the section is visible and has a size
        if section.is_displayed() and section.size['height'] > 0 and section.size['width'] > 0:
            # Try to take a screenshot
            try:
                section.screenshot(f"screenshots/section_{index + 1}.png")
            except Exception as e:
                print(f"Could not take screenshot of section {index + 1}: {e}")
        else:
            print(f"Section {index + 1} is not visible or has zero height/width.")

    print("Screenshots taken and saved in the 'screenshots' folder.")

finally:
    # Close the WebDriver
    driver.quit()
