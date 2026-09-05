import os
import pytest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


BASE_URL = "https://qa-sample-neha-eman.up.railway.app/"


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(BASE_URL)

    yield driver

    driver.quit()


def test_core_services_outdated_filter(driver):
    """
    Ticket #1 - Devices Filters

    Verify that Core Services = Outdated returns only
    devices whose Core Services status is Outdated.

    Regression coverage for Bug #12.
    """

    wait = WebDriverWait(driver, 10)

    # Locate the Core Services dropdown
    core_services_dropdown = wait.until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                "/html/body/div/div/div/main/section/div[1]/div[2]/select"
            )
        )
    )

    # Select "Outdated"
    Select(core_services_dropdown).select_by_visible_text("Outdated")

    # Wait until device rows are available
    rows = wait.until(
        EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "tbody tr")
        )
    )

    assert len(rows) > 0, "No devices were returned for Outdated filter"

    # Check the Core Services value of every returned row
    for row in rows:
        cells = row.find_elements(By.TAG_NAME, "td")

        core_services_value = cells[2].text.strip()

        assert core_services_value == "Outdated", (
            f"Expected Core Services = 'Outdated', "
            f"but found '{core_services_value}'"
        )
