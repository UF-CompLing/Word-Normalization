import re
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer

# all the stemmers
porter = PorterStemmer()
lancaster = LancasterStemmer()
snowball = SnowballStemmer("english")

lemmatiser = WordNetLemmatizer()

out = open('output.txt', 'w+')
with open("first-paragraph.txt", "r+") as file:
   for line in file:

       # regex expressions
       regexed = re.compile(r'\W+', re.UNICODE).split(line)

       # build word to print back to file
       toOutput = ''
       for word in regexed:

           # lemmatize
           newWord = lemmatiser.lemmatize(word)
           print(newWord)

           # stem
           newWord = porter.stem(toOutput)
           newWord = lancaster.stem(newWord)
           newWord = snowball.stem(newWord)

           # print(newWord + " ")

           # add it to a new line
           toOutput += newWord + ' '

       # make lower case
       toOutput = toOutput.lower()

       # print word to output file
       out.write(toOutput + '\n')
