import streamlit as st
import pandas as pd
from sklearn.cluster import KMeans
import folium
from streamlit_folium import folium_static
from PIL import Image

# Set page configuration, including a title and favicon
try:
    favicon = Image.open('favicon.ico')
    st.set_page_config(
        page_title="ClusterMap",
        page_icon=favicon
    )
except FileNotFoundError:
    st.set_page_config(page_title="ClusterMap")

# --- UI and Styling ---
st.markdown("<h1><a href='.' style='text-decoration: none; color: inherit;'>ClusterMap</a></h1>", unsafe_allow_html=True)
st.markdown("---")

# --- Data Loading ---
try:
    df = pd.read_csv('cities2.csv')
    cities_list = pd.read_csv('cities.csv')['cities'].tolist()
except FileNotFoundError as e:
    st.error(f"Error loading data file: {e.filename} was not found. Please ensure it's in the correct directory.")
    st.stop()

# --- Clustering Logic ---
L2 = df[['Latitude', 'Longitude']]
kmeans = KMeans(n_clusters=10, random_state=0)
kmeans.fit(L2)
df['loc_clusters'] = kmeans.labels_

# --- User Input ---
input_city = st.selectbox("Enter a city name:", options=[''] + sorted(cities_list))

# --- Main Application Logic ---
map_container = st.empty()

if input_city:
    matching_city = df.loc[df['location'].str.lower() == input_city.lower()]

    if not matching_city.empty:
        # Get cluster and location details for the selected city
        cluster = int(matching_city.iloc[0]['loc_clusters'])
        input_lat = matching_city.iloc[0]['Latitude']
        input_lon = matching_city.iloc[0]['Longitude']
        
        cities_in_cluster = df.loc[df['loc_clusters'] == cluster].copy()
        
        # Display the list of recommended cities
        st.subheader(f"Cities in the same cluster as '{input_city}':")
        for c in cities_in_cluster['location']:
            if c.lower() != input_city.lower():
                st.write(f"- {c}")

        # Create and display the map
        m = folium.Map(location=[input_lat, input_lon], zoom_start=6)

        # Add a special marker for the user's selected city
        folium.Marker(
            location=[input_lat, input_lon],
            popup=f"You searched for: {input_city}",
            icon=folium.Icon(color="red", icon="home")
        ).add_to(m)

        # Add markers for all other cities in the same cluster
        for index, row in cities_in_cluster.iterrows():
            if row['location'].lower() != input_city.lower():
                folium.Marker(
                    location=[row['Latitude'], row['Longitude']],
                    popup=row['location'],
                    icon=folium.Icon(color="blue", icon="info-sign")
                ).add_to(m)

        st.subheader("Geographical Locations of Recommended Cities")
        folium_static(m, width=700)
    else:
        st.write("City not found in the dataset.")
        map_container.empty()
else:
    st.info("Please enter a city name to get recommendations.")
    map_container.empty()

# --- Footer ---
footer_html = """
<style>
div.stApp {
    padding-bottom: 4rem;
}
.footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: var(--secondary-background-color);
    color: var(--text-color);
    padding: 10px 1rem;
    box-sizing: border-box;
    border-top: 1px solid rgba(0,0,0,.1);
    z-index: 99;
}
.footer-container {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
}
.footer a {
    color: #4F8BF9;
    text-decoration: none;
}
.footer a:hover {
    text-decoration: underline;
}
</style>

<div class="footer">
    <div class="footer-container">
        <span>Developed by : <a href="mailto:210401@iitk.ac.in">210401@iitk.ac.in</a></span>
        <a href="https://github.com/prajwal-pp7/ClusterMap/tree/main/ClusterMap" target="_blank">Project Link</a>
    </div>
</div>
"""
st.markdown(footer_html, unsafe_allow_html=True)