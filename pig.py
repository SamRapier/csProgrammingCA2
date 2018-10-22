def pig(word):
	"""
	This function translates a single word from English to Pig Latin

	It has one parameter which is a string
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
	This fucntion tests all the rules for the pig latin language

	It has no parameters
	"""

	assert pig('happy') == 'appyhay', "pig function is incorrect 1"
	assert pig('duck') == 'uckday', "pig function is incorrect 2"
	assert pig('glove') == 'oveglay', "pig function is incorrect 3"
	assert pig('evil') == 'evilway', "pig function is incorrect 4"
	assert pig('eight') == 'eightway', "pig function is incorrect 5"
	assert pig('yowler') == 'owleryay', "pig function is incorrect 6" 
	assert pig('crystal') == 'ystalcray', "pig function is incorrect 7"



def user_input_translator():
	"""
	This function takes the input from the user and translates each word into
	Pig Latin

	It has no parameters
	"""

	# initialising the userIn as filler so that the while loop will start
	userIn = 'filler'

	# loops through until the user only presses enter or return
	while userIn != '':
		userIn = input('Enter a word to be translated into Pig Latin: ')
		
		# splits the input into a list so that multiple words can be 
		# translated in this loop
		words = userIn.split()

		# loops through each word input by the user, translates and prints it 
		# on one line
		for word in words:
			print(pig(word), end=' ')
		
		# adds a new line 
		print()
			

if __name__ == "__main__":
	user_input_translator()
	test_pig()