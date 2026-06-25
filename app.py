import streamlit as st
import pickle
import pandas as pd
import requests


# PAGE CONFIG


st.set_page_config(
    page_title="Netflix Recommender",
    page_icon="🎬",
    layout="wide"
)

# NETFLIX THEME

st.markdown("""
<style>

.stApp{
    background-color:#141414;
}

h1,h2,h3,h4,h5,h6,p,label{
    color:white;
}

[data-testid="stSidebar"]{
    background-color:#000000;
}

.stButton > button{
    background-color:#E50914;
    color:white;
    border:none;
    border-radius:8px;
    font-weight:bold;
    width:100%;
    height:50px;
}

.stButton > button:hover{
    background-color:#B20710;
    color:white;
}

.netflix-card{
    background-color:#1F1F1F;
    padding:15px;
    border-radius:10px;
    margin-bottom:15px;
}

</style>
""", unsafe_allow_html=True)

# TMDB API KEY

API_KEY = "27d8d215b4dcdbcd8556355ced6c3b8c"

# LOAD FILES

movies = pickle.load(
    open("Models/movies.pkl", "rb")
)

nn_model = pickle.load(
    open("Models/nn_model.pkl", "rb")
)

tfidf = pickle.load(
    open("Models/tfidf.pkl", "rb")
)

links = pd.read_csv("data/link.csv")

# FEATURE MATRIX

genre_matrix = tfidf.transform(
    movies['genres']
)

# SESSION STATE

if "history" not in st.session_state:
    st.session_state.history = []

# POSTER FUNCTION

def fetch_poster(movie_id):

    try:

        tmdb_id = links[
            links['movieId'] == movie_id
        ]['tmdbId'].values[0]

        url = (
            f"https://api.themoviedb.org/3/movie/"
            f"{int(tmdb_id)}?api_key={API_KEY}"
        )

        data = requests.get(url).json()

        poster_path = data.get("poster_path")

        if poster_path:

            return (
                "https://image.tmdb.org/t/p/w500"
                + poster_path
            )

    except:
        pass

    return None

# RECOMMENDATION FUNCTION

def recommend(movie_name):

    movie_index = movies[
        movies['title'] == movie_name
    ].index[0]

    distances, indices = nn_model.kneighbors(
        genre_matrix[movie_index]
    )

    recommendations = []

    for distance, idx in zip(
        distances.flatten()[1:],
        indices.flatten()[1:]
    ):

        similarity_score = round(
            (1 - distance) * 100,
            1
        )

        recommendations.append(
            (
                movies.iloc[idx]['title'],
                similarity_score
            )
        )

    return recommendations

# SIDEBAR

st.sidebar.markdown(
    "<h2 style='color:#E50914;'>🕒 Recently Viewed</h2>",
    unsafe_allow_html=True
)

if len(st.session_state.history) == 0:
    st.sidebar.write("No movies viewed yet.")

for movie in reversed(
    st.session_state.history[-5:]
):
    st.sidebar.write(movie)

# TITLE

st.markdown("""
<h1 style='text-align:center;color:#E50914;'>
NETFLIX RECOMMENDER
</h1>
""", unsafe_allow_html=True)

# HERO BANNER

st.markdown("""
<div style="
background:linear-gradient(to right,#000000,#E50914);
padding:20px;
border-radius:10px;
margin-bottom:20px;
">
<h2 style="color:white;">
🍿 Discover Movies You'll Love
</h2>
<p style="color:white;">
Powered by Machine Learning Recommendation Engine
</p>
</div>
""", unsafe_allow_html=True)

# MOVIE SELECTOR

movie_options = [
    "Select a movie..."
] + movies['title'].tolist()

selected_movie = st.selectbox(
    "🎬 Choose a Movie",
    movie_options
)

if selected_movie == "Select a movie...":
    selected_movie = None

# SHOW MOVIE DETAILS

if selected_movie:

    movie_row = movies[
        movies['title'] == selected_movie
    ].iloc[0]

    st.markdown(
    f"""
    <h2 style="
    color:#F5F5F5;
    font-weight:700;
    ">
    {movie_row['title']}
    </h2>
    """,
    unsafe_allow_html=True
)

    movie_id = movie_row['movieId']

    poster = fetch_poster(
        movie_id
    )

    if poster:

        st.image(
            poster,
            width=300
        )

    st.markdown(
    f"""
    🎭 <b>Genres:</b> {movie_row['genres']}
    """,
    unsafe_allow_html=True
)

# RECOMMEND BUTTON

if st.button(" Recommend Movies"):

    if not selected_movie:

        st.warning(
            "Please select a movie first."
        )

        st.stop()

    if selected_movie not in st.session_state.history:

        st.session_state.history.append(
            selected_movie
        )

    recommendations = recommend(
        selected_movie
    )

    st.markdown(
    """
    <h2 style="
    color:#F5F5F5;
    margin-top:20px;
    ">
    Recommended For You
    </h2>
    """,
    unsafe_allow_html=True
)

    for movie, score in recommendations:

        movie_id = movies[
            movies['title'] == movie
        ]['movieId'].values[0]

        poster = fetch_poster(
            movie_id
        )

        col1, col2 = st.columns(
            [1, 3]
        )

        with col1:

            if poster:

                st.image(
                    poster,
                    width=120
                )

        with col2:

            st.markdown(
                f"""
                <div class="netflix-card">
                    <h3 style="color:white;">
                        {movie}
                    </h3>
                    
                </div>
                """,
                unsafe_allow_html=True
            )