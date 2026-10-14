import pytest
from sqlalchemy import create_engine, text
from faker import Faker

DB_URL = "postgresql+psycopg2://postgres:123@localhost:5432/QA"


class SubjectTable:
    __scripts = {
        "insert": text(
            "INSERT INTO subject (subject_title) "
            "VALUES (:title) "
            "RETURNING subject_id"
        ),
        "update": text(
            "UPDATE subject SET subject_title = :new_title "
            "WHERE subject_id = :id"
        ),
        "select_by_id": text(
            "SELECT * FROM subject WHERE subject_id = :id"
        ),
        "delete_by_id": text(
            "DELETE FROM subject WHERE subject_id = :id_to_delete"
        )
    }

    def __init__(self, connection_string):
        self.__db = create_engine(connection_string)

    def add(self, title):
        with self.__db.connect() as conn:
            with conn.begin():
                result = conn.execute(
                    self.__scripts["insert"],
                    {"title": title}
                )
                subject_id = result.scalar()
        return subject_id

    def update(self, subject_id, new_title):
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(
                    self.__scripts["update"],
                    {"new_title": new_title, "id": subject_id}
                )

    def get_by_id(self, subject_id):
        with self.__db.connect() as conn:
            result = conn.execute(
                self.__scripts["select_by_id"],
                {"id": subject_id}
            )
            row = result.mappings().first()
        return row

    def delete(self, subject_id):
        with self.__db.connect() as conn:
            with conn.begin():
                conn.execute(
                    self.__scripts["delete_by_id"],
                    {"id_to_delete": subject_id}
                )


@pytest.fixture
def db():
    """Фикстура, предоставляющая экземпляр SubjectTable для тестов"""
    return SubjectTable(DB_URL)


@pytest.fixture
def fake():
    """Фикстура для генерации фейковых данных на русском языке"""
    return Faker("ru_RU")
