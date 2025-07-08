# import streamlit as st
# import pandas as pd
# import plotly.express as px

# # Page settings
# st.set_page_config(page_title="Kenya Inflation Dashboard", layout="centered")

# # Title + intro
# st.title("📈 Kenya Inflation Trends Dashboard")
# st.markdown("Visualizing Kenya's inflation rate from 2000 to 2023 using World Bank data.")

# # Load dataset
# df = pd.read_csv("kenya_inflation.csv")

# # Line chart
# fig = px.line(df, x="Year", y="Inflation (%)", markers=True,
#               title="Annual Inflation Rate in Kenya (2000–2023)",
#               labels={"Inflation (%)": "Inflation %", "Year": "Year"})

# st.plotly_chart(fig, use_container_width=True)

# # Checkbox to show raw data
# if st.checkbox("Show Raw Data"):
#     st.subheader("Raw Data")
#     st.write(df)
import streamlit as st
import pandas as pd
import plotly.express as px

# Set page configuration
st.set_page_config(
    page_title="Kenya Inflation Dashboard",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Title
st.title("🇰🇪 Kenya Inflation Dashboard")
st.markdown("Track and visualize Kenya's inflation trends over time.")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("kenya_inflation.csv")
    df["Year"] = pd.to_datetime(df["Year"], format="%Y")
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
min_year = df["Year"].dt.year.min()
max_year = df["Year"].dt.year.max()
selected_years = st.sidebar.slider("Select Year Range:", min_value=int(min_year), max_value=int(max_year),
                                    value=(int(min_year), int(max_year)))

filtered_df = df[(df["Year"].dt.year >= selected_years[0]) & (df["Year"].dt.year <= selected_years[1])]

# Line chart
fig = px.line(
    filtered_df,
    x="Year",
    y="Inflation (%)",  # corrected column name
    title="Kenya Inflation Rate Over Time",
    labels={"Year": "Year", "Inflation (%)": "Inflation Rate (%)"}  # corrected label
)
fig.update_traces(mode="lines+markers")

# Display chart
st.plotly_chart(fig, use_container_width=True)

# Dataframe view
with st.expander("📄 View Data"):
    st.dataframe(filtered_df)

