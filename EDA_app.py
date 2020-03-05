# Himanshu Tripathi


import streamlit as st
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
import pydeck as pdk
from PIL import Image
import seaborn as sns

plt.style.use('ggplot')

def main():
	st.title('Coronavirus EDA in Web')
	st.sidebar.title('Coronavirus')
	image = Image.open('img.jpg')
	st.sidebar.image(image, caption='Coronaviruse', use_column_width=True)
	st.sidebar.subheader('Coronaviruses (CoV) are a large family of viruses that cause illness ranging from the common cold to more severe diseases such as Middle East Respiratory Syndrome (MERS-CoV) and Severe Acute Respiratory Syndrome (SARS-CoV). A novel coronavirus (nCoV) is a new strain that has not been previously identified in humans. ')
	
	data = pd.read_csv('data.csv')
	data.rename(columns={'Province/State':'Province_State', 'Country/Region':'Country_Region'},inplace=True)
	data.rename(columns={'Lat':'lat', 'Long':'lon'},inplace=True)
	data = data[['Province_State', 'Country_Region', 'lat', 'lon', 'Date',
       'Confirmed', 'Deaths', 'Recovered', 'geometry']]
	if st.checkbox("show Data"):
		st.write(data)

	if st.checkbox("Show Head of the data"):
		st.write(data.head())

	if st.checkbox("Check Shape"):
		st.write(data.shape)

	if st.checkbox("Show All Columns name"):
		st.write(data.columns)

	if st.checkbox("Describe Data"):
		st.write(data.describe())

	if st.checkbox("Check Null Values"):
		st.write(data.isna().sum().to_frame().sort_values(0).style.background_gradient(cmap='summer_r'))

	st.subheader("Per day (Confirmed, Deaths, and Recovered) Patient")
	if st.checkbox("Check Per Day"):
		df_perday = data.groupby('Date')['Confirmed', 'Deaths', 'Recovered'].max()
		st.write(df_perday)
		st.write(df_perday.plot())
		st.pyplot()

	st.subheader("Group Data by (State and Country Region)")
	if st.checkbox("Group Data"):
		d = data.groupby(['Province_State','Country_Region'])['Confirmed', 'Deaths', 'Recovered'].max()
		d.style.background_gradient(cmap='Pastel1_r')
		st.write(d)


	st.subheader("Which Country has the most affected people?")
	if st.checkbox("Show "):
		st.write(data['Country_Region'].value_counts().plot(kind='bar',figsize=(20,10)))
		st.pyplot()

	st.subheader(" Most Deaths with respect to Country")
	if st.checkbox("Show Plot"):
		plt.figure(figsize=(20,10))
		st.write(data.groupby(['Country_Region'])['Deaths'].max().plot(kind='bar',figsize=(20,10)))
		plt.yticks(rotation=45)
		st.pyplot()

	st.subheader("scatter plot between Confirmed and Recovered Patient")
	if st.checkbox("Scatter Plot"):
		st.write(sns.relplot(x='Confirmed',y='Recovered',data=data,hue='Recovered'))
		st.pyplot()

	st.subheader("Death with respect to Date")
	if st.checkbox("Death=>Date"):
		plt.figure(figsize=(20,10))
		plt.xlabel('Deaths')
		plt.ylabel('Date');
		st.write(plt.plot(data['Deaths'],data['Date'],c='r',marker='o',linewidth=2))
		
		st.pyplot()


	st.subheader("Interactive Geographical data visualization")
	if st.checkbox("Visualization"):
		st.deck_gl_chart(
            viewport={
                'latitude': data['lat'][0],
                'longitude':  data['lon'][0],
                'zoom': 4
            },
            layers=[{
                'type': 'ScatterplotLayer',
                'data': data,
                'radiusScale': 250,
	   			'radiusMinPixels': 5,
	                'getFillColor': [248, 24, 148],
	            }]
	        )

	st.title("Himanshu Tripathi")
	st.subheader("Thanks For Watching")

if __name__ == '__main__':
	main()