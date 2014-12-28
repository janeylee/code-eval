'''
https://www.codeeval.com/open_challenges/97/
You have a set of rows with names of famous writers encoded inside. 
Each row is divided into 2 parts by pipe char (|). The first part has a writer's name. 
The second part is a "key" to generate a name.

Your goal is to go through each number in the key (numbers are separated by space) left-to-right. 
Each number represents a position in the 1st part of a row. 
This way you collect a writer's name which you have to output.
'''

test_cases = open("test.txt","r")

def authors(insert_text):

	for line in insert_text:
		new = line.split('|')
		code = list(new[0])
		
		key = new[-1].split()
		
		authors_name = ""
		for element in key:
			element = int(element)
			letter = code[element-1] #letter is a string
			authors_name = authors_name + letter
		print authors_name




authors(test_cases)
