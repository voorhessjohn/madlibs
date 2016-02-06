import random
verbList = [] 
maxLengthVerbList = 2
while len(verbList) < maxLengthVerbList:
    item = input("Enter some verbs:")
    verbList.append(item)
print('Here\'s your list of verbs:')
print(verbList)
adjectiveList =[]
maxLengthAdjectiveList = 2
while len(adjectiveList) < maxLengthAdjectiveList:
    item = input("Enter some adjectives:")
    adjectiveList.append(item)
print('Here\'s your list of adjectives:')
print(adjectiveList)
animalList =[]
maxLengthAnimalList = 2
while len(animalList) < maxLengthAnimalList:
    item = input("Enter some types of animals:")
    animalList.append(item)
print('Here\'s your list of animals:')
print(animalList)
nounList =[]
maxLengthNounList = 2
while len(nounList) < maxLengthNounList:
    item = input("Enter some nouns:")
    nounList.append(item)
print('Here\'s your list of nouns:')
print(nounList)
holidayList =[]
maxLengthHolidayList = 2
while len(holidayList) < maxLengthHolidayList:
    item = input("Enter some holidays:")
    holidayList.append(item)
print('Here\'s your list of holidays:')
print(holidayList)
locationList = [] 
maxLengthLocationList = 2
while len(locationList) < maxLengthLocationList:
    item = input("Enter some locations:")
    locationList.append(item)
print('Here\'s your list of locations:')
print(locationList)
bodypartList = [] 
maxLengthBodypartList = 2
while len(bodypartList) < maxLengthBodypartList:
    item = input("Enter some names of body parts:")
    bodypartList.append(item)
print('Here\'s your list of body parts:')
print(bodypartList)
adverbList = [] 
maxLengthAdverbList = 2
while len(adverbList) < maxLengthAdverbList:
    item = input("Enter some adverbs:")
    adverbList.append(item)
print('Here\'s your list of adverbs:')
print(adverbList)
print('I want to ' + random.choice(verbList) + ' you like a ' + random.choice(adjectiveList) + ' ' + random.choice(animalList))
print('None of the ' + random.choice(adjectiveList) + ' ' + random.choice(animalList) + ' that I\'ve encountered in my ' + random.choice(adjectiveList) + ' life could ever hope to match the ' + random.choice(nounList) + ' of one ' + random.choice(adjectiveList) +' lady. Well, maybe ' + random.choice(adjectiveList) +
      'isn\'t quite the right word. ' + random.choice(adjectiveList) + '. That lady was' + random.choice(adjectiveList) + '. I remember how during Canadian' + random.choice(holidayList) + ', the ' + random.choice(adjectiveList) + 'of occasions, that ' + random.choice(adjectiveList) + 'lady taught me how to ' + random.choice(verbList) +
      'while ' + random.choice(verbList) + 'ing without making it seem too ' + random.choice(adjectiveList) + '. Not ' + random.choice(adverbList) + ', of course, but ' + random.choice(adverbList) + 'nonetheless. There was a contest being held at ' + random.choice(locationList) + 'for all the ' + random.choice(nounList) +
      'the children had found in' + random.choice(locationList) + 'since Tuesday. All I needed to do was ' + random.choice(verbList) + ' .' + random.choice(verbList) + ' like my' + random.choice(nounList) + ' was on the line, because it was. My' + random.choice(bodypartList) + ' felt like' + random.choice(nounList) +
      's and my' + random.choice(bodypartList) + ' itched' + random.choice(adverbList) + ' . But then I saw that very ' + random.choice(adjectiveList) + ', not quite' + random.choice(adjectiveList) + ' lady' + random.choice(verbList) + ', and I felt' + random.choice(adjectiveList) + '. The ' + random.choice(adjectiveList) +
      'folk of that ' + random.choice(adjectiveList) + ' ' + random.choice(nounList) + 'will forevermore tell tales of the ' + random.choice(verbList) + 'ing that can appear when a ' + random.choice(adjectiveList) + 'lady will ' + random.choice(verbList) + 'and someone like me will, in response, commence to ' + random.choice(verbList) + 'for the ages.')
