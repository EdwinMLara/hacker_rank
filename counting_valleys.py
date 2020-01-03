def check_valley(count_pass):
	if count_pass < 0:
		return 1
	else:
		return 0


def countingValleys(n,s):
	valleys = 0
	count = 0
	count_pass = 0

	for i in range(0,n):
		if s[i] == 'U':
			count_pass = count
			count += 1
			if count == 0:
				valleys += check_valley(count_pass)
			print('arriba')
		else:
			print('abajo')
			count -= 1
	return valleys

n=8
s='UDDDUDUU'
print(countingValleys(n,s))