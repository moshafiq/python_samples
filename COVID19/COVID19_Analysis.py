#!/usr/bin/env python
# coding: utf-8




import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

confirmed_df = pd.read_csv("time_series_covid19_confirmed_global.csv")
deaths_df = pd.read_csv("time_series_covid19_deaths_global.csv")
recovered_df = pd.read_csv("time_series_covid19_recovered_global.csv")

confirmed_df

deaths_df

recovered_df

confirmed_df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)
deaths_df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)
recovered_df.drop(columns=["Province/State", "Lat", "Long"], inplace=True)

confirmed_df = confirmed_df.groupby("Country/Region").sum().reset_index()
deaths_df = deaths_df.groupby("Country/Region").sum().reset_index()
recovered_df = recovered_df.groupby("Country/Region").sum().reset_index()

confirmed_melt = confirmed_df.melt(id_vars=["Country/Region"], var_name="Date", value_name="Confirmed")
deaths_melt = deaths_df.melt(id_vars=["Country/Region"], var_name="Date", value_name="Deaths")
recovered_melt = recovered_df.melt(id_vars=["Country/Region"], var_name="Date", value_name="Recovered")

confirmed_df

deaths_df

recovered_df


covid_df = pd.merge(confirmed_melt, deaths_melt, on=["Country/Region", "Date"])
covid_df = pd.merge(covid_df, recovered_melt, on=["Country/Region", "Date"])

covid_df


covid_df['Date'] = pd.to_datetime(covid_df['Date'])


plt.figure(figsize=(12, 6))
sns.lineplot(x='Date', y='Confirmed', data=covid_df, label='Confirmed')
sns.lineplot(x='Date', y='Deaths', data=covid_df, label='Deaths')
sns.lineplot(x='Date', y='Recovered', data=covid_df, label='Recovered')
plt.title('Global COVID-19 Cases Over Time')
plt.xlabel('Date')
plt.ylabel('Number of Cases')
plt.xticks(rotation=45)
plt.legend()
plt.show()






 




