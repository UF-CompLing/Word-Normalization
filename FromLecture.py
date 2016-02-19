import re

TextName = 'King-James-Bible'

## ~~~~~~~~~~~~~~~~~~~~
## START OF FUNCTIONS

print('opening file\n')
input_file = open(TextName + '.txt', 'r+')
	# the second parameter of both of these open functions is
	# the permission.
	#
	#	- 'w+' means you can write permissions, and it can 
	#					create a new file of this name if 
	#					this file doesn't exit	
	#
	#	- 'r'  means read-only

print('going through every line in file. hold on a sec...')
# store every word in here
for line in input_file:

   	# regex expressions
   	regexed = re.compile(r'\W+', re.UNICODE).split(line)
   		# this function takes out characters that are not
   		# letter or numbers
   		#
   		# BUT... it makes a list. let's join that list back together!

   	# build word to print back to file
   	toOutput = ''

   	for word in regexed:
   		
   		# there are lots of blank spaces that get
   		# caught up in our program
   		if word is '':
   			continue
   		
   		toOutput += word.lower() + ' '


	# print word to our screen
	print(toOutput + '\n')