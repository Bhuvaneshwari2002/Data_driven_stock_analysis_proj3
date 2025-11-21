📊 Data-Driven Stock Analysis
Organizing, Cleaning & Visualizing Nifty-50 Market Trends
📘 Project Overview

This project analyzes Nifty 50 stock performance using structured Python workflows, SQL storage, and interactive dashboards.
The workflow includes data extraction, cleaning, transformation, stock analysis, and visualization using Python, Pandas, Streamlit, and Power BI.

The goal is to provide meaningful insights such as top performers, laggards, volatility trends, cumulative returns, sector performance, and overall market behavior.

🧩 Key Features
✔ Data Extraction

Raw data provided in YAML format, organized month-wise.

Extracted and converted into 50 CSV files (one for each stock).

✔ Data Cleaning (Completed)

Handled missing values

Standardized date formats

Converted numerical fields

Removed inconsistent or duplicated entries

✔ Yearly Return Calculation (Completed)

Formula used:

Yearly Return = (Last Close - First Close) / First Close * 100

✔ Data Analysis

Includes the following analyses (partially or to be implemented depending on your progress):

Top 10 Green Stocks (best performers)

Top 10 Red Stocks (worst performers)

Market Summary

% of green vs red stocks

Average price

Average volume

Volatility (standard deviation of daily returns)

Monthly top gainers & losers

Correlation matrix (heatmap)

Sector-wise performance

✔ Visualization

Using Matplotlib/Seaborn/Streamlit:

Bar chart → Top 10 most volatile stocks

Line chart → Top 5 cumulative returns

Heatmap → Stock correlation

Bar charts → Monthly gainers & losers

Bar chart → Sector performance

✔ Streamlit Dashboard

Interactive UI with:

Key metrics

Market summary

Upload/show CSVs

Visualizations

Filter-based exploration

✔ Power BI Dashboard

(Optional but recommended for evaluation)

Sector performance

Top gainers/losers

Market summary tiles

Correlation visuals

    🗂 Project Structure
    📁 Data-Driven-Stock-Analysis/
    │
    ├── data/
    │   ├── raw_yaml/             # Original YAML files
    │   ├── cleaned_csv/          # Cleaned CSVs (50 files)
    │    
    ├── scripts/
    │   ├── extract_yaml.py
    │   ├── clean_data.py
    │   ├── analysis.py
    │   ├── visualizations.py
    │
    ├── streamlit_app/
    │   └── app.py                # Streamlit dashboard
    │
    ├── sql/
    │   ├── schema.sql
    │   ├── insert_data.sql
    │
    ├── powerbi/
    │   └── dashboard.pbix        # BI report (optional)
    │
    └── README.md


🛠 Technologies Used

Python

Pandas

NumPy

Matplotlib

Seaborn

Streamlit

MySQL / PostgreSQL

Power BI

SQLAlchemy (optional)

🚀 How to Run the Project
1️⃣ Install Dependencies
pip install -r requirements.txt

2️⃣ Run Analysis Scripts
python scripts/analysis.py

3️⃣ Launch Streamlit App
streamlit run streamlit_app/app.py

4️⃣ Import Data to SQL

Run the schema + insert scripts:

mysql -u root -p < sql/schema.sql
mysql -u root -p < sql/insert_data.sql

📈 Outputs & Insights

Top 10 best/worst performing stocks

Market movement summary

Volatility ranking

Sector-based insights

Monthly gainers/losers

Correlation between stock movements

📌 Project Deliverables

✔ Cleaned dataset (CSV format)

✔ Python scripts (ETL + Analysis + Visuals)

✔ SQL database

✔ Streamlit dashboard

✔ (Optional) Power BI dashboard

✔ README.md

✔ Demo video (for evaluation)

🎥 Demo Video (Mandatory for evaluation)

📌 Upload your project demo on YouTube / LinkedIn and paste the link here.
