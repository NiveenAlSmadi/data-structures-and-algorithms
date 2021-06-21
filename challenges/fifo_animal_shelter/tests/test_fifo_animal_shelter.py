
from fifo_animal_shelter import __version__
from fifo_animal_shelter.fifo_animal_shelter import AnimalShelter,Cat,Dog

def test_version():
    assert __version__ == '0.1.0' 

def test_enqueue_cat():
    soker = Cat('soker')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(soker)
    actual = animal_shelter.frontcat.name
    expected = 'soker'
    assert actual == expected


def test_dequeue_cat():
    soker = Cat('soker')
    loz = Cat('loz')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(soker)
    animal_shelter.enqueue(loz)
    animal_shelter.dequeue('cat')
    actual = animal_shelter.frontcat.name
    expected = 'loz'
    assert actual == expected

def test_enqueue_dog():
    bull = Dog('bull')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(bull)
    actual = animal_shelter.frontdog.name
    expected = 'bull'
    assert actual == expected

def test_dequeue_dog():
    rock = Dog('rock')
    rox = Dog('rox')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(rox)
    animal_shelter.enqueue(rock)
    animal_shelter.dequeue('dog')
    actual = animal_shelter.frontdog.name
    expected = 'rock'
    assert actual == expected




def test_enqueue_dog_and_cat():
    soker = Cat('soker')
    bull = Dog('bull')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(bull)
    animal_shelter.enqueue(soker)
    actual1 = animal_shelter.frontdog.name
    expected1 = 'bull'
    actual2 = animal_shelter.frontcat.name
    expected2 = 'soker'
    assert actual1 == expected1
    assert actual2 == expected2


def test_null_case():
    rock = Dog('rock')
    rox = Dog('rox')
    animal_shelter = AnimalShelter()
    animal_shelter.enqueue(rox)
    animal_shelter.enqueue(rock)
    animal_shelter.dequeue('dog')
    animal_shelter.dequeue('dog')
    actual = animal_shelter.dequeue('dog')
    expected = 'null'
    assert actual == expected    


