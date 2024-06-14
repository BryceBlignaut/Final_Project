import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import plotly as plt
import plotly.express as px
import datetime

# 1=sidebar menu, 2=horizontal menu, 3=horizontal menu w/ custom menu

# Read and Wrangle Data
df = pd.read_csv('data/forecast_neural_exp_2017_2022.csv')
today = datetime.datetime.now()
tomorrow = datetime.datetime.now() + datetime.timedelta(days=1)

# Create new date column for filtering
df['date_no_hour'] = df['date'].str[:10]
df['date_no_hour'] = pd.to_datetime(df['date_no_hour'])
#df['date_no_hour'] = pd.to_datetime(df['date_no_hour'])

# Change date format

df = df[['date_no_hour','date','calls','agents']]

# Streamlit Menu
EXAMPLE_NO = 1

def streamlit_menu(example=1):
    if example == 1:
        # 1. as sidebar menu
        with st.sidebar:
            selected = option_menu(
                menu_title="Main Menu",  # required
                options=["Home", "Phones", "Email/Chats"],  # required
                icons=["house", "phone", "chat-dots"],  # optional
                menu_icon="cast",  # optional
                default_index=0,  # optional
            )
        return selected


selected = streamlit_menu(example=EXAMPLE_NO)

# Page Information
if selected == "Home":
    st.title(f"{selected}")
    st.subheader("Call Volume and Agent Staffing Predictions for University Call Center")
    st.subheader('')

    st.write("The predictions range from 12/02/2022 - 01/12/2023. Filter the date selectors accordingly.")
    st.write("The number of call center agents needed for each shift is calculated through a function where the call volume prediction as an input.")

    # date selector and dataset filtering
    start_date = st.date_input('Start date', value= datetime.date(2022,12,2))
    end_date = st.date_input('End date', value= tomorrow)

    if start_date <= end_date:
        st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))

        df2 = df[df["date_no_hour"].isin(pd.date_range(start_date, end_date))]

        df3 = df2[['date','calls','agents']]

        st.line_chart(data= df3, x = 'date', width= 950 , height= 600, use_container_width= False)
        st.write(df2)
    else:
        st.error('Error: End date must fall after start date.')


if selected == "Phones":
    st.title(f"{selected}")

    # date selector and dataset filtering

    start_date = st.date_input('Start date', value= today)
    end_date = st.date_input('End date', value= tomorrow)

    if start_date <= end_date:
        st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))

        df2 = df[df["date_no_hour"].isin(pd.date_range(start_date, end_date))]

        df3 = df2[['date','calls','agents']]

        st.line_chart(df3)
        st.write(df2)
    else:
        st.error('Error: End date must fall after start date.')



if selected == "Email/Chats":
    st.title(f"{selected}")




