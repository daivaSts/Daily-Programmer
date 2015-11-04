"""
[2015-08-03] Challenge #226 [Easy] Adding fractions
For today's challenge, you will get a list of fractions which you will add together and produce
 the resulting fraction, reduced as far as possible.
Input 1:
1/6
3/10
Output: 7/15

Input 2:
3
1/3
1/4
1/12

Output 2:2/3
"""
def add_fractions(*args):
	result = "0/1"
	for i in range(len(args)):
		result = add_fractions_two(result, args[i])
	return result


def add_fractions_two(a,b):
	nom_a, denom_a = [int(i) for i in a.split("/") ]
	nom_b, denom_b = [int(i) for i in b.split("/") ]

	denom_common = denom_a * denom_b
	nom_total = nom_a * denom_b + nom_b * denom_a

	gcd_num = gcd(nom_total, denom_common)

	return '{0}/{1}'.format(nom_total/gcd_num, denom_common/gcd_num)

def gcd(x, y):
    while y != 0:
    	(x, y) = (y, x % y)
    return x

print add_fractions("1/6","3/10")
