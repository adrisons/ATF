import math
 
# a and b should be string representation of the binary components
# You could easily extend this to overload the + operator for binaries,
# but this is already built into python.
def binary_addition(bin_a, bin_b):
    """Performs a binary addition against two provided binary numbers"""
 
    # Pad the components so they are of equal length
    max_length = max(len(bin_a), len(bin_b))*2
    bin_a, bin_b = bin_a.zfill(max_length), bin_b.zfill(max_length)
 
 
    carry = 0
    result = ''
 
    # Note that we work from right to left
    for i in range(0, max_length)[::-1]:
        tmp = int(math.floor((int(bin_a[i]) + int(bin_b[i]) + carry)/2))
        res = str(int(bin_a[i]) + int(bin_b[i]) + carry - 2*tmp)
        result += res
        carry = tmp
 
    result = (result + str(carry))[::-1]
    try:
        return result[result.index('1'):]
    except ValueError, ex:
        return '0'

def array_to_str(a):
	aux = ''
	for i in a:
		aux += str(i)
	return aux

# Double precision checksum 
def checksum_dp(code):
	a = array_to_str(code[0])
	b = array_to_str(code[1])
	c = array_to_str(code[2])
	d = array_to_str(code[3])
	sum1 = binary_addition(a,b)
	sum2 = binary_addition(c,d)
	sumTot = binary_addition(sum1,sum2)
	return sumTot


def check_cs(c1,c2):
    i1 = checksum_dp(c1)
    print ' | sent:' + i1 + ' '*(28-len(i1)) + '|'
    i2 = checksum_dp(c2)
    print ' | recv:' + i2 + ' '*(28-len(i2)) + '|'
    if(i1==i2):
        return True
    else:
        return False


