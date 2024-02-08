import pytest
from func2 import Movie, is_higher_5_5, filter_movies_by_imdb_higher_5_5, filter_movies_by_categories, average_movies_imdb, average_movies_imdb_by_categories

def test_is_higher_5_5():
    assert is_higher_5_5(10) == True
    assert is_higher_5_5(5.5) == False
    assert is_higher_5_5(5) == False

def test_invalid_is_higher_5_5():
    with pytest.raises(TypeError):
        is_higher_5_5("2")

def test_filter_movies_by_imdb_higher_5_5():
    movies = [Movie("Star Wars", 8.5, "Comedy"), Movie("Star Wars", 5, "Movie")]
    assert filter_movies_by_imdb_higher_5_5(movies) == [movies[0]]

# def test_invalid_filter_movies_by_imdb_higher_5_5():
#     with pytest.raises(TypeError):
#         filter_movies_by_imdb_higher_5_5(["2"])

def test_filter_movies_by_categories():
    movies = [Movie("Star Wars", 8.5, "Comedy"), Movie("Star Wars", 5.5, "Horor")]
    categories = ["Comedy"]
    assert filter_movies_by_categories(movies, categories) == [movies[0]]

# def test_invalid_filter_movies_by_categories():
#     with pytest.raises(TypeError):
#         filter_movies_by_categories("2")


def test_average_movies_imdb():
    movies = [Movie("Star Wars", 8.5, "Comedy"), Movie("Star Wars", 5.5, "Horor")]
    assert average_movies_imdb(movies) == 7

# def test_invalid_average_movies_imdb():
#     with pytest.raises(TypeError):
#         average_movies_imdb("2")

def test_average_movies_imdb_by_categories():
    movies = [Movie("Star Wars", 8.5, "Comedy"), Movie("Star Wars", 5.5, "Horor")]
    categories = ["Comedy"]
    assert average_movies_imdb_by_categories(movies, categories) == 8.5

# def test_invalid_average_movies_imdb_by_categories():
#     with pytest.raises(TypeError):
#         average_movies_imdb_by_categories("2")
