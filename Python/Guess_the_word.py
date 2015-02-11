#!/usr/bin/env python

#Documentation: Essentially, the user will enter a word phrase or any item and then the program will try and find out what that phrase is. It will run through all special characters and letters. To check for solution, it will just compare to the user entry.
#Eventually, there will be a list for checking common things and also checking for unlimited length. As well, there will be implementation for only being able to check at certain points.

def Phrase():
	phrase = raw_input("What is the phrase you would like the computer to guess?")
	try:
		str(phrase)
	except ValueError:
		Phrase()
	return phrase
	
def Guess():
	Char = ['a','s','d','f','q','w','e','r','t','y','u','i','o','p','g','h','j','k','l','z','x','c','v','b','n','m',',','.','/','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','-','_','+','=','`','~','<','>','?',':',';','\'','\"','[','{',']','}']
	ToFind = Phrase()
	PhraseList = list(ToFind)
	Result = []
	j = 0
	while j in range(len(PhraseList)):
		for i in range(len(Char)):
			if PhraseList[j] == Char[i]:
				Result.append(Char[i])
				j += 1
	print 'Is this your phrase: {0}'.format(Result)
	