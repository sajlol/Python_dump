listt = ['a','b','c']

for i, item, in enumerate(listt):
	print(item)

	if i == len(listt) -1:
		print("This is after the last item in list")