mx=1000000000
for n in range(1,mx):
	two_n=''.join(sorted(str(2*n)))
	three_n=''.join(sorted(str(3*n)))
	four_n=''.join(sorted(str(4*n)))
	five_n=''.join(sorted(str(5*n)))
	six_n=''.join(sorted(str(6*n)))
	if two_n==three_n and three_n==four_n and four_n==five_n and five_n==six_n:
		print(n,two_n,three_n,four_n,five_n,six_n)
		break
