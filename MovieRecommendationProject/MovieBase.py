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
# recommendations = "movie/4108/recommendations?language=en-US&page=1"

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

class ReccomendationAPI(BaseAPI):
    def __init__(self, movieId, base_url=base_url, headers=headers):
        self.movieId = movieId
        self.endpoint = f'movie/{self.movieId}/recommendations?language=en-US&page='
        print(self.endpoint)
        super().__init__(base_url, headers=headers)
        self.requested = self.make_request(endpoint=self.endpoint,page=1)

class ActorAPI(BaseAPI):
    def __init__(self,segmentOne="Statham",segmentTwo=None) -> None:
        self.segmentOne = segmentOne
        self.segmentTwo = segmentTwo
        _spacer = '%20'
        if self.segmentTwo == None:
            endpoint = f'search/person?query={self.segmentOne}&include_adult=false&language=en-US&page='
        else:
            endpoint = f'search/person?query={self.segmentOne}{_spacer}{self.segmentTwo}&include_adult=false&language=en-US&page='
        super().__init__(base_url,headers=headers)
        self.requested = self.make_request(endpoint=endpoint,page=1)

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
        self.genre = {'Action': 28, 'Adventure': 12, 'Animation': 16, 'Comedy': 35, 'Crime': 80, 'Documentary': 99, \
                      'Drama': 18, 'Family': 10751, 'Fantasy': 14, 'History': 36, 'Horror': 27, 'Music': 10402, \
                        'Mystery': 9648, 'Romance': 10749, 'Science Fiction': 878, 'TV Movie': 10770, 'Thriller': 53, \
                              'War': 10752, 'Western': 37}
        self.categoryDir = ""
    def choice(self,cat):
        for key, value in self.genre.items():
            if key in cat:
                self.categoryDir = value
                return self.categoryDir

class CategroyDF():
    def __init__(self,obj,cat:int) -> pd.DataFrame:
        self.df = pd.DataFrame()
        print(type(cat))
    # def frame(self,obj,cat):
        self.obj, self.cat, self.data, idx = obj, cat, [], []
        self.page = self.obj['page']
        for x in range(0,len(self.obj['results'])):
            if self.cat in self.obj['results'][x]['genre_ids']:
                self.data.append({'id':self.obj['results'][x]['id'],'title':self.obj['results'][x]['title'],\
                            'overview':self.obj['results'][x]['overview'],'rating':str(self.obj['results'][x]['vote_average']),\
                            'genre_ids':str(self.obj['results'][x]['genre_ids'])})
                idx.append(self.obj['results'][x]['id'])         
        if not idx == []:
            self.df = pd.DataFrame(self.data,index=idx)
            print(self.df.head(20))
        else:
            _blank = pd.DataFrame()
            print('Dataframe was not created')
            return None

class ActorDF():
    def __init__(self,obj,cat:int) -> pd.DataFrame:
        self.df = pd.DataFrame()
        self.obj, self.cat, self.data, idx = obj.requested, cat, [], []
        self.page = self.obj['page']
        for x in range(0,len(self.obj['results'][0]['known_for'])):
            if self.cat in self.obj['results'][0]['known_for'][x]['genre_ids']:
                self.data.append({'id':self.obj['results'][0]['known_for'][x]['id'],'title':self.obj['results'][0]['known_for'][x]['title'],\
                            'rating':str(self.obj['results'][0]['known_for'][x]['vote_average']),\
                            'genre_ids':str(self.obj['results'][0]['known_for'][x]['genre_ids'])})
    
                idx.append(self.obj['results'][0]['known_for'][x]['id'])      
        if not idx == []:
            self.df = pd.DataFrame(self.data,index=idx)
            print(self.df.head(20))
        else:
            return None

class MergeDF():
    def __init__(self,df1,df2) -> pd.DataFrame:
        self.df1 = df1
        self.df2 = df2
        try:
            self.df3 = pd.concat([self.df1,self.df2],ignore_index=True)
            print(self.df3)
        except KeyError:
            print('A Merge Error has occured')



if __name__ == "__main__":
    print("Running Movie Base.py")
    R = ReccomendationAPI(movieId=1408)
    # print(R.requested['results'])
    d = CategroyDF(R.requested,18)

