import requests, random

API_TOKEN = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTZjMDM3ZDhkOWJjZDFjYWFmMDRjNWRhNTE0NTBiNiIsInN1YiI6IjVmNTQxMTQ0NjY1NDA4MDAzMTA5YTdiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.N3v5u-yLnBRrsVY6Q7sMVtYmcKBO07IfoHN6RLKEZdE"

def get_movies(how_many, list_type):
    if list_type != 'popular' and  list_type != 'top_rated' and  list_type != 'now_playing' and  list_type != 'upcoming' :
       list_type == 'popular'
    endpoint = f"https://api.themoviedb.org/3/movie/{list_type}"
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    response.raise_for_status()
    data = response.json()
    data = data['results'][:how_many]
    return data


def get_poster_url(path,size):
    domain = "https://image.tmdb.org/t/p/"
    return f'{domain}{size}/{path}'

def get_single_movie(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_single_movie_cast(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/credits"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()["cast"]

def get_movie_images(movie_id):
    endpoint = f"https://api.themoviedb.org/3/movie/{movie_id}/images"
    
    headers = {
        "Authorization": f"Bearer {API_TOKEN}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_shuffle(how_many):
    data = get_movies()
    data_ran= random.sample(data['results'], how_many)
    return data_ran

