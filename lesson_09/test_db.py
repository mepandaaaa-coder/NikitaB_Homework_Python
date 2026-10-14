def test_add_subject(db, fake):
    """Тест на добавление предмета"""
    subject_title = f"Курс: {fake.job()}"

    # 1. Добавляем предмет
    subject_id = db.add(subject_title)

    # 2. Получаем запись через get_by_id и проверяем
    saved_subject = db.get_by_id(subject_id)
    assert (
        saved_subject is not None
        and saved_subject["subject_title"] == subject_title
    )

    # 3. Очистка после теста
    db.delete(subject_id)


def test_update_subject(db, fake):
    """Тест на изменение названия предмета"""
    original_title = f"Старый предмет {fake.word()}"

    # 1. Создаем начальную запись
    subject_id = db.add(original_title)

    # 2. Обновляем название
    new_title = f"Обновленный предмет {fake.word()}"
    db.update(subject_id, new_title)

    # 3. Получаем обновленную запись и проверяем
    updated_subject = db.get_by_id(subject_id)
    assert (
        updated_subject is not None
        and updated_subject["subject_title"] == new_title
    )

    # 4. Очистка после теста
    db.delete(subject_id)


def test_delete_subject(db, fake):
    """Тест на удаление предмета с поэтапной проверкой"""
    subject_title = f"Предмет на удаление {fake.word()}"

    # 1. Создаем запись и убеждаемся, что ID был успешно сгенерирован
    subject_id = db.add(subject_title)
    assert subject_id is not None

    # 2. Проверяем, что запись успешно создана и существует
    existing_subject = db.get_by_id(subject_id)
    assert (
        existing_subject is not None
        and existing_subject["subject_title"] == subject_title
    )

    # 3. Удаляем запись
    db.delete(subject_id)

    # 4. Проверяем отсутствие записи (должен вернуться None)
    deleted_subject = db.get_by_id(subject_id)
    assert deleted_subject is None
