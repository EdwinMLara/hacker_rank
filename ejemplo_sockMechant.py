
import math

def pair(count,count_pair):
	count = count + 1
	if count % 2 == 0:
		aux_modulo = count / 2 
		count_pair = count_pair + aux_modulo
	elif count > 1:
		count = count - 1
		aux_modulo = count / 2
		count_pair = count_pair + aux_modulo
	return count_pair

def sockMerchant(n,ar):
	count = 0
	count_pair = 0
	ar.sort()
	aux = ar[0]
	print(ar)

	for i in range(1,n):
		if aux == ar[i]:
			count = count + 1
			if i == (len(ar)-1):
				count_pair = pair(count,count_pair)	
		else:
			aux = ar[i]
			
			count_pair = pair(count,count_pair)
			count = 0;		
	count_pair = int(count_pair)
	return count_pair

ar = [10,20,20,10,10,30,50,10,20]
ar2 = [4, 5, 5, 5, 6, 6, 4, 1, 4, 4, 3, 6, 6, 3, 6, 1, 4, 5, 5, 5]
ar3 = [44, 55, 11, 15, 4, 72, 26, 91, 80, 14, 43, 78, 70, 75, 36, 83, 78, 91, 17, 17, 54, 65, 60, 21, 58, 98, 87, 45, 75, 97, 81, 18, 51, 43, 84, 54, 66, 10, 44, 45, 23, 38, 22,44, 65, 9, 78, 42, 100, 94, 58, 5, 11, 69, 26, 20, 19, 64, 64, 93, 60, 96, 10, 10, 39, 94, 15, 4, 3, 10, 1, 77, 48, 74, 20, 12, 83, 97, 5, 82, 43, 15, 86, 5, 35, 63, 24, 53, 27, 87, 45, 38, 34, 7, 48, 24, 100, 14, 80, 54]

print(sockMerchant(len(ar),ar))