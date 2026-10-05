import pytest
from selenium import webdriver
from lesson_07.pages.login_page import LoginPage
from lesson_07.pages.inventory_page import InventoryPage
from lesson_07.pages.cart_page import CartPage
from lesson_07.pages.checkout_page import CheckoutPage


@pytest.fixture
def driver():
    # Используем браузер Firefox согласно условию задачи
    browser = webdriver.Firefox()
    browser.implicitly_wait(4)
    yield browser
    browser.quit()


def test_saucedemo_checkout(driver):
    login_page = LoginPage(driver)
    inventory_page = InventoryPage(driver)
    cart_page = CartPage(driver)
    checkout_page = CheckoutPage(driver)

    # 1. Открыть сайт магазина
    login_page.open()

    # 2. Авторизоваться как standard_user
    login_page.login("standard_user", "secret_sauce")

    # 3. Добавить в корзину указанные товары
    items_to_add = [
        "Sauce Labs Backpack",
        "Sauce Labs Bolt T-Shirt",
        "Sauce Labs Onesie"
    ]
    for item in items_to_add:
        inventory_page.add_to_cart(item)

    # 4. Перейти в корзину
    inventory_page.go_to_cart()

    # Проверка состава корзины через Page Object метод
    cart_items = cart_page.get_cart_item_names()
    assert len(cart_items) == 3

    # 5. Нажать кнопку Checkout
    cart_page.click_checkout()

    # 6. Заполнить форму персональными данными
    checkout_page.fill_form("Иван", "Иванов", "101000")

    # 7. Прочитать со страницы итоговую стоимость (Total)
    total_price = checkout_page.get_total_price()

    # 8. Проверить (assert), что итоговая сумма равна $58.29
    assert total_price == "Total: $58.29"
