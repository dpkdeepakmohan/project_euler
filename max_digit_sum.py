
#returns the max{digit_sum(x)}
def max_digit_sum(n):
	n_str=str(n)
	length=len(n_str)
	if length==1:
		return n

	msd=int(n_str[0])
	digits=[int(d) for d in n_str]
	print("Digits:",digits)
	suffix_digits={d for d in digits[1:]}
	print("Suffix digits:",suffix_digits)
	if len(suffix_digits)==1 and 9 in suffix_digits:
		return sum(digits)
	else:
		return msd-1+9*(length-1)

n=10**100
print("n:",n,"\nMax digit sum:",max_digit_sum(n))
