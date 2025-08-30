# ClusterMap                                      ###[Link](https://clustermap.streamlit.app/)

This project is a web-based application that recommends cities to users based on their geographical proximity. It uses a machine learning clustering algorithm to group cities with similar locations.

### Key Components

* **Data-Driven:** The system uses a dataset of cities with their latitude and longitude coordinates.
* **Clustering:** It employs the K-Means clustering algorithm to create logical groups of cities. A **Silhouette Score** is provided to measure how well the cities are clustered together.
* **Interactive Map:** The recommendations are visualized on an interactive map, highlighting the entered city and the suggested destinations.

---

### Understanding the Silhouette Score

The Silhouette Score is a measure of how well-defined your clusters are. The score ranges from -1 to +1.

* A score close to **+1** indicates that the data points are in a cluster that is well-separated from other clusters.
* A score close to **0** indicates that the clusters are overlapping and not clearly separated.
* A score close to **-1** indicates that data points have been assigned to the wrong clusters.

---

### Step-by-Step Instructions to Run the Application

Follow these steps to set up and run the project on your local machine.

#### Step 1: Download and Prepare the Project Files

1.  Download the project files from the GitHub repository page by clicking "Download ZIP".
2.  Unzip the downloaded folder to a location on your computer.
3.  Place the provided Python script (`app.py`) and the data file (`cities2.csv`) in the same folder.
4.  Ensure you have **Python** installed on your system.

#### Step 2: Install Required Libraries

1.  Open your **Command Prompt (CMD)**.
2.  Navigate to your project folder using the `cd` command.
    * Example: `cd C:\Users\YourName\Documents\MyProject`
3.  Install all the necessary libraries by typing the following command and pressing Enter:
    ```bash
    pip install streamlit pandas scikit-learn folium streamlit-folium
    ```

#### Step 3: Run the Application

1.  In the same Command Prompt window, type this command and press Enter:
    ```bash
    streamlit run app.py
    ```
2.  A web browser will open automatically, showing your application. You can now enter a city name from the list of cities provided to receive your recommendations.
