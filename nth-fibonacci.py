def getNthFib(n):
    # Write your code here.
	# define the base case when n is 0 or 1
	if n <= 1:
		return 0
	if n == 2:
		return 1
	# recursively call fib(n-2) + fib(n-1)
	return getNthFib(n-1) + getNthFib(n-2)
