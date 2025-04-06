from selenium.webdriver.common.by import By

def scrape_mark_text(driver):
    """
    Scrapes text from <div class='value markText'> on the page.
    
    :param driver: Selenium WebDriver instance
    :return: Scraped text (or 'Not Found' if element is missing)
    """
    try:
        element = driver.find_element(By.CLASS_NAME, "markText")
        scraped_text = element.text.strip()  # Extract and clean the text
        print(f"✅ Scraped Mark Text: {scraped_text}")  # Print the scraped text
        return scraped_text
    except:
        print("❌ Mark Text Not Found")  # Print an error message
        return "Not Found"  # Return 'Not Found' if element is missing
