import requests


class YougileApi:
    """Класс для взаимодействия с API Yougile (API Client)."""

    def __init__(self, token: str, base_url: str = "https://yougile.com"):
        self.base_url = base_url
        self.headers = {
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json"
        }

    def create_project(
            self,
            title: str = None,
            users: dict = None
            ) -> requests.Response:
        """[POST] /api-v2/projects —
        Создание нового проекта."""
        url = f"{self.base_url}/api-v2/projects"
        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users
        return requests.post(url, json=payload, headers=self.headers)

    def get_project_by_id(self, project_id: str) -> requests.Response:
        """[GET] /api-v2/projects/{id} —
        Получение информации о проекте по ID."""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        return requests.get(url, headers=self.headers)

    def update_project(
            self,
            project_id: str,
            title: str = None,
            users: dict = None,
            deleted: bool = None
            ) -> requests.Response:
        """[PUT] /api-v2/projects/{id} —
        Обновление данных существующего проекта."""
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {}
        if title is not None:
            payload["title"] = title
        if users is not None:
            payload["users"] = users
        if deleted is not None:
            payload["deleted"] = deleted
        return requests.put(url, json=payload, headers=self.headers)
