import pandas as pd
import plotly.express as px
import streamlit as st

st.set_page_config(
    page_title="Formula 1 Performance Analysis", page_icon="🏎️", layout="wide"
)

# Title & Overview
st.title("🏎️ Formula 1 Race Intelligence Dashboard")
st.caption("Interactive analysis of race results, driver reliability, constructor performance, and tyre strategies.")

# Load Data
@st.cache_data
def load_data():
    file_path = "F1 Racing Project Dataset.xlsx"
    df = pd.read_excel(file_path, sheet_name="race_results")
    return df

try:
    df = load_data()
except Exception as e:
    st.error(f"Failed to load dataset: {e}")
    st.stop()

# Data Preprocessing
df["dnf"] = pd.to_numeric(df["dnf"], errors="coerce").fillna(0)
df["points"] = pd.to_numeric(df["points"], errors="coerce").fillna(0)
df["laps_led"] = pd.to_numeric(df["laps_led"], errors="coerce").fillna(0)

# Sidebar Filters
st.sidebar.header("Filters")

# Season Filter
seasons = sorted(df["season"].dropna().unique().astype(int))
selected_seasons = st.sidebar.multiselect("Season", seasons, default=seasons)

# Team Filter
teams = sorted(df["team"].dropna().unique())
selected_teams = st.sidebar.multiselect("Team", teams, default=teams)

# Driver Filter
drivers = sorted(df["driver"].dropna().unique())
selected_drivers = st.sidebar.multiselect("Driver", drivers, default=drivers)

# Filter Dataframe
filtered_df = df[
    (df["season"].isin(selected_seasons))
    & (df["team"].isin(selected_teams))
    & (df["driver"].isin(selected_drivers))
]

if filtered_df.empty:
    st.info("No data available for the selected filters. Please adjust your selections.")
    st.stop()

# Key Metrics KPI Row
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Races Analyzed", filtered_df["race_id"].nunique())
col2.metric("Total Drivers", filtered_df["driver"].nunique())
col3.metric("Total Constructors", filtered_df["team"].nunique())
col4.metric("Total Points Scored", int(filtered_df["points"].sum()))

st.markdown("---")

# Row 1: Constructor Points & Driver Leaderboard
r1_left, r1_right = st.columns(2)

with r1_left:
    st.subheader("01. Constructor Championship Points by Season")
    team_season = (
        filtered_df.groupby(["season", "team"], as_index=False)["points"]
        .sum()
    )
    fig1 = px.bar(
        team_season,
        x="team",
        y="points",
        color="season",
        barmode="group",
        title="Constructor Points Comparison",
        labels={"team": "Constructor", "points": "Points", "season": "Season"},
    )
    fig1.update_layout(xaxis_tickangle=-35)
    st.plotly_chart(fig1, use_container_width=True)

with r1_right:
    st.subheader("04. Driver Leaderboard by Total Points")
    driver_pts = (
        filtered_df.groupby(["driver", "team"], as_index=False)["points"]
        .sum()
        .sort_values("points", ascending=False)
        .head(10)
    )
    fig4 = px.bar(
        driver_pts,
        x="points",
        y="driver",
        color="team",
        orientation="h",
        title="Top 10 Drivers by Points",
        labels={"points