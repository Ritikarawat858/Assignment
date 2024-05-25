 from bs4 import BeautifulSoup
import requests
import re

base_url = 'https://whatismymovie.com/results?text='
#user input
actor_name = input("Enter the name of an actor: ")

actor_name = actor_name.replace(" ", "+")

#complete url
url = base_url + actor_name

response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

h3_elements = soup.find_all('h3', class_='panel-title')

movies_dict = {}

for h3 in h3_elements:
    movie_title = h3.text.strip()

    match = re.search(r'\((\d{4})\)', movie_title)
    if match:
        release_year = match.group(1)
        movie_title = re.sub(r'\(\d{4}\)', '', movie_title).strip()

        movies_dict[movie_title] = f"({release_year})"

# Sort the dictionary in descending order
sorted_movies = sorted(movies_dict.items(), key=lambda x: x[1], reverse=True)

# Print the movie titles in descending order of release year
for movie, year in sorted_movies:
    print(f"{movie} {year}")
