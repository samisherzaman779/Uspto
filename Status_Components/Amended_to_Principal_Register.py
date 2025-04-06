from selenium.webdriver.common.by import By

def scrape_amended_to_principal_register(driver):
    try:
        # Find the element containing "Amended to Principal Register:"
        elements = driver.find_elements(By.CLASS_NAME, "row")

        for element in elements:
            key_elements = element.find_elements(By.CLASS_NAME, "key")
            value_elements = element.find_elements(By.CLASS_NAME, "value")

            for key, value in zip(key_elements, value_elements):
                if "Amended to Principal Register:" in key.text:
                    return value.text.strip()  # Extract the "No" value
        
        return "Not Found"  # Return "Not Found" if the element is missing

    except Exception as e:
        print(f"❌ Error scraping Amended to Principal Register: {e}")
        return "Error"
