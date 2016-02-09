import random
main = {}
parts = ['verbs',
       'adjectives',
       'animals',
       'nouns',
       'holidays',
       'locations',
       'body parts',
       'adverbs',]

maxLength = 2
for i in range(len(parts)):
   item = []
   for j in range(maxLength):  
       item.append(input('Type some ' + str(parts[i]) + ':'))
       print('Here\'s your list of ' + str(parts[i]) + ':')
       print(item)
   main[i] = item


i + 1
print(main)

#print('I want to ' + random.choice(verbList) + ' you like a ' + random.choice(adjectiveList) + ' ' + random.choice(animalList))
#print('None of the ' + random.choice(adjectiveList) + ' ' + random.choice(animalList) + ' that I\'ve encountered in my ' + random.choice(adjectiveList) + ' life could ever hope to match the ' + random.choice(nounList) + ' of one ' + random.choice(adjectiveList) +' lady. Well, maybe ' + random.choice(adjectiveList) +
#      'isn\'t quite the right word. ' + random.choice(adjectiveList) + '. That lady was' + random.choice(adjectiveList) + '. I remember how during Canadian' + random.choice(holidayList) + ', the ' + random.choice(adjectiveList) + 'of occasions, that ' + random.choice(adjectiveList) + 'lady taught me how to ' + random.choice(verbList) +
#      'while ' + random.choice(verbList) + 'ing without making it seem too ' + random.choice(adjectiveList) + '. Not ' + random.choice(adverbList) + ', of course, but ' + random.choice(adverbList) + 'nonetheless. There was a contest being held at ' + random.choice(locationList) + 'for all the ' + random.choice(nounList) +
#      'the children had found in' + random.choice(locationList) + 'since Tuesday. All I needed to do was ' + random.choice(verbList) + ' .' + random.choice(verbList) + ' like my' + random.choice(nounList) + ' was on the line, because it was. My' + random.choice(bodypartList) + ' felt like' + random.choice(nounList) +
#      's and my' + random.choice(bodypartList) + ' itched' + random.choice(adverbList) + ' . But then I saw that very ' + random.choice(adjectiveList) + ', not quite' + random.choice(adjectiveList) + ' lady' + random.choice(verbList) + ', and I felt' + random.choice(adjectiveList) + '. The ' + random.choice(adjectiveList) +
#      'folk of that ' + random.choice(adjectiveList) + ' ' + random.choice(nounList) + 'will forevermore tell tales of the ' + random.choice(verbList) + 'ing that can appear when a ' + random.choice(adjectiveList) + 'lady will ' + random.choice(verbList) + 'and someone like me will, in response, commence to ' + random.choice(verbList) + 'for the ages.')

#I have hashed out the code above until I change the references from the original lists to the new mutiple-key dictionary.
