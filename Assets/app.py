# to run the file: type in developer command prompt: streamlit run app.py


import streamlit as st
import pickle               # to load the pickle objects
import pandas as pd


#-----------recommend function definition-----------
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]         # get the index of selected movie
    distances = similarity[movie_index]                             # get the cosine distances of the selected movie and all the rest movies
    movies_list = sorted(list(enumerate(distances)), reverse = True, key = lambda x: x[1])[1:6] # fetch the top 5 movies which are most similar to the selected movie and sort them in descending order

    recommended_movies = []
    
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)          # append the title of the movies_list

    return recommended_movies




movies_dict = pickle.load(open('movie_dict.pkl','rb'))      # load the movies dictionary in read binary mode
movies = pd.DataFrame(movies_dict)                          # converting the dictionary to a data frame
similarity = pickle.load(open('similarity.pkl','rb'))       # load the similarity matrix of all the movies


#---------for the title----------
st.title('Movie Recommender')
st.header('Get top similar movies of your choice...')


#----------for the movie selector drop down option----------------
movie = st.selectbox('please select a movie', movies['title'].values)


#----------for the button----------------
# when the button is clicked, recommend() is called and the selected movie name from the drop down is passed
if st.button('Recommend'):
    recommendations = recommend(movie)      # recommendations is a list containing all the recommended movies
    for i in recommendations:
        st.write(i)