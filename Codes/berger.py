import math

def comp(s):
	if(s=='0'):
		return '1'
	elif(s=='1'):
		return '0'

def complementary(s):
	aux = ""
	for i in s:
		aux += comp(i)

	return aux

def codify(a):
	num_bits = int(math.ceil(math.log(len(a)+1, 2)))
	num_ones = a.count('1')
	
	num_ones_bin = "{0:b}".format(num_ones)
	
	code = '0' * (num_bits - len(num_ones_bin))
	code += num_ones_bin
	code = complementary(code)
	"""
	print ' |Codify:'+' '*27+'|'
	print ' |  bits_ori: ' + str(a)+' '*(22 - len(str(a)))+'|'
	print ' |  bits_cod: ' + str(a+code)+' '*(22 - len(str(a+code)))+'|'
	"""
	return a+code

def decodify(a):
	num_bits_code = len(a)
	added_bits = int(math.ceil(math.log(num_bits_code,2)))
	num_bits_orig = num_bits_code - added_bits

	bits_orig = a[:num_bits_orig]
	
	print ' |Decodify:'+' '*25+'|'
	print ' |  bits_cod: ' + str(a)+' '*(22 - len(str(a)))+'|'
	print ' |  bits_dec: ' + str(bits_orig)+' '*(22 - len(str(bits_orig)))+'|'

	check_code = codify(bits_orig)
	return ((check_code == a), bits_orig)


def check_ber(c1,c2):
	# c1 and c2 matrixes to string
	c1 = ''.join(str(x) for x in c1[0])
	c2 = ''.join(str(x) for x in c2[0])

	if(codify(c1) == c2):		
		if(decodify(c2)[0]):
			return True
	else:
		return False
