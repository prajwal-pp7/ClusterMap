import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
import folium
from streamlit_folium import folium_static

st.title("ClusterMap")
st.markdown("---")
st.markdown("Developed by : 210401@iitk.ac.in ")
st.markdown("Project Link : [click here](https://github.com/prajwal-pp7/ClusterMap/tree/main/ClusterMap)")

try:
    df = pd.read_csv('cities2.csv')
except FileNotFoundError:
    st.error("The 'cities2.csv' file was not found. Please make sure it's in the same directory.")
    st.stop()

L2=df[['Latitude','Longitude']]

kmeans=KMeans(n_clusters=10,random_state=0)
kmeans.fit(L2)

df['loc_clusters']=kmeans.labels_

input_city=st.text_input("Enter a city name:")

map_container=st.empty()

if input_city:
    matching_city=df.loc[df['location'].str.contains(input_city,case=False,na=False)]

    if not matching_city.empty:
        cluster=int(matching_city.iloc[0]['loc_clusters'])
        input_lat=matching_city.iloc[0]['Latitude']
        input_lon=matching_city.iloc[0]['Longitude']
        
        cities_in_cluster=df.loc[df['loc_clusters']==cluster].copy()
        
        st.subheader(f"Cities in the same cluster as {input_city}:")
        for c in cities_in_cluster['location']:
            if c.lower()!=input_city.lower():
                st.write(f"- {c}")

        m = folium.Map(location=[input_lat,input_lon],zoom_start=6)

        folium.Marker(
            location=[input_lat,input_lon],
            popup=f"You searched for:{input_city}",
            icon=folium.Icon(color="red", icon="home")
        ).add_to(m)

        for index, row in cities_in_cluster.iterrows():
            if row['location'].lower()!=input_city.lower():
                folium.Marker(
                    location=[row['Latitude'],row['Longitude']],
                    popup=row['location'],
                    icon=folium.Icon(color="blue",icon="info-sign")
                ).add_to(m)

        map_container.subheader("Geographical Locations of Recommended Cities")
        folium_static(m,width=700)
    else:
        st.write("City not found in the dataset.")
        map_container.empty()
else:
    st.info("Please enter a city name to get recommendations.")
    map_container.empty()

silhouette_avg = silhouette_score(L2,kmeans.labels_)
st.write(f"Silhouette Score: {silhouette_avg}")