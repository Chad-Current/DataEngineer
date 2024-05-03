import requests
import json
# import numpy as np
import pandas as pd
from datetime import datetime

base_url = "https://api.themoviedb.org/3/"
authenticationurl = "authentication"
popularmovies = "/movie/popular?language=en-US&page="
topRated = "movie/top_rated?language=en-US&page="
upcoming = "movie/upcoming?language=en-US&page="
actorquery = "search/person?query=duchovny&include_adult=false&language=en-US&page="
# discover = "discover/movie?include_adult=false&include_video=true&language=en-US&page=1&sort_by=popularity.desc&with_cast=Ryan-Reynolds"
#discover has no return items due to be currently blank or over daily limit

headers = {
    "accept": "application/json",
    "Authorization": 
}

class BaseAPI:
    def __init__(self, base_url=base_url, headers=headers):
         self.base_url = base_url
         self.headers = headers
    def make_request(self,endpoint,page):
        response = requests.get(f"{self.base_url}{endpoint}{page}",headers=self.headers)
        response.raise_for_status()
        return response.json()
    
class PopularAPI(BaseAPI):
    def __init__(self):
        super().__init__(base_url)

def Main():
    b = BaseAPI()
    p = PopularAPI()
    a = p.make_request(popularmovies,1)
    print(a)

if __name__ == "__main__":
    Main()

