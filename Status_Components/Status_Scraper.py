from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def scrape_status_text(driver):
    """
    Scrapes the text dynamically based on 'Status:' key, even if it's not at a fixed position.

    :param driver: Selenium WebDriver instance
    :return: Scraped status text (or 'N/A' if missing)
    """
    try:
        # ✅ Find all 'key' divs
        key_divs = driver.find_elements(By.CSS_SELECTOR, "div.key")

        for key_div in key_divs:
            if key_div.text.strip().lower() == "status:":  # ✅ Match 'Status:' dynamically
                # ✅ Get the corresponding 'value' div (next sibling)
                value_div = key_div.find_element(By.XPATH, "./following-sibling::div[contains(@class, 'value')]")
                
                # ✅ Extract and return text
                status_text = value_div.text.strip()
                print(f"✅ Scraped Status Text: {status_text}")
                return status_text if status_text else "N/A"

        print("⚠️ 'Status:' key not found.")
        return "N/A"

    except Exception as e:
        print(f"❌ Error in scrape_status_text: {e}")
        return "N/A"
