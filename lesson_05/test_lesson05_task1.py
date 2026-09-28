from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online")

    html_from_link = driver.find_element(By.LINK_TEXT, "HTML Form")
    html_from_link.click()

    assert "/forms/post" in driver.current_url, (
        f"Ожидается URL с /forms/post, получен: {driver.current_url}"
    )
    driver.back()

    assert driver.current_url == "https://httpbin.qa-territory.online/", (
        f"Ожидается исходный URL, получен: {driver.current_url} "
    )
    driver.quit()
