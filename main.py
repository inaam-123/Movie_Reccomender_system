import pandas as pd
import streamlit as st
import pickle
import requests
def fetch_poster(movie_):
    response=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=2d2e1cf3752e730189fa0618b6cb25f0&language=en-US'.format(movie_))
    data=response.json()
    return 'https://image.tmdb.org/t/p/w500/'+data['poster_path']

def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movies_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommend_movie = []
    poster = []
    for i in movies_list:
        movie_ = movies.iloc[i[0]].id
        recommend_movie.append(movies.iloc[i[0]].title)
        poster.append(fetch_poster(movie_))
    return recommend_movie,poster
movies_list = pickle.load(open('movies.pkl','rb'))
similarity = pickle.load(open('similarity.pkl','rb'))

movies = pd.DataFrame(movies_list)
st.title('Movie Recommender System')
selected_movie=st.selectbox(
    'List of movies',
    movies['title'].values
)

if st.button('Recommend'):
    name,posters=recommend(selected_movie)
    col1,col2,col3,col4,col5 = st.columns(5)
    with col1:
       st.text(name[0])
       st.image(posters[0])

    with col2:
       st.text(name[1])
       st.image(posters[1])

    with col3:
       st.text(name[2])
       st.image(posters[2])

    with col4:
       st.text(name[3])
       st.image(posters[3])

    with col5:
       st.text(name[4])
       st.image(posters[4])