test_case = int(input())

for case in range(1,test_case+1):
	numbers = int(input())
	size=[]
	for number in range(numbers):
		size.append(int(input()))
	count = 0

	average = sum(size)/len(size)

	for hay in size:
		if hay > average:
			count += hay - average
		elif hay < average:
			count += average - hay
	
	print("#{} {}".format(case,int(count//2)))
			

