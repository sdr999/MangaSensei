# MangaSensei
Unveiling the World of Manga through Customized Recommendations

The project focuses on extracting manga information from the website Mangakakalot.com to create a comprehensive dataset for manga reviews and recommendations.
<br><br>
Using web scraping techniques, the project collects data from the website's "Latest Manga" section, which provides a wealth of manga titles, genres, and descriptions. By programmatically navigating the website and parsing its HTML structure, the project retrieves the desired information using Python's requests and BeautifulSoup libraries.
<br><br>
The web scraping code extracts manga titles, genres, and descriptions from each manga's respective webpage. It carefully identifies the relevant HTML elements and retrieves the textual data, ensuring accuracy and completeness. The scraped information is then stored in a structured format, such as a pandas DataFrame, allowing for easy analysis and manipulation.
<br><br>
Once the data extraction and processing are complete, the project generates a dataset containing the manga titles, genres, and descriptions. This dataset serves as a valuable resource for analyzing manga trends, conducting sentiment analysis, and building recommendation systems based on genre or content similarities.
<br><br>
The project aims to provide personalized manga recommendations based on user input. It utilizes the concept of cosine similarity to determine the similarity between manga titles using their descriptions.
<br><br>
The project begins by loading a dataset containing manga titles, descriptions, and other relevant information. It then preprocesses the manga descriptions by applying TF-IDF vectorization, which assigns importance weights to the words based on their frequency across the entire corpus. This vectorization process helps capture the essence of each manga's description.
<br><br>
Once the dataset is prepared, the recommendation system prompts the user to enter the title of a manga they enjoy. Using the entered title, the system calculates the cosine similarities between the input manga and the other manga in the dataset. The manga titles with the highest cosine similarity scores are then selected as recommendations.
<br><br>
The recommendations are presented to the user, displaying the titles and descriptions of the top five most similar manga. This assists users in discovering new manga titles that align with their interests and preferences.
<br><br>
The project incorporates libraries such as pandas for data handling, scikit-learn for TF-IDF vectorization, and cosine similarity calculations. Additionally, it provides a simple and interactive command-line interface for users to input their preferences and receive relevant recommendations.
<br><br>
By automating the data collection process through web scraping, the project eliminates the need for manual data entry, saving time and effort while ensuring data accuracy and consistency. It enables enthusiasts, researchers, and developers to access a ready-to-use dataset for various manga-related analyses, reviews, and recommendation systems.
<br><br>
It is important to note that web scraping should be done responsibly and in compliance with the target website's terms of service. Additionally, the generated dataset provides a snapshot of the manga information available on Mangakakalot.com at the time of scraping and may need periodic updates to capture new manga releases and changes on the website.
<br><br>
Overall, this project offers a valuable resource for manga enthusiasts, researchers, and developers to explore, analyze, and create innovative solutions within the vibrant world of manga.
