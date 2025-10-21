# 🔗 Automation POM Tests

Automated testing framework for the real marketplace [Kasta.ua](https://kasta.ua)  
Built with Python + Selenium using the Page Object Model (POM).

---

## 📂 Project Structure

- `pages/` – Page Object models for the website pages  
- `tests/` – Tests organized by type:
  - **smoke** – basic functionality checks  
  - **integration** – scenarios involving multiple features  
  - **regression** – regression tests after changes  
- `Dockerfile` – container for running tests  
- `.github/workflows/` – CI/CD workflow for building the Docker image, running tests, and generating Allure reports  

---

## 📊 Viewing Allure Reports

After the GitHub Actions workflow runs, the `allure-report` artifact can be downloaded and viewed locally.