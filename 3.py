def prime_nums(num):

	primes = [2]

	if num < 2:
		return []
	elif num == 2:
		return primes

	i = 3

	while i <= num:
		for j in range(3,num-1):
			if i%j == 0:
				i += 2
				break
		else:
			primes.append(i)
			i += 2

	return primes

if __name__ == '__main__':
 	a = prime_nums(100)
 	print(a)