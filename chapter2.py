from __future__ import division

# This is the O(n) solution
def biggest(data):
    ''' find the biggest in a list '''
    m = data[0]
    for each in data:
    	if each > m:
    		m = each
    return m

def decimal_to_binary(decimal):
	def divide_2(decimal):
		whole = decimal // 2
		part = decimal - whole * 2
		return whole, part

	digits = []
	while True:
		whole, part = divide_2(decimal)
		digits.append(part)
		if whole > 0:
			decimal = whole
		else:
			break

	return int(''.join([str(each) for each in digits[::-1]]))

print decimal_to_binary(10)