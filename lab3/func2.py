class Movie:
    def __init__(self, name: str, imdb: float, category: str):
        self.name = name
        self.imdb = imdb
        self.category = category
    def __eq__(self, other):
        if not isinstance(other, Movie):
            return False
        return self.name == other.name and self.imdb == other.imdb and self.category == other.category

# 1
def is_higher_5_5(imdb: float) -> bool:
    return imdb > 5.5

# 2
def filter_movies_by_imdb_higher_5_5(movies: [Movie]) -> [Movie]:
    return [movie for movie in movies if is_higher_5_5(movie.imdb)]

# 3
def filter_movies_by_categories(movies: [Movie], categories: [str]) -> [Movie]:
    return [movie for movie in movies if movie.category in categories]

# 4
def average_movies_imdb(movies: [Movie]) -> float:
    return sum(movie.imdb for movie in movies) / len(movies)

# 5
def average_movies_imdb_by_categories(movies: [Movie], categories: str) -> float:
    result = [movie.imdb for movie in movies if movie.category in categories]
    return sum(result) / len(result)

movies: [Movie] = [
{
"name": "Usual Suspects", 
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]