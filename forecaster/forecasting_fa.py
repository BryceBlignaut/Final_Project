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
len(df)

# %%
df_count = df.set_index('ds')

df_count = df_count.groupby(pd.Grouper(freq='D')).count()
df_count = df_count.reset_index()
threshold = 3
df_count = df_count.query('y > @threshold')
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
future = m.make_future_dataframe(periods=52)
# %%
forecast = m.predict(future)
# %%
forecast.head()
# %%
forecast[['ds', 'yhat', 'yhat_lower', 'yhat_upper']].tail(12)
# %%
m.plot(forecast);
# %%
