mx_n=100
gt_one_mln=0
one_mln=1000000
cache={}

for n in range(0,mx_n+1):
	for r in range(0,n+1):
		if r==n or r==0:
			cache[(n,r)]=1
		else:
			w=cache[(n-1,r-1)]
			wo=cache[(n-1,r)]
			ncr=w+wo
			if ncr>one_mln:
				gt_one_mln+=1
			cache[(n,r)]=ncr
print(gt_one_mln)
