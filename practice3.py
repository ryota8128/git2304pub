def func(x):
	if x == 0:
		return 1
	else:
		return x * func(x-1)
