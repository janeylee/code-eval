'''
Write a program which determines the sum of the first 1000 prime numbers.

https://www.codeeval.com/open_challenges/4/
'''

def sumAll(m):
	total = 0
	for value in m:
		total = total + value
	return total


def checkPrime(number):
	if number == 2:
		return True
	for i in range(2, number):
		if number%i == 0:
			return False
	return True
	# to check if all items in  list are 
	#prime, iterate through it and on
	#the first instance of it not being prime, 
	#mark as false. otherwise it's true

def getPrimes():
	list_of_primes = []
	num = 2

	while len(list_of_primes) < 1000:
		if checkPrime(num) == True:
			list_of_primes.append(num)
		num = num + 1 
		#this must be outside the if
		#statement because you want to increment
		#even if checkPrime is false
	return list_of_primes

thelist = getPrimes()
print sumAll(thelist)

