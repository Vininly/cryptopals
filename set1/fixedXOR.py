import sys

def fixedXOR(hex1, hex2):
	'''Takes the XOR of hex1 and hex2

	Precondition:	hex1 and hex2 have the same length, and are both valid hexadecimal
					numbers'''

	assert (len(hex1) == len(hex2)), 'The two inputs have different lengths'

	# Converting the hex numbers to decimal
	num1 = int(hex1, base=16)
	num2 = int(hex2, base=16)

	# Taking the XOR
	xor = num1 ^ num2

	# Slicing off the first two characters (0x) and last 
	result = str(hex(xor))[2:]

	# If result is a long, has an extra L at the end
	if result[len(result)-1] == 'L':
		result = result[:len(result)-1]

	return result

if __name__ == '__main__':
	print fixedXOR(sys.argv[1], sys.argv[2])