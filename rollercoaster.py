
# https://www.codeeval.com/open_challenges/156/

import sys

test_cases = open(sys.argv[1],"r")

def switchNumber(number):
	if number == 0:
		return number + 1
	else:
		return number - 1

def rollercoaster(insert_text):
	string = ''
	
	for line in insert_text:
		number = 0
		for element in line:

			if element.isalpha() == True:

				if number == 0:
					string = string + element.upper()
				if number == 1:
					string = string + element.lower()

				number = switchNumber(number)
				#switching must take place AFTER both conditions are checked 
			else: 
				string = string + element
	return string

print rollercoaster(test_cases)

