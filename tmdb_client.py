import requests, random

def get_popular_movies():
    endpoint = "https://api.themoviedb.org/3/movie/popular"
    api_token = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI5OTZjMDM3ZDhkOWJjZDFjYWFmMDRjNWRhNTE0NTBiNiIsInN1YiI6IjVmNTQxMTQ0NjY1NDA4MDAzMTA5YTdiZSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.N3v5u-yLnBRrsVY6Q7sMVtYmcKBO07IfoHN6RLKEZdE"
    headers = {
        "Authorization": f"Bearer {api_token}"
    }
    response = requests.get(endpoint, headers=headers)
    return response.json()

def get_poster_url(path,size):
    domain = "https://image.tmdb.org/t/p/"
    return f'{domain}{size}/{path}'

def get_movies(how_many):
    data = get_popular_movies()
    return data["results"][:how_many]

def get_shuffle(how_many):
    data = get_popular_movies()
    data_ran= random.sample(data['results'], how_many)
    return data_ran


