import pytest
from func1 import gram_to_ounce, fahrenheit_centigrade, get_chicken_and_rabbit_count, is_prime, filter_primes, get_permutations, reverse_words, has_33, spy_game, circle_volume, unique_list, is_palindrome, histogram, guess_number_validate

def test_gram_to_ounce():
    assert gram_to_ounce(1) == 28.3495231

def test_invalid_gram_to_ounce():
    with pytest.raises(TypeError):
        gram_to_ounce("1")

def test_fahrenheit_centigrade():
    assert fahrenheit_centigrade(32) == 0
    assert fahrenheit_centigrade(212) == 100
    assert fahrenheit_centigrade(0) != 32

def test_invalid_fahrenheit_centigrade():
    with pytest.raises(TypeError):
        fahrenheit_centigrade("32")

def test_get_chicken_and_rabbit_count():
    assert get_chicken_and_rabbit_count(35, 94) == (23, 12)

def test_invalid_get_chicken_and_rabbit_count():
    with pytest.raises(TypeError):
        get_chicken_and_rabbit_count("35", "94")

def test_is_prime():
    assert is_prime(2) == True
    assert is_prime(101) == True

def test_invalid_is_prime():
    with pytest.raises(TypeError):
        is_prime("2")

def test_filter_primes():
    assert filter_primes([2, 5, 10, 20]) == [2, 5]

def test_get_permutations():
    assert set(get_permutations("ab")) == set(["ab", "ba"])
    assert set(get_permutations("abc") ) == set(["abc", "acb", "bac", "bca", "cab", "cba"])

def test_invalid_get_permutations():
    with pytest.raises(TypeError):
        get_permutations(1)

def test_reverse_words():
    assert reverse_words("We are ready") == "ready are We"

def test_invalid_reverse_words():
    with pytest.raises(TypeError):
        reverse_words(1)

def test_has_33():
    assert has_33([1, 2, 3, 3, 3]) == True

def test_invalid_has_33():
    with pytest.raises(TypeError):
        has_33(1)

def test_spy_game():
    assert spy_game([1, 0, 0, 7]) == True
    assert spy_game([0, 1, 0, 7]) == True
    assert spy_game([0, 1, 7]) == False

def test_invalid_spy_game():
    with pytest.raises(TypeError):
        spy_game(1)

def test_circle_volume():
    assert circle_volume(1) == 12.56
    assert circle_volume(2) == 50.24

def test_invalid_circle_volume():
    with pytest.raises(TypeError):
        circle_volume("1")

def test_unique_list():
    assert unique_list([1, 2, 3, 3, 3]) == [1, 2, 3]

def test_invalid_unique_list():
    with pytest.raises(TypeError):
        unique_list(1)

def test_is_palindrome():
    assert is_palindrome("aba") == True
    assert is_palindrome("racecar") == True
    assert is_palindrome("abracadabra") == False

def test_invalid_is_palindrome():
    with pytest.raises(TypeError):
        is_palindrome(1)

def test_histogram():
    assert histogram([4, 9, 7]) == "****\n*********\n*******"

def test_invalid_histogram():
    with pytest.raises(TypeError):
        histogram(1)

def test_guess_number_validate():
    assert guess_number_validate(1, 1) == (True, None)
    assert guess_number_validate(1, 0) == (False, "Your guess is too low.")
    assert guess_number_validate(1, 2) == (False, "Your guess is too high.")

def test_invalid_guess_number_validate():
    with pytest.raises(TypeError):
        guess_number_validate(1, "1")
