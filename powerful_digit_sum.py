max_dig_sum=0
for a in range(1,100):
	for b in range(0,100):
		n=a**b
		digits=[int(d) for d in str(n)]
		dig_sum=sum(digits)
		max_dig_sum=max(max_dig_sum,dig_sum)

print(max_dig_sum)

