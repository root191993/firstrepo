
animals = ['cat', 'dog', 'rabbit', 'hamster', 'parrot']
animals.extend(['turtle', 'fish'])
print(animals)

more_animals = ['lion', 'tiger', 'bear']
animals.extend(more_animals)
print(animals)
animals.insert(2, 'elephant')
print(animals)
animals.remove('hamster')
print(animals)
some_animals = animals[1:4]
print('some_animals:  {}'.format(some_animals))

First_Two_Animals = animals[:2]
print('First_Two_Animals:  {}'.format(First_Two_Animals))   
Last_Two_Animals = animals[-2:]
print('Last_Two_Animals:  {}'.format(Last_Two_Animals))
