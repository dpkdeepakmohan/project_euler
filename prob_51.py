def is_prime(n):
	if n<=1:
		return False
	d=2
	while d*d<=n:
		if n%d==0:
			return False
		d+=1
	return True

def get_subsets(s):
	sz=len(s)	
	subsets=[]
	for mask in range(1,1<<sz):
		subset=[s[idx] for idx in range(sz) if (1<<idx)&mask]
		subsets.append(subset)
	return subsets
	
n=1000
done=False

while True:
	if is_prime(n):
		digits=[int(d) for d in str(n)]
		sz=len(digits)
		for digit in range(3):
			occurences=[idx for idx,val in enumerate(digits) if val==digit]
			subsets=get_subsets(occurences)
				
			for subset in subsets:
				primes=1
				family=[]
				for rep in range(digit+1,10):
					new_digits=[rep if idx in subset else digits[idx]  for idx in range(sz)]
					new_num=int(''.join(map(str,new_digits)))
					if is_prime(new_num):
						primes+=1
						family.append(new_num)
			
				if primes==8:
					print(n,family)
					done=True
	
	n=n+1
	if done :
		break
