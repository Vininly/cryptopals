import sys

REF = {}
KEYLIST = '0123456789abcdef'

def buildRef(file):
	'''Builds the referance dictionary by parsing an input plaintext file and
	counting occurances of characters. All characters are converted to lowercase,
	and it's assumed that the size of the input file is large enough that the
	frequencies of letters evens out.

	It's also assumed that all letters occur at least once in the input file'''

	with open (file, 'r') as f:
		for line in f:
			# Remove newlines and make all characters lowercase
			string = line.strip().lower()
			for char in string:
				if char.isalpha():
					if char not in REF:
						REF[char] = 1
					else:
						REF[char] += 1

def normalizeRef():
	'''Normalizes ref to make all entries sum to 1 in order to find relative 
	frequencies'''

	total = 0.0

	for val in REF.itervalues():
		total += val

	for key in REF:
		REF[key] = REF[key] / total



if __name__ == '__main__':
	buildRef('twocities.txt')
	buildRef('hamlet.txt')
	buildRef('gatsby.txt')
	normalizeRef()
	print ref
