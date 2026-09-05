import os

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://qa-sample-neha-eman.up.railway.app/"

EMAIL_XPATH = '//*[@id="root"]/div/div/div/form/div[1]/input'
PASSWORD_XPATH = '//*[@id="root"]/div/div/div/form/div[2]/input'
LOGIN_BUTTON_XPATH = '//*[@id="root"]/div/div/div/form/button'
CORE_SERVICES_XPATH = "/html/body/div/div/div/main/section/div[1]/div[2]/select"


def test_core_services_outdated_filter():
    driver = webdriver.Chrome()
    driver.maximize_window()
    wait = WebDriverWait(driver, 15)

    try:
        # Open app
        driver.get(BASE_URL)

        # Login
        wait.until(
            EC.presence_of_element_located((By.XPATH, EMAIL_XPATH))
        ).send_keys(os.getenv("TEST_EMAIL"))

        driver.find_element(
            By.XPATH,
            PASSWORD_XPATH
        ).send_keys(os.getenv("TEST_PASSWORD"))

        driver.find_element(
            By.XPATH,
            LOGIN_BUTTON_XPATH
        ).click()

        # Wait for Devices page
        dropdown = wait.until(
            EC.element_to_be_clickable(
                (By.XPATH, CORE_SERVICES_XPATH)
            )
        )

        # Remember table before filtering
        old_table = driver.find_element(
            By.CSS_SELECTOR,
            "tbody"
        ).text

        # Select Outdated
        Select(dropdown).select_by_visible_text("Outdated")

        # Wait until table actually changes
        wait.until(
            lambda d: d.find_element(
                By.CSS_SELECTOR,
                "tbody"
            ).text != old_table
        )

        # Read filtered rows
        rows = driver.find_elements(
            By.CSS_SELECTOR,
            "tbody tr"
        )

        for row in rows:
            cells = row.find_elements(By.TAG_NAME, "td")
            core_services = cells[2].text.strip()

            assert core_services == "Outdated", (
                f"Expected 'Outdated' but found '{core_services}'"
            )

    finally:
        driver.quit()
