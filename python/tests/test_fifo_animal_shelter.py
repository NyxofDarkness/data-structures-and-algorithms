import pytest

from fifo_animal_shelter.fifo_animal_shelter import Node, AnimalShelter


#  animal added to shelter
def test_animal_added():
    dog = AnimalShelter()
    dog.enqueue("dog")
    actual = dog.first.value
    expected = "dog"
    assert actual == expected

def test_dequeue():
    x = AnimalShelter()
    x.enqueue("cat")
    actual = x.dequeue("cat")
    expected = "cat"
    assert actual == expected

def test_when_not_the_special():
    x = AnimalShelter()
    x.enqueue("cat")
    x.enqueue("dog")
    x.enqueue("cat")
    x.enqueue("cat")
    actual = x.dequeue("Tony")
    expected = "None"
    assert actual == expected
#  returns null if not dog or cat
# return oldest in shelter

