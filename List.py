"""animals = ["cat", "dog", "rabbit", "hamster", "parrot" ]

animals.append("turtle")
"""

Animals = ['Man', 'Bear', 'Pig']
print(Animals[0])
Animals[0] = 'Dog'
print(Animals[0])
Animals.append('Cat')
print(Animals[-1])
Animals.extend(['Cow', 'Sheep'])
print(Animals[-1])

for animal in Animals:
    print(animal.upper())



   
