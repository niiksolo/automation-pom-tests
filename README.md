# Automation POM Tests

Автоматизированный фреймворк для тестирования веб-приложения на Python + Selenium с использованием Page Object Model (POM).

## Структура

- `pages/` – Page Object модели страниц  
- `tests/` – Тесты по типам: smoke, integration, regression  
- `Dockerfile` – Контейнер для запуска тестов  
- `.github/workflows/` – CI/CD workflow для сборки образа, запуска тестов и генерации Allure-отчёта  

[Открыть Allure-отчёт](https://github.com/niiksolo/automation-pom-tests/suites/latest/artifacts/allure-report/allure-html/index.html)
