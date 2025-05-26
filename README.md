# 🧪 API Testing Portfolio: ReqRes Demo Suite

This project demonstrates automated API testing using **Python**, **pytest**, and **requests**, targeting the [ReqRes Demo API](https://reqres.in/). It includes both **positive** and **negative** test cases, along with auto-generated reports in **Markdown** and **HTML**.

---

## ✅ What’s Covered

### User Tests
- Get all users (`GET /api/users?page=2`)
- Get a single user by ID
- User not found (`GET /api/users/23`)

### Login Tests
- Successful login (`POST /api/login`)
- Login with missing password (expected failure)

---

## 🧰 Tech Stack

- Python
- pytest
- requests
- pytest-html (for HTML reports)
- pytest-md (for Markdown reports)

---

## 🧾 Project Structure

- `tests/test_users.py` – User listing and detail tests  
- `tests/test_login.py` – Login endpoint tests  
- `requirements.txt` – Dependencies  
- `pytest.ini` – Pytest config  
- `reports/` – Contains auto-generated test reports  

---

## ▶️ How to Run

1. Install dependencies

    ```bash
    pip install -r requirements.txt
    ```

2. Run tests with Markdown + HTML reports

    ```bash
    mkdir -p reports
    pytest --md=reports/api_report.md --html=reports/api_report.html
    ```

---

## 📊 Sample Output

- ✅ Successful login returns a `token`
- ❌ Missing password returns a `400` with `"Missing password"` error
- ❌ Requesting non-existent user returns `404`

---

## 📍 About ReqRes

- Free, public API for testing frontend/backend logic
- No API key required
- Documentation: https://reqres.in/

---

## 📌 Author

**Numair Kaukab**  
QA Automation Engineer  
