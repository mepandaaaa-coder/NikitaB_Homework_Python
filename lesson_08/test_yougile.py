import pytest
from lesson_08.yougile_api import YougileApi
from faker import Faker


fake = Faker("ru_RU")


@pytest.fixture
def api_client(api_token):
    """Инициализация клиента API с полученным токеном."""
    return YougileApi(token=api_token)


@pytest.fixture
def created_project_id(api_client):
    """Фикстура для создания тестового проекта перед выполнением проверок."""
    response = api_client.create_project(title="Тестовый проект для фикстуры")
    assert response.status_code == 201
    return response.json()["id"]


# =====================================================================
# 1. ТЕСТЫ МЕТОДА [POST] /api-v2/projects
# =====================================================================

def test_create_project_positive(api_client):
    """Позитивный тест: Успешное создание проекта с валидным названием."""
    response = api_client.create_project(title="Новый проект QA")
    assert response.status_code == 201
    assert "id" in response.json()


def test_create_project_negative_empty_title(api_client):
    """Негативный тест: Попытка создания проекта с пустым названием."""
    response = api_client.create_project(title="")
    assert response.status_code in [400, 422]


# =====================================================================
# 2. ТЕСТЫ МЕТОДА [GET] /api-v2/projects/{id}
# =====================================================================

def test_get_project_by_id_positive(api_client, created_project_id):
    """Позитивный тест: Получение данных существующего проекта по ID."""
    response = api_client.get_project_by_id(created_project_id)
    assert response.status_code == 200
    assert response.json()["id"] == created_project_id


def test_get_project_by_id_negative_not_found(api_client):
    """Негативный тест: Запрос проекта с несуществующим ID."""
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.get_project_by_id(invalid_id)
    assert response.status_code == 404


# =====================================================================
# 3. ТЕСТЫ МЕТОДА [PUT] /api-v2/projects/{id}
# =====================================================================

def test_update_project_positive(api_client, created_project_id):
    """Позитивный тест: Успешное обновление названия существующего проекта."""
    # Генерация случайного названия проекта при каждом запуске
    updated_title = f"Проект {fake.word()} {fake.random_int(100, 999)}"

    response = api_client.update_project(
        created_project_id, title=updated_title
    )
    assert response.status_code == 200

    # Дополнительная проверка сохранения изменений через GET-запрос
    get_res = api_client.get_project_by_id(created_project_id)
    assert get_res.json()["title"] == updated_title


def test_update_project_negative_not_found(api_client):
    """Негативный тест: Попытка обновления проекта с несуществующим ID."""
    invalid_id = "00000000-0000-0000-0000-000000000000"
    response = api_client.update_project(invalid_id, title="Новое название")
    assert response.status_code == 404
