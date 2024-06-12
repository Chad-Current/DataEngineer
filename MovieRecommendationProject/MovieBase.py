import requests
import json
# import numpy as np
import pandas as pd
from datetime import datetime


base_url = "https://api.themoviedb.org/3/"
authenticationurl = "authentication"

# popularmovies = "/movie/popular?language=en-US&page="
# topRated = "movie/top_rated?language=en-US&page="
# upcoming = "movie/upcoming?language=en-US&page="
# actorquery = "search/person?query=duchovny&include_adult=false&language=en-US&page="
# discover = "discover/movie?include_adult=false&include_video=true&language=en-US&page=1&sort_by=popularity.desc&with_cast=Ryan-Reynolds"
#discover has no return items due to be currently blank or over daily limit

headers = {
    "accept": "application/json",
    "Authorization": ""
}
class BaseAPI:
    def __init__(self, base_url=base_url, headers=headers):
        self.base_url = base_url
        self.headers = headers
    def make_request(self,endpoint,page=1):
        # print(f"{self.base_url}{endpoint}{page}")
        self.response = requests.get(f"{self.base_url}{endpoint}{page}",headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()
    
class PopularAPI(BaseAPI):
    def __init__(self,base_url=base_url,headers=headers):
        self.clicked = 1
        self.endpoint = "/movie/popular?language=en-US&page="
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(endpoint=self.endpoint,page=self.clicked)

class UpcomingAPI(BaseAPI):
    def __init__(self,base_url=base_url,headers=headers):
        self.clicked = 1
        self.endpoint = "movie/upcoming?language=en-US&page="
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(endpoint=self.endpoint,page=self.clicked)

class TopRatedAPI(BaseAPI):
    def __init__(self,base_url=base_url,headers=headers):
        self.clicked = 1
        self.endpoint = "movie/top_rated?language=en-US&page="
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(endpoint=self.endpoint,page=self.clicked)



class CreateAPI(PopularAPI,TopRatedAPI,UpcomingAPI):
    clicked = 0
    def __init__(self,tag):
        self.FetchAPI = {'p':PopularAPI(),
                    't':TopRatedAPI(), 'u':UpcomingAPI()}
        self.answer = [y for x,y in tag.items() if x == True]
        try:
            self.obj = self.FetchAPI[self.answer[0]].requested
            self.object = self.FetchAPI[self.answer[0]]
        except IndexError as i:
            print('Index Error, resolve issue when search button clicked with no catergory selected')
        super().__init__(base_url,headers=headers)
    def __str__(self) -> str:
        return super().__str__()
  

class Genres():
    def __init__(self, *createAPIobj) -> None:
        self.genre = {"Action":28,"Adventure":12,"Animation":16,"Comedy":35,"Crime":80,
                      "Documentary":99,"Drama":18,"Family":10751,"Fantasy":14,"History":36,
                      "Horror":27,"Music":10402,"Mystery":9648,"Romance":10749,
                      "Science Fiction":878,"Thriller":53,"Western":37}
        self.categoryDir = ""
    def choice(self,cat):
        for key, value in self.genre.items():
            if key in cat:
                self.categoryDir = value
                return self.categoryDir


if __name__ == "__main__":
    print("Running Movie Base.py")

