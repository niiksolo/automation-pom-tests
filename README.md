# Automation POM Tests

Автоматизированный фреймворк для тестирования реального маркетплейса [Kasta.ua](https://kasta.ua)  
Python + Selenium с использованием Page Object Model (POM).

## Структура

- `pages/` – Page Object модели страниц  
- `tests/` – Тесты по типам:
  - **smoke** – базовые проверки работоспособности  
  - **integration** – сценарии взаимодействия нескольких функций  
  - **regression** – проверка регрессии после изменений  
- `Dockerfile` – контейнер для запуска тестов  
- `.github/workflows/` – CI/CD workflow для сборки образа, запуска тестов и генерации Allure-отчёта  

## Просмотр Allure-отчёта

После выполнения workflow в GitHub Actions артефакт `allure-report` можно скачать и открыть локально