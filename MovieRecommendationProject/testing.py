import requests
import json
# import numpy as np
import pandas as pd
from datetime import datetime
headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlY2IyMzNjNmU2ZmVhN2U5YWM3OWJlMTg0YWJiNTdiYyIsInN1YiI6IjY2MmE4ZTVhOTljOTY0MDExYjM5YzA1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-1fy7KBQp5ijVqI-0WVQANLeAAZZQqlAkvSaxvhIyws"
}
base_url = "https://api.themoviedb.org/3/"
authenticationurl = "authentication"
# ACTOR = f"search/person?query={0}&include_adult=false&language=en-US&page=".format(input())

class BaseAPI:
    def __init__(self, base_url=base_url, headers=headers):
        self.base_url = base_url
        self.headers = headers
    def make_request(self,endpoint,page=1):
        self.response = requests.get(f"{self.base_url}{endpoint}{page}",headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()

class ReccomendationAPI(BaseAPI):
    def __init__(self, movieId, page=1, base_url=base_url, headers=headers):
        self.movieId = movieId
        self.page = page
        self.endpoint = f'movie/{self.movieId}/recommendations?language=en-US&page='
        print(self.endpoint)
        super().__init__(base_url, headers=headers)
        self.requested = self.make_request(endpoint=self.endpoint,page=self.page)



if __name__=="__main__":
    b = BaseAPI()
    print('Who\'s your actor or actress of choice? ')
    i = input()
    ACTOR = f"search/person?query={i}&include_adult=false&language=en-US&page=".format()
    c = b.make_request(endpoint=ACTOR)
    # print(c['results'][0]['known_for'][0]['id'])
    d = c['results'][0]['known_for'][0]['id']
    e = ReccomendationAPI(d)
    # print(e.requested)
    print(f'page on: ',e.requested['page'])
    print(f'total pages on: ',e.requested['total_pages'])
    while e.requested['page'] <= e.requested['total_pages']:
        for x in range(len(e.requested['results'])):
            print(f'{x}: ',e.requested['results'][x]['title'])
        nextpage =+ e.requested['page']+1
        print(f'next page ',nextpage)
        c = e.make_request(endpoint=ACTOR,page=nextpage)
        d = c['results'][0]['known_for'][0]['id']
        e = ReccomendationAPI(d,page=nextpage)
        # print(e.requested)
        print('Here are some other reccomended movies based on your actor of interest')
