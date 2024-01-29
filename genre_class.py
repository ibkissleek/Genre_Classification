import streamlit as st
import pandas as pd
import numpy as np
import pickle
from sklearn import preprocessing

loaded_model = pickle.load(open('model.sav', 'rb'))

def prediction(data):

    gc = pd.DataFrame(data)

    label = preprocessing.LabelEncoder()

    gc.iloc[0] = label.fit_transform(gc.iloc[0])
    gc.iloc[1] = label.fit_transform(gc.iloc[1])
    gc.iloc[2] = label.fit_transform(gc.iloc[2])
    gc.iloc[3] = label.fit_transform(gc.iloc[3])
    num_data = gc.drop([4, 5, 12]).values.reshape(1, -1)

    pred = loaded_model.predict(num_data)


    if pred[0] == 0:
        return "Missing"
    elif pred[0] == 1:
        return "afro dancehall"
    elif pred[0]== 2:
        return "afro r&b"
    elif pred[0]== 3:
        return "afropop"
    elif pred[0]== 4:
        return "afroswing"
    elif pred[0]== 5:
        return "alternative r&b"
    elif pred[0]== 6:
        return "azonto"
    elif pred[0]== 7:
        return "azontobeats"
    elif pred[0]== 8:
        return "bongo flava"
    elif pred[0]== 9:
        return "christian afrobeat"
    elif pred[0]== 10:
        return "erotica"
    elif pred[0]== 11:
        return "gqom"
    elif pred[0]== 12:
        return "highlife"
    elif pred[0]== 13:
        return "hiplife"
    elif pred[0]== 14:
        return "indie r&b"
    elif pred[0]== 15:
        return "nigerian hip hop"
    elif pred[0]== 16:
        return "nigerian pop"
    elif pred[0]== 17:
        return "soft rock"
    elif pred[0]== 18:
        return "south african house"
    
    

def main():
    
    st.title("Genre Identification Predictive Model")
    name = st.text_input("Song title")
    album = st.text_input("Album title")
    artist = st.text_input("Name of the artist")
    release_date = st.number_input("Year of release")
    length = st.number_input("Duration of song in seconds")
    popularity = st.number_input("Nummber of popularity")          
    danceability = st.number_input("Nummber of danceability")
    acousticness = st.number_input("Number of acousticness")
    energy = st.number_input("Number of energy")
    instrumentalness = st.number_input("Number of instrumentalness")
    liveness = st.number_input("Number of liveness")
    loudness = st.number_input("Loudness of the song")
    speechiness = st.number_input("number of speechiness")
    tempo = st.number_input("Tempo of the song")
    time_signature = st.number_input("Time signature of the song")
    


    artist_top_genre = " "       


    if st.button("Result"):
        artist_top_genre = prediction([name, album, artist, release_date, length, popularity, danceability, 
                                   acousticness, energy, instrumentalness, 
                                   liveness, loudness, speechiness, tempo, time_signature])
        

    st.success(artist_top_genre)


if __name__ == "__main__":
     main()

