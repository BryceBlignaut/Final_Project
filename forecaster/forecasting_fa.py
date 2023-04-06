#%%
import pandas as pd
import numpy as np
from prophet import Prophet

# %%
df = pd.read_excel('fa_data.xlsx')
# %%
df['Created'] = pd.to_datetime(df['Created'])
# %%
df = df.rename(columns={'Office List 1':'y', 'Created':'ds'})
# %%
df = df[['ds', 'y']]

# Extract the day of the week as an integer (0 = Monday, 1 = Tuesday, ..., 6 = Sunday)
df['day_of_week'] = df['ds'].dt.dayofweek

# Remove all rows where 'day_of_week' is 6 (Sunday)
df = df[df['day_of_week'] != 6]
df = df[df['day_of_week'] != 5]

# Drop the 'day_of_week' column as it's no longer needed
df.drop('day_of_week', axis=1, inplace=True)


# %%
df_count = df.set_index('ds')

df_count = df_count.groupby(pd.Grouper(freq='D')).count()
df_count = df_count.reset_index()
upper_threshold = 2
lower_threshold = 500
df_count = df_count.query('y > @upper_threshold')
df_count = df_count.query('y <= @lower_threshold')
df_count.head(20)
#%%
min_value_A = df_count['y'].min()

print(min_value_A)


# %%
m = Prophet(seasonality_mode='multiplicative')
m.add_seasonality(name='daily',period=1, fourier_order=10)
# m.add_seasonality(name='weekly', period=7, fourier_order=3)
m.add_seasonality(name='yearly', period=365.25, fourier_order=10)
m.fit(df_count)
# %%
future = m.make_future_dataframe(periods=32)
# %%
forecast = m.predict(future)
# %%
floor_value = 0 # Set the desired floor value
forecast['yhat'] = forecast['yhat'].clip(lower=floor_value) # Clip forecasted values below the floor value
forecast['yhat_lower'] = forecast['yhat_lower'].clip(lower=floor_value)
# Access the forecasted values with the floor applied
forecast_with_floor = forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']]
# %%
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12)
# %%
m.plot(forecast_with_floor);
# %%
