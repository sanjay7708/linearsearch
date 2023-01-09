def linearsearch(a,n):
	count=0
	for i in range(len(a)):
		if a[i] ==n:
			count+=1
			print(count)
linearsearch([1,30,6,5,30,60,30],30)
