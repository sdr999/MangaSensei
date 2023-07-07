import streamlit as st
import requests
from PIL import Image
from io import BytesIO
from bs4 import BeautifulSoup
import pickle
import pandas as pd

manga_list = pickle.load(open('F:\material\movie-recommender\manga_list.pkl' , 'rb'))
similarity = pickle.load(open('F:\material\movie-recommender\similarity2.pkl' , 'rb'))

mangas = pd.DataFrame(manga_list)


def recommend(movie):
    manga_index = mangas[mangas['title'] == movie].index[0]
    distances = similarity[manga_index]
    manga_list = sorted(list(enumerate(distances)) , reverse = True , key = lambda x:x[1])[1:6]


    recom_mangas = []
    recom_posters = []

    for i in manga_list:
        manga_title = mangas.iloc[i[0]].title
        recom_mangas.append(mangas.iloc[i[0]].title)
        recom_posters.append(scrape_manga_poster(manga_title))
    return recom_mangas,recom_posters
# Display the image using Streamlit

def scrape_manga_poster(manga_title):
    # Fetch the image URL using web scraping

    dfd = pd.read_csv("manga_dataset (1).csv")

    index=dfd[dfd['title'] == manga_title]
    url=index['link']
    url = url.to_string()
    splitstr = url.split()
    lnk=splitstr[1]
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    response = requests.get(lnk, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")
    if "https://mangakakalot.com" in url:
        image_element = soup.find("div", class_="manga-info-pic").find("img")
        return image_element["src"]
    else:
        img = soup.find("span", class_="info-image").find("img")
        image_url = img["src"]
        return image_url

    # # Request the image from the URL
    # image_response = requests.get(image_url)
    # image = Image.open(BytesIO(image_response.content))



st.title('Manga Recommender System')


selected_manga_name = st.selectbox(

    'Which manga You want to Select?',
    mangas['title'].values
)


if st.button('Recommend'):

    recommended_manga_names , recommended_manga_posters = recommend(selected_manga_name)


    col1, col2, col3, col4, col5 = st.columns(5)
    with col1:
        st.text(recommended_manga_names[0])
        st.image(recommended_manga_posters[0])
    with col2:
        st.text(recommended_manga_names[1])
        st.image(recommended_manga_posters[1])

    with col3:
        st.text(recommended_manga_names[2])
        st.image(recommended_manga_posters[2])
    with col4:
        st.text(recommended_manga_names[3])
        st.image(recommended_manga_posters[3])
    with col5:
        st.text(recommended_manga_names[4])
        st.image(recommended_manga_posters[4])