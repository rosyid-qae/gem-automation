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
1. Clone the repo
bash
git clone https://github.com/rosyid-qae/gem-automation.git
cd gem-automation

2. Create virtual environment & install requirements
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

3. Run tests with Allure
pytest --alluredir=allure-results
allure serve allure-results


📄 License
MIT License
