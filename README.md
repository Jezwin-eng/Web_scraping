
# 🛒 Amazon Laptop Price Tracker (Only Windows)

A Python-based project that automatically scrapes the top 20 laptops from [Amazon.in](https://www.amazon.in), saves them to a CSV, sends email alerts on price drops, and displays the data in a Streamlit dashboard.

---

## 🚀 Features

- ✅ Scrapes **name**, **price**, **link**, and **date**
- ✅ Saves daily results in a structured CSV
- ✅ Sends **email alerts** when prices drop below a target
- ✅ Visualizes top laptops in a **Streamlit dashboard**
- ✅ Automated via `.bat` file and Windows Task Scheduler

---

## 🧰 Requirements

Install the required packages:

```bash
pip install selenium pandas matplotlib streamlit
```

Also install:
- Microsoft Edge browser
- [Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/) matching your Edge version

---

## ⚙️ Setup Instructions

### 🔹 1. Clone or Download

```bash
git clone https://github.com/yourusername/amazon-price-tracker.git
cd amazon-price-tracker
```

### 🔹 2. Configure Alerts

Edit `config.py`:

```python
ALERT_THRESHOLD = 45000

EMAIL_SETTINGS = {
    "sender": "your_email@gmail.com",
    "receiver": "your_email@gmail.com",
    "app_password": "your_gmail_app_password"
}
```

Use a [Gmail App Password](https://support.google.com/accounts/answer/185833) (not your actual password).

---

### 🔹 3. Run the Scraper

```bash
python main_scraper.py
```

This will:
- Scrape top 20 laptops
- Save to `laptop_prices.csv`
- Send email alerts for price drops

---

### 🔹 4. View the Dashboard

```bash
streamlit run app.py
```

Features:
- Filter by brand or price range
- View the top 10 laptops by price
- Click links to view on Amazon

---

### 🔹 5. Automate Daily Scraping (Windows)

Create a file `run_daily.bat`:

```bat
@echo off
cd C:\Path\To\Project
C:\Path\To\Python\python.exe main_scraper.py
```

Then use **Task Scheduler**:
- Trigger: Daily
- Action: Start `run_daily.bat`

---

## 📦 Output Example

| Date       | Name                | Price    | Link                         |
|------------|---------------------|----------|------------------------------|
| 2025-06-11 | ASUS Vivobook 15... | ₹43,999  | https://www.amazon.in/...    |

---

## 📌 Notes

- Amazon’s HTML structure may change; this script may need updates
- Use only for **personal/educational purposes**
- Data is saved in `laptop_prices.csv` for trend analysis

---

## 📜 License

MIT License — Free for educational and personal use.
