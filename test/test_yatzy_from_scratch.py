# Importamos Yatzy
from src.yatzy import Yatzy

# Importamos PYTEST
import pytest




# Test Chance
@pytest.mark.test_chance
def test_chance():

    assert 15 == Yatzy.chance(1, 2, 3, 4, 5)
    assert 14 == Yatzy.chance(1, 1, 3, 3, 6)
    assert 21 == Yatzy.chance(4, 5, 5, 6, 1)




# Test Yatzy
@pytest.mark.test_yatzy
def test_yatzy():

    assert 50 == Yatzy.yatzy(1,1,1,1,1)
    assert 0 == Yatzy.yatzy(1,1,1,2,1)




# Test Ones
@pytest.mark.test_ones
def test_ones():
    
    assert 5 == Yatzy.ones(1,1,1,1,1)
    assert 0 == Yatzy.ones(6,5,2,3,4)


# Test Twos
@pytest.mark.test_twos
def test_twos():
    
    assert 10 == Yatzy.twos(2,2,2,2,2)
    assert 0 == Yatzy.twos(6,5,1,3,4)


# Test Threes
@pytest.mark.test_threes
def test_threes():
    
    assert 15 == Yatzy.threes(3,3,3,3,3)
    assert 0 == Yatzy.threes(6,5,1,2,4)


# Test Fours
@pytest.mark.test_fours
def test_fours():
    
    assert 20 == Yatzy.fours(4,4,4,4,4)
    assert 0 == Yatzy.fours(6,5,1,2,3)


# Test Fives
@pytest.mark.test_fives
def test_fives():
    
    assert 25 == Yatzy.fives(5,5,5,5,5)
    assert 0 == Yatzy.fives(6,4,1,2,3)


# Test Sixes
@pytest.mark.test_sixes
def test_sixes():
    
    assert 30 == Yatzy.sixes(6,6,6,6,6)
    assert 0 == Yatzy.sixes(5,4,1,2,3)




# Test Pair
@pytest.mark.test_score_pair
def test_score_pair():

    assert 8 == Yatzy.score_pair(3,3,3,4,4)
    assert 12 == Yatzy.score_pair(1,1,6,2,6)
    assert 6 == Yatzy.score_pair(3,3,3,4,1)
    assert 6 == Yatzy.score_pair(3,3,3,3,1)
    assert 0 == Yatzy.score_pair(1,6,2,5,4)




# Test Two Pair
@pytest.mark.test_two_pair
def test_two_pair():

    assert 8 == Yatzy.two_pair(1,1,2,3,3)
    assert 0 == Yatzy.two_pair(1,1,2,3,4)
    assert 6 == Yatzy.two_pair(1,1,2,2,2)




# Test Three of a kind
@pytest.mark.test_three_of_a_kind
def test_three_of_a_kind():

    assert 9 == Yatzy.three_of_a_kind(3,3,3,4,5)
    assert 0 == Yatzy.three_of_a_kind(3,3,4,5,6)
    assert 9 == Yatzy.three_of_a_kind(3,3,3,3,1)




# Test Four of a kind
@pytest.mark.test_four_of_a_kind
def test_four_of_a_kind():

    assert 8 == Yatzy.four_of_a_kind(2,2,2,2,5)
    assert 0 == Yatzy.four_of_a_kind(2,2,2,5,5)
    assert 8 == Yatzy.four_of_a_kind(2,2,2,2,2)




# Test Small straight
@pytest.mark.test_smallStraight
def test_smallStraight():

    assert 15 == Yatzy.smallStraight(1,2,3,4,5)
    assert 0 == Yatzy.smallStraight(1,2,3,4,4)




# Test Large straight
@pytest.mark.test_largeStraight
def test_largeStraight():

    assert 20 == Yatzy.largeStraight(2,3,4,5,6)
    assert 0 == Yatzy.largeStraight(2,3,4,5,5)




# Test Full House
@pytest.mark.test_fullHouse
def test_fullHouse():

    assert 8 == Yatzy.fullHouse(1,1,2,2,2)
    assert 0 == Yatzy.fullHouse(2,2,3,3,4)
    assert 0 == Yatzy.fullHouse(4,4,4,4,4)
