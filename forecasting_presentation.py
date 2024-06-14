import streamlit as st
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


st.title(f"University Call Center Volume and Staffing Predictions")
st.subheader("Call volume and agent staffing predictions for a university Call Center")
st.subheader('')

st.write("The predictions range from 12/02/2022 - 01/12/2023. Filter the date selectors accordingly.")
st.write("The number of call center agents needed for each shift is calculated through a function where the call volume prediction is an input.")

# date selector and dataset filtering
start_date = st.date_input('Start date', value= datetime.date(2022,12,2))
end_date = st.date_input('End date', value= tomorrow)

if start_date <= end_date:
    st.success('Start date: `%s`\n\nEnd date:`%s`' % (start_date, end_date))

    df2 = df[df["date_no_hour"].isin(pd.date_range(start_date, end_date))]

    df3 = df2[['date','calls','agents']]
    st.header("Call Volume and Staffing Requirements")

    st.line_chart(data= df3,  x = 'Shift Date and Time', y = 'Call Volumes and Agents Needed' , width= 950 , height= 600, use_container_width= False)
    st.dataframe(df2, width= 1200)
else:
    st.error('Error: End date must fall after start date.')





