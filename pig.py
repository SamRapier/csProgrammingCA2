def pig(word):
	"""
	This function translates a single word from English to Pig Latin

	It has one parameter which is a string

	It returns the Pig Latin translation
	"""

	# initialising the vowels list and turing the word argument to lower case
	vowels = ['a', 'e', 'i', 'o', 'u']
	word = word.lower()

	# if the first letter is a vowel add way to the end
	if word[0] in vowels:
		word = word + 'way'
	else:
		letter = ''
		count = 0
		# add y to the list of vowels
		vowels.append('y')

		# This loop determines how many consonants are at the beginning 
		while letter not in vowels:
			count = count + 1
			letter = word[count]

		# The initial consonants are moved to the end of the word and ay is 
		# added to the end of the word
		word = word[count:] + word[0:count] + 'ay'
	
	
	return(word)


def test_pig():
	"""
	This function tests all the rules for the pig latin language

	It has no parameters

	It returns no value
	"""

	assert pig('happy') == 'appyhay', "pig function is incorrect"
	assert pig('duck') == 'uckday', "pig function is incorrect"
	assert pig('glove') == 'oveglay', "pig function is incorrect"
	assert pig('evil') == 'evilway', "pig function is incorrect"
	assert pig('eight') == 'eightway', "pig function is incorrect"
	assert pig('yowler') == 'owleryay', "pig function is incorrect" 
	assert pig('crystal') == 'ystalcray', "pig function is incorrect"



def user_input_translator():
	"""
	This function takes the input from the user and translates each word into
	Pig Latin

	It has no parameters

	It will print the translation from the pig function
	"""

	# initialise userIn as filler so while loop will start
	userIn = 'filler'

	# loops until input is empty
	while userIn != '':
		userIn = input('Enter a word to be translated into Pig Latin: ')
		
		# splits input into a list so multiple words can be tanslated 
		words = userIn.split()

		#translates each word and prints it on one line
		for word in words:
			print(pig(word), end=' ')
		 
		print()
			

if __name__ == "__main__":
	test_pig()
	user_input_translator()
	