# 🌉 InsightBridge AI

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-APP-URL-HERE.streamlit.app)
[![Python](https://img.shields.io/badge/Python-3.10%2B-blue)](https://www.python.org/)
[![AI](https://img.shields.io/badge/AI-Google_Gemini-orange)](https://deepmind.google/technologies/gemini/)

**InsightBridge** is an AI-powered Data Analyst agent that bridges the gap between raw data and actionable insights. It allows users to upload multiple CSV files and ask questions in plain English—no SQL knowledge required.

## 🚀 Live Demo
**[Click here to try the App](https://insightbridge-tool.streamlit.app)**

---

## 🌟 Key Features

* **🗣️ Natural Language to SQL:** Just ask *"What is the total sales for Laptop?"* and get an instant answer.
* **📂 Multi-File Support:** Upload multiple CSVs (e.g., `users.csv` and `orders.csv`) and the AI will automatically join them to answer complex queries.
* **📊 Smart Visualizations:** Automatically detects if the answer should be a metric card, a data table, or a chart.
* **🔍 Deep Zoom:** Preview data cleanly on the dashboard or expand to view the full dataset with a single click.
* **⚡ High Performance:** Optimized for speed using the `Gemini Flash` model and local SQLite processing.

---

## 🛠️ Tech Stack

* **Frontend:** [Streamlit](https://streamlit.io/) (UI/UX)
* **AI Model:** Google Gemini 1.5 Flash (via LangChain)
* **Database:** SQLite & SQLAlchemy
* **Data Processing:** Pandas
* **Language:** Python

---

## 💻 How to Run Locally

If you want to run this project on your own machine:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/paresh-patel-10/InsightBridge.git](https://github.com/paresh-patel-10/InsightBridge.git)
    cd InsightBridge
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Set up API Keys:**
    * Create a `.env` file in the root directory.
    * Add your Google API Key:
        ```env
        GOOGLE_API_KEYS="AIzaSyD-Your-Key-Here"
        ```

5.  **Run the App:**
    ```bash
    streamlit run src/app.py
    ```

---

## 📁 Project Structure

```text
InsightBridge/
├── src/
│   ├── app.py          # Main application interface
│   ├── db_utils.py     # Database handling (CSV to SQLite)
│   └── lang_utils.py   # AI Logic (LangChain + Gemini)
├── .env                # API Keys (Not uploaded to GitHub)
├── .gitignore          # Files to ignore
├── README.md           # Project Documentation
└── requirements.txt    # List of dependencies