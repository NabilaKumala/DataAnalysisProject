import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_holiday_bs(df):
    holiday_bs = df[(df['holiday'] == 1)].groupby(by="dteday").agg({
        "cnt": "max",
        "weekday": "min"
    }).sort_values(by="cnt", ascending=False)
    return holiday_bs

def create_workday_bs(df):
    workday_bs = df[(df['workingday'] == 1)].groupby(by="dteday").agg({
        "cnt": "max",
        "weekday": "min"
    }).sort_values(by="cnt", ascending=False)
    return workday_bs

def create_monthly_bs(df):
    monthly_bs = df.resample(rule='M', on='dteday').agg({
        "cnt": "sum"
    })
    monthly_bs.index = monthly_bs.index.strftime('%Y-%m')
    monthly_bs = monthly_bs.reset_index()
    monthly_bs.rename(columns={
        "dteday": "year_month",
        "cnt": "total"
    }, inplace=True)
    return monthly_bs

def create_season_bs(df):
    season_bs = df.groupby(by="season").agg({
        "cnt": "sum",
        "weathersit": "mean",
        "temp": "mean",
        "atemp": "mean",
        "hum": "mean",
        "windspeed": "mean"
    }).sort_values(by="cnt", ascending=False)
    return season_bs

def create_spring_bs(df):
    spring_bs = df[(df['season'] == 1)]
    return spring_bs

def create_summer_bs(df):
    summer_bs = df[(df['season'] == 2)]
    return summer_bs

def create_fall_bs(df):
    fall_bs = df[(df['season'] == 3)]
    return fall_bs

def create_winter_bs(df):
    winter_bs = df[(df['season'] == 4)]
    return winter_bs

bikeshare_df = pd.read_csv("bikeshare.csv")

bikeshare_df.sort_values(by="dteday", inplace=True)
bikeshare_df.reset_index(inplace=True)
bikeshare_df["dteday"] = pd.to_datetime(bikeshare_df["dteday"])

min_date = bikeshare_df["dteday"].min()
max_date = bikeshare_df["dteday"].max()
 
with st.sidebar:
    # Menambahkan logo perusahaan
    st.image("https://i.pinimg.com/736x/3f/11/f6/3f11f65984821992489493152b2b1dd2.jpg")
    
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu',min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

main_df = bikeshare_df[(bikeshare_df["dteday"] >= str(start_date)) & 
                (bikeshare_df["dteday"] <= str(end_date))]

holiday_bs = create_holiday_bs(main_df)
workday_bs = create_workday_bs(main_df)
monthly_bs = create_monthly_bs(main_df)
season_bs = create_season_bs(main_df)
spring_bs = create_spring_bs(main_df)
summer_bs = create_summer_bs(main_df)
fall_bs = create_fall_bs(main_df)
winter_bs = create_winter_bs(main_df)

st.header('Bike Sharing Dashboard 	:bike:')

st.subheader('Monthly Bike Users')

col1, col2 = st.columns(2)
 
with col1:
    total_holiday = holiday_bs.cnt.sum()
    st.metric("Number of User in Holiday", value=total_holiday)
 
with col2:
    total_workday = workday_bs.cnt.sum()
    st.metric("Number of User in Working Day", value=total_workday)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    monthly_bs["year_month"],
    monthly_bs["total"],
    marker='o', 
    linewidth=2,
    color="#3E4E50"
)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=8)
 
st.pyplot(fig)


st.subheader("Bike Users per Season")
 
col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))

    colors = ["#EBB3A9", "#E86252", "#EBB3A9", "#EBB3A9", "#EBB3A9"]
 
    sns.barplot(
        y="cnt", 
        x="dteday",
        data=spring_bs,
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of User in Spring", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=4)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#F8FA90", "#2AB7CA", "#F8FA90", "#F8FA90", "#F8FA90"]
 
    sns.barplot(
        y="cnt", 
        x="dteday",
        data=summer_bs,
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of User in Summer", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=4)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

col1, col2 = st.columns(2)
 
with col1:
    fig, ax = plt.subplots(figsize=(20, 10))

    colors = ["#FFB563", "#A63C06", "#FFB563", "#FFB563", "#FFB563"]
 
    sns.barplot(
        y="cnt", 
        x="dteday",
        data=fall_bs,
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of User in Fall", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=4)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)
 
with col2:
    fig, ax = plt.subplots(figsize=(20, 10))
    
    colors = ["#BFDBF7", "#1F7A8C", "#BFDBF7", "#BFDBF7", "#BFDBF7"]
 
    sns.barplot(
        y="cnt", 
        x="dteday",
        data=winter_bs,
        palette=colors,
        ax=ax
    )
    ax.set_title("Number of User in Winter", loc="center", fontsize=50)
    ax.set_ylabel(None)
    ax.set_xlabel(None)
    ax.tick_params(axis='x', labelsize=4)
    ax.tick_params(axis='y', labelsize=30)
    st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    bikeshare_df["dteday"],
    bikeshare_df["cnt"],
    marker='o', 
    linewidth=2,
    color="#B0CA87"
)
ax.set_title("Number of User Through Seasons", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=8)
 
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(20, 10))
colors = ["#E86252", "#2AB7CA", "#A63C06", "#1F7A8C"]
sns.barplot(
    x="season", 
    y="cnt",
    data=bikeshare_df.sort_values(by="cnt", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Number of User per Season", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=35)
st.pyplot(fig)
st.caption('Notes:')
st.caption('1 = Spring :cherry_blossom:, 2 = Summer :sunny:, 3 = Fall :fallen_leaf:, 4 = Winter :snowflake:')


st.subheader('Weather Conditions Through Seasons')

fig, ax = plt.subplots(figsize=(16, 8))
colors = ["#00ABE7", "#DDD8C4", "#A0AAB2", "#3D5A6C"]
sns.barplot(
    x="weathersit", 
    y="cnt",
    data=bikeshare_df.sort_values(by="cnt", ascending=False),
    palette=colors,
    ax=ax
)
ax.set_title("Weather Situation", loc="center", fontsize=30)
ax.set_ylabel(None)
ax.set_xlabel(None)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=20)
st.pyplot(fig)
st.caption('Notes:')
st.caption('1 = Clear, Few clouds, Partly cloudy :sun_small_cloud:')
st.caption('2 = Mist + Cloudy, Mist + Broken clouds, Mist + Few clouds, Mist :cloud:')
st.caption('3 = Light Snow, Light Rain + Thunderstorm + Scattered clouds, Light Rain + Scattered clouds :rain_cloud:')
st.caption('4 = Heavy Rain + Ice Pallets + Thunderstorm + Mist, Snow + Fog :thunder_cloud_and_rain:')

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    bikeshare_df["dteday"],
    bikeshare_df["temp"],
    marker='o', 
    linewidth=2,
    color="#F4B942"
)
ax.set_title("Temperature", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=8)
 
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    bikeshare_df["dteday"],
    bikeshare_df["atemp"],
    marker='o', 
    linewidth=2,
    color="#F3E37C"
)
ax.set_title("Temperature (Feels like...)", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=8)
 
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    bikeshare_df["dteday"],
    bikeshare_df["hum"],
    marker='o', 
    linewidth=2,
    color="#ACCBE1"
)
ax.set_title("Humidity", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=8)
 
st.pyplot(fig)

fig, ax = plt.subplots(figsize=(16, 8))
ax.plot(
    bikeshare_df["dteday"],
    bikeshare_df["windspeed"],
    marker='o', 
    linewidth=2,
    color="#97D8C4"
)
ax.set_title("Wind Speed", loc="center", fontsize=30)
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=8)
 
st.pyplot(fig)