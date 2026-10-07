import pytest
import requests

# Учетные данные пользователя Yougile
USER_LOGIN = "tg3yqfitzm@yzcalo.com"
USER_PASSWORD = "ihW-m2v-n4x-rYh"
BASE_URL = "https://yougile.com"


@pytest.fixture(scope="session")
def api_token():
    """
    Сессионная фикстура: автоматически получает актуальный API-токен Yougile
    по логину и паролю перед запуском тестов.
    """
    # 1. Получение ID компании по логину и паролю
    companies_res = requests.post(
        f"{BASE_URL}/api-v2/auth/companies",
        json={"login": USER_LOGIN, "password": USER_PASSWORD}
    )
    assert companies_res.status_code == 200

    companies_data = companies_res.json()
    company_id = companies_data["content"][0]["id"]

    # 2. Генерация ключа API (Bearer token)
    key_res = requests.post(
        f"{BASE_URL}/api-v2/auth/keys",
        json={
            "login": USER_LOGIN,
            "password": USER_PASSWORD,
            "companyId": company_id
        }
    )
    assert key_res.status_code == 201

    return key_res.json()["key"]
