from sqlalchemy import create_engine, text
from faker import Faker

DB_URL = "postgresql+psycopg2://postgres:123@localhost:5432/QA"
fake = Faker("ru_RU")


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
                    self.__scripts["insert"], {"title": title}
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
                self.__scripts["select_by_id"], {"id": subject_id}
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


# --- ТЕСТЫ ---

def test_add_subject():
    """Тест на добавление предмета"""
    db = SubjectTable(DB_URL)
    subject_title = f"Курс: {fake.job()}"

    # 1. Добавляем предмет
    subject_id = db.add(subject_title)
    print("ОТЛАДКА - ПОЛУЧЕННЫЙ ID:", subject_id)

    # 2. Получаем запись через get_by_id и проверяем через словарь
    saved_subject = db.get_by_id(subject_id)
    assert (
        saved_subject is not None
        and saved_subject["subject_title"] == subject_title
    )

    # 3. Очистка после теста
    db.delete(subject_id)


def test_update_subject():
    """Тест на изменение названия предмета"""
    db = SubjectTable(DB_URL)
    original_title = f"Старый предмет {fake.word()}"

    # 1. Создаем начальную запись
    subject_id = db.add(original_title)

    # 2. Обновляем название
    new_title = f"Обновленный предмет {fake.word()}"
    db.update(subject_id, new_title)

    # 3. Получаем обновленную запись и проверяем через словарь
    updated_subject = db.get_by_id(subject_id)
    assert (
        updated_subject is not None
        and updated_subject["subject_title"] == new_title
    )

    # 4. Очистка после теста
    db.delete(subject_id)


def test_delete_subject():
    """Тест на удаление предмета"""
    db = SubjectTable(DB_URL)
    subject_title = f"Предмет на удаление {fake.word()}"

    # 1. Создаем запись для удаления
    subject_id = db.add(subject_title)

    # 2. Удаляем запись
    db.delete(subject_id)

    # 3. Проверка того, что запись успешно удалена (вернулся None)
    deleted_subject = db.get_by_id(subject_id)
    assert deleted_subject is None
