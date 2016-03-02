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

v = main[0] #verbs
a = main[1] #adjectives
a2 = main[2] #animals
n = main[3] #nouns
h = main[4] #holidays
l = main[5] #locations
b = main[6] #body parts
a3 = main[7] #adverbs

print('I want to ' + random.choice(v) + ' you like a ' + random.choice(a) + ' ' + random.choice(a2))
print('None of the ' + random.choice(a) + ' ' + random.choice(a2) + ' that I\'ve encountered in my ' + random.choice(a) + ' life could ever hope to match the ' + random.choice(n) + ' of one ' + random.choice(a) +' lady. Well, maybe ' + random.choice(a) +
      'isn\'t quite the right word. ' + random.choice(a) + '. That lady was' + random.choice(a) + '. I remember how during Canadian' + random.choice(h) + ', the ' + random.choice(a) + 'of occasions, that ' + random.choice(a) + 'lady taught me how to ' + random.choice(v) +
      'while ' + random.choice(v) + 'ing without making it seem too ' + random.choice(a) + '. Not ' + random.choice(a3) + ', of course, but ' + random.choice(a3) + 'nonetheless. There was a contest being held at ' + random.choice(l) + 'for all the ' + random.choice(n) +
      'the children had found in' + random.choice(l) + 'since Tuesday. All I needed to do was ' + random.choice(v) + ' .' + random.choice(v) + ' like my' + random.choice(n) + ' was on the line, because it was. My' + random.choice(b) + ' felt like' + random.choice(n) +
     's and my' + random.choice(b) + ' itched' + random.choice(a3) + ' . But then I saw that very ' + random.choice(a) + ', not quite' + random.choice(a) + ' lady' + random.choice(v) + ', and I felt' + random.choice(a) + '. The ' + random.choice(a) +
      'folk of that ' + random.choice(a) + ' ' + random.choice(n) + 'will forevermore tell tales of the ' + random.choice(v) + 'ing that can appear when a ' + random.choice(a) + 'lady will ' + random.choice(v) + 'and someone like me will, in response, commence to ' + random.choice(v) + ' for the ages.')

#I have hashed out the code above until I change the references from the original lists to the new mutiple-key dictionary.
