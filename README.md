# 🎬 Netflix Hybrid Recommender System

A Machine Learning-based Movie Recommendation System developed as an extension of a research-oriented project from the **Design and Analysis of Algorithms (DAA)** course. The original project focused on studying recommendation algorithms and similarity search techniques from a theoretical perspective. This implementation transforms those concepts into a practical and interactive web application using Machine Learning and Streamlit.

---

##  Project Overview

Recommendation systems play a major role in modern streaming platforms such as Netflix, Amazon Prime, and Disney+ by helping users discover relevant content.

This project implements a movie recommendation engine using **Content-Based Filtering** and explores the foundations of **Hybrid Recommendation Systems**. The system analyzes movie metadata, converts genres into numerical representations using TF-IDF Vectorization, and retrieves similar movies using the Nearest Neighbors algorithm.

The recommendation engine is integrated into a Streamlit web application featuring:

* Movie recommendations based on similarity
* Movie posters fetched using TMDB API
* Similarity match percentages
* Recently viewed movie history
* Netflix-inspired dark UI

---

##  Objectives

* Convert a research-based DAA project into a practical application
* Apply Machine Learning techniques to recommendation systems
* Understand similarity search and nearest-neighbor retrieval
* Build an interactive recommendation platform
* Demonstrate real-world applications of algorithm design concepts

---

##  Machine Learning Workflow

### Data Collection

The project uses the MovieLens dataset containing:

* Movies
* Ratings
* Tags
* Genome Tags
* Movie Links (TMDB IDs)

### Data Preprocessing

* Cleaned movie metadata
* Processed genre information
* Prepared features for recommendation generation

### Feature Engineering

Used **TF-IDF Vectorization** to convert movie genres into numerical vectors.

Example:

```text
Action|Adventure|Sci-Fi
```

↓

```text
Action Adventure Sci-Fi
```

### Similarity Search

Implemented **Nearest Neighbors** with cosine similarity to identify movies with similar characteristics.

### Recommendation Generation

When a user selects a movie:

1. Movie genres are converted into vectors.
2. Similar movies are retrieved using Nearest Neighbors.
3. Similarity scores are calculated.
4. Top recommendations are displayed.

---
## 🚀 Features

### 🎥 Movie Recommendations

Recommend movies based on content similarity.

### ⭐ Similarity Match Scores

Displays how closely recommended movies match the selected movie.

### 🖼 Movie Posters

Movie posters are fetched dynamically using the TMDB API.

### 🕒 Recently Viewed Movies

Tracks recently viewed movies using Streamlit Session State.

### 🎨 Netflix-Inspired Interface

* Dark theme
* Netflix red accents
* Poster previews
* Interactive recommendation cards

---

## 🛠 Technologies Used

* Python
* Pandas
* Scikit-Learn
* Streamlit
* Pickle
* Requests
* TMDB API

---

## 📂 Project Structure

```text
Netflix-Hybrid-Recommender-System/
│
├── app.py
├── README.md
│
├── Models/
│   ├── movies.pkl
│   ├── nn_model.pkl
│   ├── svd_model.pkl
│   └── tfidf.pkl
│
└── notebook/
    └── recommender.ipynb
```

---

##  Algorithms Used

### TF-IDF Vectorization

Transforms textual genre information into machine-readable numerical vectors.

### Nearest Neighbors

Finds the most similar movies based on feature similarity.



### SVD (Collaborative Filtering)

Explored collaborative filtering using Singular Value Decomposition (SVD) on user ratings data.

---

## 📥 Dataset

This repository does **not include the MovieLens dataset** due to GitHub storage limitations.

Download the dataset from Kaggle:

**MovieLens 25M Dataset**

https://www.kaggle.com/datasets/grouplens/movielens-25m-dataset

After downloading, place the files inside a folder named:

```text
data/
```

Example:

```text
data/
├── movie.csv
├── rating.csv
├── link.csv
├── tag.csv
├── genome_tags.csv
└── genome_scores.csv
```

---

## 💻 Running the Project

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

##  Academic Background

This project originated from a research-based course project in the **Design and Analysis of Algorithms (DAA)** course.

The original work focused on studying recommendation systems, similarity search, and retrieval algorithms. To bridge the gap between theory and real-world implementation, the concepts were extended into a fully functional Machine Learning application with an interactive user interface.

This project demonstrates how algorithmic concepts studied in academia can be transformed into practical software solutions.

---

##  Future Improvements

* Full Hybrid Recommendation System
* User-Based Collaborative Filtering
* Personalized User Profiles
* Search Autocomplete
* Recommendation Explanations
* User Rating Integration
* Cloud Deployment

---
