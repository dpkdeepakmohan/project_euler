def reverse_string(s):
	return s[::-1]


def is_lychrel(n):

	for i in range(0,50):
		rev_n=int(reverse_string(str(n)))
		n=n+rev_n
		#print(n,'+',rev_n,'=',n)
		rev_n=int(reverse_string(str(n)))
		if n==rev_n:
			return False
	return True

def count_lychrel_numbers():
	max_n=10000
	cnt=0
	for n in range(1,max_n):
		if is_lychrel(n):
			cnt=cnt+1
	print(cnt)
count_lychrel_numbers()
