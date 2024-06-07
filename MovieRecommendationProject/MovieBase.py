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
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlY2IyMzNjNmU2ZmVhN2U5YWM3OWJlMTg0YWJiNTdiYyIsInN1YiI6IjY2MmE4ZTVhOTljOTY0MDExYjM5YzA1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-1fy7KBQp5ijVqI-0WVQANLeAAZZQqlAkvSaxvhIyws"
}

class BaseAPI:
    def __init__(self, base_url=base_url, headers=headers):
        self.base_url = base_url
        self.headers = headers
    def make_request(self,endpoint,page):
        self.response = requests.get(f"{self.base_url}{endpoint}{page}",headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()

class PopularAPI(BaseAPI):
    def __init__(self,base_url=base_url,headers=headers):
        self.endpoint = "/movie/popular?language=en-US&page="
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(self.endpoint,page=1)

class UpcomingAPI(BaseAPI):
    def __init__(self,base_url=base_url,headers=headers):
        self.endpoint = "movie/upcoming?language=en-US&page="
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(self.endpoint,page=1)

class TopRatedAPI(BaseAPI):
    def __init__(self,base_url=base_url,headers=headers):
        self.endpoint = "movie/top_rated?language=en-US&page="
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(self.endpoint,page=1)

class ActorQueryAPI(BaseAPI):
    def __init__(self,base_url=base_url,headers=headers):
        self.endpoint = "search/person?query=duchovny&include_adult=false&language=en-US&page="
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(self.endpoint,page=1)


class Genres(PopularAPI,UpcomingAPI,TopRatedAPI,ActorQueryAPI):
    def __init__(self, *createAPIobj) -> None:
        self.genre = {"Action":28,"Adventure":12,"Animation":16,"Comedy":35,"Crime":80,
                      "Documentary":99,"Drama":18,"Family":10751,"Fantasy":14,"History":36,
                      "Horror":27,"Music":10402,"Mystery":9648,"Romance":10749,
                      "Science Fiction":878,"Thriller":53,"Western":37}
        self.categoryDir = ""
        # self.pop, self.upcoming, self.toprated, self.actorquery = ('p','u','t','a')
        super().__init__()
        self.FetchAPI = {'a':ActorQueryAPI(), 'p':PopularAPI(),
                    't':TopRatedAPI(), 'u':UpcomingAPI()}
        # api = self.pop
        # key = self.FetchAPI[api]
        # print('key ', key.endpoint)
#Start here with returning choices matching genre ids
    def choice(self,cat,tag):
        answer = [x for x,y in tag.items() if y == True]
        self.retrieveAPI = self.FetchAPI[answer[0]]
        print(self.retrieveAPI)
        # print(answer)
        # print(type(answer))
        for key, value in self.genre.items():
            # print(key,value)
            # print(self.categoryDir)
            # print('printing args',args)
            if key in cat:
                self.categoryDir = value
                print(self.categoryDir)
                return self.categoryDir
    # def foundGenre(self):
    #     self.pop.requested.get('total_results',{})
    #     for i in range(1,11):
    #         self.categoryDir = self.pop.requested.get('results',{})[i]['genre_ids']
    #         print(self.categoryDir)
#End returning choices





if __name__ == "__main__":
    print("Running Movie Base.py")

