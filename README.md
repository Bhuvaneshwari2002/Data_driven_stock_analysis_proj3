# 📊 Data-Driven Stock Market Analysis

### **Power BI • Python • MySQL • Streamlit**

This project provides a complete **end-to-end stock analytics system** that processes raw price data, stores it in a relational database, computes financial metrics, and visualises insights using **Power BI** and a **Streamlit web application**.

The goal is to help users understand **market trends, volatility, sector performance, cumulative returns, monthly movers**, and **correlation between stock behaviors**.

---

## 🚀 Features

### ✅ **1. SQL Database (MySQL)**

A relational schema stores stock metadata and historical price data.

* `stocks` table → basic company info
* `prices` table → daily OHLC data + computed `daily_return`
* Includes indexes for faster analytics queries
* Supports time-series analysis & advanced resampling
* Auto-computes:

  * Daily return
  * Monthly return
  * Cumulative return

### ✅ **2. Power BI Dashboard**

A professionally designed BI dashboard with **two pages**:

#### **Page 1 — Overview (Market Summary)**

* Top 10 **Green** (best yearly return) & **Red** (worst yearly return) stocks
* Top 10 **Most Volatile** stocks
* KPI Cards

  * Green Stocks Count
  * Red Stocks Count
  * Average Last Close
  * Average Volume
* Sector Performance (Avg Cumulative Return)
* Cumulative Return Trend (Line Chart)

#### **Page 2 — Details (Deep Dive)**

* Monthly Filter Slicer
* Monthly Top 5 **Gainers**
* Monthly Top 5 **Losers**
* Correlation Heatmap of Daily Returns
* Supports drill-down filtering across visuals

---

## 🧪 **3. Streamlit Web App**

The Python dashboard includes the following modules:

### 📈 Overview

* Green vs Red stocks
* Top & bottom performers
* Market insights at a glance

### 📉 Volatility

* Standard deviation of daily returns
* Bar chart of volatility by stock

### 📊 Cumulative Returns

* Computes log cumulative returns
* Identifies top-performing stocks

### 🏭 Sector Performance

* Compares average cumulative return by sector

### 🔥 Monthly Movers

* Monthly Top-5 gainers
* Monthly Top-5 losers
* Perfect for tracking trading momentum

### 🔗 Correlation Heatmap

* Plotly-based interactive correlation matrix
* Shows relationships between stock movements
* Useful for portfolio diversification analysis

---

## 🗂 Project Structure

```
📦 Data-Driven-Stock-Analysis
│
├── 📁 SQL
│   └── data_driven_stock_analysis.sql         # Database schema + table creation
│
├── 📁 StreamlitApp
│   ├── app_streamlit_simple.py               # Main Streamlit dashboard
│   └── requirements.txt                      # Python libraries
│
├── 📁 PowerBI
│   └── data_driven_proj.pbix                 # Power BI report (2 pages)
│
├── 📁 Notebooks
│   └── Data_driven_stock_analysis.ipynb      # EDA, preprocessing, calculations
│
├── README.md                                 # Project documentation
```

---

## 🛠️ **Technology Stack**

### **Backend / Processing**

* Python
* Pandas
* NumPy
* Plotly
* Streamlit
* Matplotlib

### **Database**

* MySQL
* Window functions (LAG) for return calculations

### **Visualization**

* Power BI
* Streamlit (Plotly charts)

---

## 🔧 Setup Instructions

### **1️⃣ Clone the repository**

```bash
git clone https://github.com/your-username/data-driven-stock-analysis.git
cd data-driven-stock-analysis
```

---

### **2️⃣ Setup Virtual Environment**

```bash
python -m venv .venv
source .venv/bin/activate       # Mac/Linux
.venv\Scripts\activate          # Windows
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

### **3️⃣ Setup MySQL Database**

Import the SQL file:

```sql
SOURCE data_driven_stock_analysis.sql;
```

Populate tables with your data (CSV or API-fed).

---

### **4️⃣ Run Streamlit App**

```bash
streamlit run app_streamlit_simple.py
```

App will open at:

```
http://localhost:8501/
```

---

### **5️⃣ Open Power BI Dashboard**

* Launch `data_driven_proj.pbix`
* Refresh data source
* Ensure connection to MySQL is configured

---

## 📊 Outputs & Insights

### You will be able to:

* Identify outperforming sectors
* Detect high-volatility stocks
* Track trends over months
* Observe correlations between companies
* Compare cumulative performance across time

---

## 📌 Example Screenshots


## 📸 Overview: <img width="1286" height="723" alt="image" src="https://github.com/user-attachments/assets/249f65d3-11c1-43c7-987f-657bab2d06bd" />

## 📸 Details: <img width="1285" height="721" alt="Screenshot 2025-12-06 230057" src="https://github.com/user-attachments/assets/ce3cb7c6-126a-4c01-9e0f-2590a52b459d" />
