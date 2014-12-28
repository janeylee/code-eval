'''
https://www.codeeval.com/open_challenges/8/
Write a program that reverses the words in an input sentence.
'''


test_cases = open("test.txt","r")

def reverse(insert_text):
	
	for line in insert_text:
		new = []
		wordlist = line.split()
		n = len(wordlist)-1
		while n >= 0:
			new.append(wordlist[n])
			n = n - 1
		new = " ".join(new)
		print new




reverse(test_cases)
