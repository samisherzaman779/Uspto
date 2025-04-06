from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Directly import the WebDriver
driver = webdriver.Chrome()

# Open the target website
driver.get("https://tmsearch.uspto.gov/search/search-results")

# Wait for the page to load
time.sleep(5)  # Adjust sleep time if necessary

# Create or open a file to save URLs
output_file = "scraped_urls.txt"
with open(output_file, "a") as file:
    while True:
        # Wait for user input to start scraping
        input("Press Enter to start scraping this page...")
        
        # Find all serial numbers on the page
        serial_numbers = driver.find_elements(By.XPATH, "//div[contains(@class, 'col ps-0 ps-sm-1')]/span")
        
        # Iterate through serial numbers and construct URLs
        for serial in serial_numbers:
            serial_text = serial.text.strip()
            if serial_text.isdigit():  # Ensure it's a valid serial number
                url = f"https://tsdr.uspto.gov/#caseNumber={serial_text}&caseSearchType=US_APPLICATION&caseType=DEFAULT&searchType=statusSearch"
                print(url)
                file.write(url + "\n")  # Save the URL to the file
        
        file.flush()  # Ensure data is written to the file
        
        # Wait for user input before scraping the next page
        input("Press Enter to continue to the next page or close manually...")

# Keep the browser open until manually closed
input("Press Enter to close the browser...")
driver.quit()
