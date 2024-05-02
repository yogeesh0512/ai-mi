import streamlit as st
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.cluster import KMeans
from sklearn.manifold import TSNE
import plotly.express as px
from collections import defaultdict

st.title('Song Recommender')

# Sample data for demonstration
data = pd.DataFrame({
    'name': ['Come As You Are', 'Smells Like Teen Spirit', 'Lithium', 'All Apologies', 'Stay Away'],
    'year': [1991, 1991, 1992, 1993, 1993],
    # Add other columns as needed
})

@st.cache
def get_mean_vector(song_list):
    song_vectors = []
    for song in song_list:
        # Add code to get song features based on name and year
        song_vector = np.random.rand(15)  # Sample data for demonstration
        song_vectors.append(song_vector)
    return np.mean(song_vectors, axis=0)

def recommend_songs(song_list, n_songs=5):
    song_center = get_mean_vector(song_list)
    # Add code to calculate distances and recommend songs based on the clustering model
    # For demonstration, returning random songs
    recommended_songs = data.sample(n_songs)
    return recommended_songs

song_list = []
for i in range(5):
    name = st.text_input(f"Song {i+1} Name")
    year = st.number_input(f"Song {i+1} Year", min_value=1900, max_value=2022)
    song_list.append({'name': name, 'year': year})

if st.button('Recommend Songs'):
    recommended_songs = recommend_songs(song_list)
    st.write('Recommended Songs:')
    st.write(recommended_songs[['name', 'year']])


