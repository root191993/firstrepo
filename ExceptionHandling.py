animals = ['cat', 'dog', 'rabbit', 'hamster', 'parrot']


cat_index = animals.index('dog')
print(cat_index)
Cat_index = animals.index('elephant')
print(Cat_index)

try:
    cat_index = animals.index('dog')
    print(cat_index)
    Cat_index = animals.index('elephant')
    print(Cat_index)
except ValueError:
    print("Elephant is not in the list of animals.")