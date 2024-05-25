from bs4 import BeautifulSoup
import requests
import re

# Construct the base URL
base_url = 'https://whatismymovie.com/results?text='

# Prompt the user to enter the name of an actor
actor_name = input("Enter the name of an actor: ")

# Replace spaces with "+" in the actor's name
actor_name = actor_name.replace(" ", "+")

# Construct the complete URL with the actor's name
url = base_url + actor_name

# Fetch the HTML content of the page
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Select all <h3> elements with the class "panel-title"
h3_elements = soup.find_all('h3', class_='panel-title')

movies_dict = {}

# Extract the text of each <h3> element and corresponding release time
for h3 in h3_elements:
    movie_title = h3.text.strip()

    # Extract the release year from the text inside parentheses
    match = re.search(r'\((\d{4})\)', movie_title)
    if match:
        release_year = match.group(1)
        # Remove the release year from the movie title
        movie_title = re.sub(r'\(\d{4}\)', '', movie_title).strip()

        # Store movie title and release year in the dictionary
        movies_dict[movie_title] = f"({release_year})"

# Sort the dictionary by release year in descending order
sorted_movies = sorted(movies_dict.items(), key=lambda x: x[1], reverse=True)

# Print the movie titles in descending order of release year
for movie, year in sorted_movies:
    print(f"{movie} {year}")
