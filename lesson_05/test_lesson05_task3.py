from selenium import webdriver
from selenium.webdriver.common.by import By


def test_multiple_elements():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/links/10")

    links = driver.find_elements(By.TAG_NAME, "a")
    assert len(links) == 9

    for link in links:
        assert link.is_displayed()

    assert any("1" in link.text for link in links)

    driver.quit()
