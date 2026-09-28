import time
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submission():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    name_input = driver.find_element(By.NAME, "custname")
    name_input.send_keys("Ivan")

    submit_btn = driver.find_element(
        By.XPATH, "//button[text()='Submit order']"
    )
    submit_btn.click()

    time.sleep(1)

    assert (
        driver.current_url != "https://httpbin.qa-territory.online/forms/post"
    )
    driver.quit()
