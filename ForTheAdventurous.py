import re
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from collections import Counter



TextName = 'King-James-Bible'

# All the stemmers

# it may be best just to use one at a time. for this
# tutorial, i will use Porter Stemmer! It is the one
# jurafsky discussed in our last Coursera video!

porter = PorterStemmer()
	# further reading: http://tartarus.org/martin/PorterStemmer/

# lancaster = LancasterStemmer()
	# further reading: http://textminingonline.com/tag/lancaster-stemmer
	
# snowball = SnowballStemmer("english")
	# further reading: http://snowball.tartarus.org/texts/introduction.html

# the lemmatizer
lemmatiser = WordNetLemmatizer()

def Normalize(word):
	## NOTE: the lemmatizers and stemmers have serious
	## performance tradeoffs. keep that in mind
	
	# lemmatize
	newWord = lemmatiser.lemmatize(word)

	# stem
	newWord = porter.stem(newWord)

	# for reference, here are how you would use the
	# other two stemmers....
	# newWord = lancaster.stem(newWord)
	# newWord = snowball.stem(newWord)

	# make lower case, and return
	return newWord.lower()


## ~~~~~~~~~~~~~~~~~~~~
## START OF FUNCTIONS

# input/output
print('\nopening output files')
text_out = open('Normalized-Texts/' + TextName + '.txt', 'w+')
frequencyOut = open('Frequencies/' + TextName + '.txt', 'w+')

print('opening input file\n')
input_file = open('Original-Texts/' + TextName + '.txt', 'r+')
	# the second parameter of both of these open functions is
	# the permission.
	#
	#	- 'w+' means you can write permissions, and it can 
	#					create a new file of this name if 
	#					this file doesn't exit	
	#
	#	- 'r'  means read-only

print('tokenizing and normalizing.')
print('this might take a little bit...')

# store every word in here
AllTheWords = []

lineCounter = 0
for line in input_file:

	# keep track of prograss
	print("line number " + str(lineCounter))
	lineCounter += 1

   	# regex expressions
   	regexed = re.compile(r'\W+', re.UNICODE).split(line)
   		# this function takes out characters that are not
   		# letter or numbers

   	# build word to print back to file
   	toOutput = ''

   	for word in regexed:
   		
   		# there are lots of blank spaces that get
   		# caught up in our program
   		if word is '':
   			continue

   		word = Normalize(word)
   		AllTheWords.append(word)

		toOutput += Normalize(word) + ' '

	# print word to output file
	text_out.write(toOutput + '\n')

# SORTING
print('\nnow, sorting the inputs')

# group them
sortedWords = Counter(AllTheWords)

# print them out
for key, value in sortedWords.most_common():
	print(str(value) + ' ' + str(key))
	frequencyOut.write(str(value) + ' ' + str(key) + '\n')
