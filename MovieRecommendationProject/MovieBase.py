import requests

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJlY2IyMzNjNmU2ZmVhN2U5YWM3OWJlMTg0YWJiNTdiYyIsInN1YiI6IjY2MmE4ZTVhOTljOTY0MDExYjM5YzA1MyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.-1fy7KBQp5ijVqI-0WVQANLeAAZZQqlAkvSaxvhIyws"
}
base_url = "https://api.themoviedb.org/3/"
authenticationurl = "authentication"

    
class ActorAPI():
    def __init__(self,page=1,segmentOne="",segmentTwo=None,base_url=base_url,headers=headers) -> None:
        self.page = page
        self.segmentOne = segmentOne
        self.segmentTwo = segmentTwo
        self.base_url = base_url
        self.headers = headers
        _spacer = '%20'
        if self.segmentTwo == None:
            self.endpoint = f'search/person?query={self.segmentOne}&include_adult=false&language=en-US&page='
        else:
            self.endpoint = f'search/person?query={self.segmentOne}{_spacer}{self.segmentTwo}&include_adult=false&language=en-US&page='
    def make_request(self,page=1):
        self.response = requests.get(f"{self.base_url}{self.endpoint}{page}",headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()

class MovieCredits():
    def __init__(self, actorid=1,base_url=base_url,headers=headers):
        self.actorid = actorid
        self.base_url = base_url
        self.headers = headers
        self.endpoint = f'/person/{self.actorid}/movie_credits'
    def make_request(self):
        self.response = requests.get(f"{self.base_url}{self.endpoint}",headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()

class ReccomendationAPI():
    def __init__(self,movieID,base_url=base_url, headers=headers):
        self.base_url = base_url
        self.headers = headers
        self.movieId = movieID
        self.endpoint = f'movie/{self.movieId}/recommendations?language=en-US&page='
    def make_request(self,page=1):
        self.response = requests.get(f"{self.base_url}{self.endpoint}{page}",headers=self.headers)
        self.response.raise_for_status()
        return self.response.json()


class Genres():
    def __init__(self) -> None:
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
            
    
if __name__=="__main__":
    print('Running testing.py')

