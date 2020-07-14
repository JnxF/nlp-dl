#!/usr/bin/python


#Create Traditional Chinese Word List and gold standard corpus

import nltk

rawtextfile=open("chinesetext.utf8","w")
goldfile=open("chinesetext_goldstandard.utf8","w")
wordsfile=open("chinesetrad_wordlist.utf8","w")


wordset=set()
sents=nltk.corpus.sinica_treebank.sents()

for s in sents:
	for w in s: wordset.add(w) #add to set to create dictionary
	rawtextfile.write(''.join(s)+'\n') #write words to raw file
	goldfile.write(' '.join(s)+'\n') #write to gold file seperated by space

print "Raw Chinese Text Written to: "+rawtextfile.name
print "Gold Standard Written to: "+goldfile.name

for w in sorted(wordset):
	wordsfile.write(w+'\n')
	
print "Gold Standard Written to: "+wordsfile.name

