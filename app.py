import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(layout="wide")
st.title("🌍 Air Quality Intelligence Dashboard (Spark Powered)")

# ---------------- LOAD DATA ----------------
@st.cache_data
def load_data():
    totaldata=pd.read_csv("data/INDIA_AQI_COMPLETE_20251126.csv")
    trend = pd.read_csv("trend.csv")
    hourly = pd.read_csv("hourly.csv")
    city = pd.read_csv("city.csv")
    heatmap = pd.read_csv("heatmap.csv")
    corr = pd.read_csv("corr.csv")
    map_df = pd.read_csv("map.csv")
    return totaldata,trend, hourly, city, heatmap, corr, map_df

totaldata,trend, hourly, city, heatmap, corr_df, map_df = load_data()

# ---------------- TABS ----------------
tab1, tab2, tab3, tab4 = st.tabs([
    "📈 Trends",
    "🔥 Analysis",
    "🌍 Map",
    "🧠 Insights"
])

# ================= TAB 1 =================
with tab1:
    totaldata["Datetime"] = pd.to_datetime(totaldata["Datetime"])

    trend_df = totaldata.groupby(
        totaldata["Datetime"].dt.date
    )["US_AQI"].mean().reset_index()

    fig = px.line(
        trend_df,
        x="Datetime",
        y="US_AQI",
        title="Daily AQI Trend"
    )

    st.plotly_chart(fig, use_container_width=True)
    totaldata["Hour"] = totaldata["Datetime"].dt.hour

    hourly_df = totaldata.groupby("Hour")["US_AQI"].mean().reset_index()

    fig2 = px.line(
        hourly_df,
        x="Hour",
        y="US_AQI",
        title="Hourly AQI Pattern"
    )

    st.plotly_chart(fig2, use_container_width=True)

# ================= TAB 2 =================
with tab2:
    st.subheader("📊 City-wise AQI Comparison")

    top_n = st.slider("Select Top N Cities", 5, 20, 10)

    top_cities = city.sort_values("AQI", ascending=False).head(top_n)

    fig3 = px.bar(
        top_cities,
        x="City",
        y="AQI",
        color="AQI",
        color_continuous_scale="Reds"
    )
    st.plotly_chart(fig3, use_container_width=True)

    # 🔥 NEW: Bottom cities
    st.subheader("🟢 Least Polluted Cities")

    bottom_cities = city.sort_values("AQI").head(top_n)

    fig_bottom = px.bar(
        bottom_cities,
        x="City",
        y="AQI",
        color="AQI",
        color_continuous_scale="Greens"
    )
    st.plotly_chart(fig_bottom, use_container_width=True)

    st.subheader("Heatmap (Month vs Hour)")
    pivot = heatmap.pivot(index="Month", columns="Hour", values="AQI")

    fig4, ax = plt.subplots()
    sns.heatmap(pivot, cmap="coolwarm", ax=ax)
    st.pyplot(fig4)

    st.subheader("Correlation Matrix")
    corr_matrix = corr_df.corr()

    fig5, ax2 = plt.subplots()
    sns.heatmap(corr_matrix, annot=True, ax=ax2)
    st.pyplot(fig5)

# ================= TAB 3 =================
with tab3:
    st.subheader("🌍 AQI Map")

    # 🔥 AQI Filter
    min_aqi, max_aqi = st.slider("Filter AQI Range", 0, 300, (0, 200))

    filtered_map = map_df[
        (map_df["US_AQI"] >= min_aqi) &
        (map_df["US_AQI"] <= max_aqi)
    ]

    fig_map = px.scatter_mapbox(
        filtered_map.sample(min(2000, len(filtered_map))),
        lat="Latitude",
        lon="Longitude",
        color="US_AQI",
        size="US_AQI",
        color_continuous_scale=[
            (0.0, "green"),
            (0.25, "yellow"),
            (0.5, "orange"),
            (0.75, "red"),
            (1.0, "darkred")
        ],
        mapbox_style="open-street-map",
        zoom=4
    )

    st.plotly_chart(fig_map, use_container_width=True)

# ================= TAB 4 =================
with tab4:
    st.subheader("Smart Insights")

    most_polluted = city.sort_values("AQI", ascending=False).iloc[0]["City"]
    cleanest = city.sort_values("AQI").iloc[0]["City"]

    st.write(f"🔴 Most polluted city: **{most_polluted}**")
    st.write(f"🟢 Least polluted city: **{cleanest}**")

    avg_aqi = city["AQI"].mean()

    if avg_aqi > 150:
        st.error("Air quality is unhealthy overall")
    elif avg_aqi > 100:
        st.warning("Air quality is moderate")
    else:
        st.success("Air quality is good")

    st.subheader("Top Polluted Cities")
    st.dataframe(city.sort_values("AQI", ascending=False).head(10))

# ---------------- FOOTER ----------------
st.caption("Big Data Analytics using Apache Spark + Streamlit")