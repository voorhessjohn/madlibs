verbList = [] 
maxLengthVerbList = 6
while len(verbList) < maxLengthVerbList:
    item = input("Enter some verbs:")
    verbList.append(item)
print('Here\'s your list of verbs:')
print(verbList)
adjectiveList =[]
maxLengthAdjectiveList = 6
while len(adjectiveList) < maxLengthAdjectiveList:
    item = input("Enter some adjectives:")
    adjectiveList.append(item)
print('Here\'s your list of adjectives:')
print(adjectiveList)
animalList =[]
maxLengthAnimalList = 6
while len(animalList) < maxLengthAnimalList:
    item = input("Enter some types of animals:")
    animalList.append(item)
print('Here\'s your list of animals:')
print(animalList)
import random
print('I want to ' + random.choice(verbList) + ' a ' + random.choice(adjectiveList) + ' ' + random.choice(animalList))
