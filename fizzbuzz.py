'''
Write a program that prints out the final series of numbers where those divisible by X, 
Y and both are replaced by “F” for fizz, “B” for buzz and “FB” for fizz buzz.

https://www.codeeval.com/open_challenges/1/
'''

import sys

test_cases = open(sys.argv[1],"r")

def fizzbuzz(insert_text):


	
	for line in insert_text:
		string = ''
		numberlist = str(line).split()
		valu = 1
		while valu <= int(numberlist[2]):
			if valu%int(numberlist[0]) == 0 and valu%int(numberlist[1]) == 0:
				string += "FB "
			if valu%int(numberlist[0]) == 0 and not valu%int(numberlist[1]) == 0:
				string += "F "
			elif valu%int(numberlist[1]) == 0 and not valu%int(numberlist[0]) == 0:
				string += "B "
			elif valu%int(numberlist[0]) != 0 and valu%int(numberlist[1]) != 0:
				string += str(valu) + " "

			valu = valu + 1
		string.strip()

		print string


fizzbuzz(test_cases)
