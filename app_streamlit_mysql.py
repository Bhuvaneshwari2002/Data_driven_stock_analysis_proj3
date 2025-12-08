# Import necessary libraries
import streamlit as st
import pandas as pd
import pymysql
import plotly.express as px # pyright: ignore

# Configuration for MySQL connection
MYSQL_HOST = "localhost"
MYSQL_USER = "root"
MYSQL_PASS = "123456789"  
MYSQL_DB   = "stock_analysis"

st.set_page_config(layout="wide", page_title="Stock Analysis (Simple MySQL)")

@st.cache_data
def load_data():
    conn = pymysql.connect(host=MYSQL_HOST, user=MYSQL_USER, password=MYSQL_PASS, database=MYSQL_DB)
    # load all prices and stocks tables
    prices = pd.read_sql("SELECT ticker, date, open, high, low, close, volume, daily_return FROM prices", conn, parse_dates=["date"])
    stocks = pd.read_sql("SELECT ticker, company, sector FROM stocks", conn)
    conn.close()
    prices["ticker"] = prices["ticker"].str.upper()
    stocks["ticker"] = stocks["ticker"].str.upper()
    prices = prices.sort_values(["ticker", "date"])
    return prices, stocks

prices, stocks = load_data()

st.title("Stock Analysis — Simple Streamlit (MySQL)")

page = st.sidebar.radio("Page", ["Overview", "Volatility", "Cumulative", "Sector", "Correlation", "Monthly Movers"])

# Overview Page
if page == "Overview":
    st.header("Overview: Top/Bottom & Market Summary")
    first = prices.groupby("ticker").first().reset_index()[["ticker","close"]].rename(columns={"close":"start_close"})
    last  = prices.groupby("ticker").last().reset_index()[["ticker","close"]].rename(columns={"close":"end_close"})
    summary = first.merge(last, on="ticker")
    summary["yearly_return"] = (summary["end_close"] - summary["start_close"]) / summary["start_close"]
    # Top & bottom 10 
    top10 = summary.sort_values("yearly_return", ascending=False).head(10)[["ticker","yearly_return"]]
    bot10 = summary.sort_values("yearly_return", ascending=True).head(10)[["ticker","yearly_return"]]
    # Market summary 
    green_count = (summary["yearly_return"] > 0).sum()
    red_count = (summary["yearly_return"] <= 0).sum()
    avg_last_close = summary["end_close"].mean()
    col1, col2, col3 = st.columns(3)
    col1.metric("Green stocks", green_count)
    col2.metric("Red stocks", red_count)
    col3.metric("Avg last close", f"{avg_last_close:.2f}")

    st.subheader("Top 10 Yearly Gainers")
    st.dataframe(top10.rename(columns={"ticker":"Ticker","yearly_return":"YearlyReturn"}).reset_index(drop=True))

    st.subheader("Top 10 Yearly Losers")
    st.dataframe(bot10.rename(columns={"ticker":"Ticker","yearly_return":"YearlyReturn"}).reset_index(drop=True))

# Volatility Page
elif page == "Volatility":
    st.header("Volatility (Std dev of daily returns)")
    vol = prices.groupby("ticker")["daily_return"].std().dropna().sort_values(ascending=False)
    st.bar_chart(vol.head(20))


# Cumulative Page
elif page == "Cumulative":
    st.header("Cumulative Returns (Top N)")
    N = st.slider("Top N tickers to plot", 1, 10, 5)
    final = []
    for t, g in prices.groupby("ticker"):
        g = g.sort_values("date")
        cum = (1 + g["daily_return"]).cumprod() - 1
        final.append((t, cum.iloc[-1]))
    final_df = pd.DataFrame(final, columns=["ticker","final_cum"]).sort_values("final_cum", ascending=False)
    top_tickers = final_df["ticker"].head(N).tolist()

    # build pivot for plotting
    plot_df = pd.DataFrame()
    for t in top_tickers:
        g = prices[prices["ticker"]==t].sort_values("date")
        plot_df[t] = (1 + g["daily_return"]).cumprod() - 1
        plot_df.index = g["date"]
    st.line_chart(plot_df.fillna(method="ffill"))

# Sector page
elif page == "Sector":
    st.header("Sector Performance (average final cumulative return)")
    final = []
    for t, g in prices.groupby("ticker"):
        g = g.sort_values("date")
        final.append((t, (1 + g["daily_return"]).cumprod().iloc[-1]))
    final_df = pd.DataFrame(final, columns=["ticker","final_cum"])
    merged = final_df.merge(stocks[["ticker","sector"]], on="ticker", how="left")
    sector_perf = merged.groupby("sector")["final_cum"].mean().sort_values(ascending=False)
    st.bar_chart(sector_perf)

# Correlation heatmap page
elif page == "Correlation":
    st.header("Correlation Heatmap (Daily Returns)")
    pivot = prices.pivot(index="date", columns="ticker", values="daily_return")
    corr = pivot.corr().fillna(0)

    fig = px.imshow(
        corr,
        labels=dict(x="Ticker", y="Ticker", color="Correlation"),
        x=corr.columns,
        y=corr.columns,
        color_continuous_scale="RdBu_r",
        zmin=-1, zmax=1
    )
    fig.update_layout(height=800)
    st.plotly_chart(fig, use_container_width=True)


# Monthly Movers page
elif page == "Monthly Movers":
    st.header("Monthly Top 5 Gainers & Losers")
    rows = []
    for t, g in prices.groupby("ticker"):
        g = g.sort_values("date").set_index("date")
        monthly = g["close"].resample("M").agg(["first","last"]).dropna()
        monthly["monthly_return"] = (monthly["last"] - monthly["first"]) / monthly["first"]
        monthly = monthly.reset_index()
        monthly["ticker"] = t
        rows.append(monthly[["ticker","date","monthly_return"]])
    monthly_df = pd.concat(rows, ignore_index=True)
    months = sorted(monthly_df["date"].dt.strftime("%Y-%m").unique(), reverse=True)
    sel = st.selectbox("Choose month (YYYY-MM)", months)
    this = monthly_df[monthly_df["date"].dt.strftime("%Y-%m")==sel]
    st.subheader("Top 5 Gainers")
    st.table(this.nlargest(5,"monthly_return").rename(columns={"ticker":"Ticker","monthly_return":"MonthlyReturn"})[["Ticker","MonthlyReturn"]])
    st.subheader("Top 5 Losers")
    st.table(this.nsmallest(5,"monthly_return").rename(columns={"ticker":"Ticker","monthly_return":"MonthlyReturn"})[["Ticker","MonthlyReturn"]])
