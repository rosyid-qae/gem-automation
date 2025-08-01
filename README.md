# GEM Automation with Playwright and Allure

This project demonstrates automated end-to-end testing for the GEM platform using **Playwright** with **Python**, and generates detailed test reports using **Allure Reporter**.

## 🔧 Tech Stack

- **Automation Tool:** Playwright
- **Language:** Python
- **Test Runner:** Pytest
- **Reporting:** Allure Report
- **Assertion Library:** Built-in `expect` from Playwright

## 📁 Project Structure

```bash
tests/                  # Test cases
page/                   # Page Object Models
.env                    # Environment variables
pytest.ini              # Pytest configuration
playwright.config.py    # Playwright configuration (optional)


🚀 Getting Started
Clone the repo

bash
Copy
Edit
git clone https://github.com/rosyid-qae/gem-automation.git
cd gem-automation
Create virtual environment & install requirements

bash
Copy
Edit
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
Run tests with Allure

bash
Copy
Edit
pytest --alluredir=allure-results
allure serve allure-results
📄 License
MIT License