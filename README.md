# NikitaB_Homework_Python
# Автоматизированное тестирование с использованием Page Object и Allure

Проект содержит UI-автотесты для демонстрации паттерна **Page Object Model (POM)** с использованием **Selenium WebDriver**,
**Pytest** и детализированными отчетами **Allure**.

---

## 🛠 Технологический стек
- **Python** (версия 3.14+)
- **Selenium WebDriver**
- **Pytest**
- **Allure Pytest**

---

## 📦 Установка зависимостей

Перед запуском тестов убедитесь, что у вас установлены все необходимые библиотеки. Вы можете установить их одной командой с помощью файла `requirements.txt`:

```bash
pip install -r requirements.txt

---

## 🚀 Запуск тестов для формирования отчета

python -m pytest lesson_10/tests/ --alluredir=allure-results

---

## 📊 Просмотр сформированного отчета

allure serve allure-results