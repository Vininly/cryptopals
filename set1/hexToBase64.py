import sys

LOOKUP = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

def hexToBin(hex):
	'''Converts an input hex string into binary, zero padding when necessary'''

	binary = ''

	for char in hex:
		# Converts hex to decimal for zero padding
		dec = int(char, base=16)
		# Convert dec to binary string, slicing off first two chars (0b)
		b2 = str(bin(dec))[2:]
		# Taking care of 0 padding
		if dec <= 1:
			binary = binary + '000' + b2
		elif dec <= 3:
			binary = binary + '00' + b2
		elif dec <= 7:
			binary = binary + '0' + b2
		else:
			binary = binary + b2

	return binary

def hexToBase64(hex):
	'''Converts an input hex string into base 64. Currently does not account
	for an input length that is not divisible by 3

	Precondition: len(hex) must be divisible by 3'''

	assert (len(hex)%3 == 0), 'Input length is not a multiple of 3'

	binary = hexToBin(hex)

	result = ''

	# Takes chunks of 6, converts to decimal, and converts to base64 based on
	# a lookup string
	for i in range(0, len(binary), 6):
		dec = int(binary[i:i+6], base=2)
		if dec <= 25:
			result = result + LOOKUP[dec]
		elif dec <= 51:
			result = result + LOOKUP[dec-26].lower()
		elif dec <= 61:
			result = result + str(dec - 52)
		elif dec == 62:
			result = result + '+'
		else:
			result = result + '/'

	return result

if __name__ == '__main__':
	print hexToBase64(sys.argv[1])
