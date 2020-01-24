def numbers_to_saltar(argument):
    switcher = { 
        1: "1", 
        2: "-1",
        3: "-1",
        4: "-2",  
    } 
    return switcher.get(argument,"3")

def jumpingOnClouds(c):
	saltos = 0
	count = 0
	i=0
	while i < len(c):
		if c[i] == 0 and count < 4:
			count+=1
			i+=1
		else:
			saltos += 1
			aux = int(numbers_to_saltar(count))
			count = 0
			i += aux

		print(i)
		if c[i-1] == 0 and (i == len(c)) and count > 1:
			saltos += 1
			aux = int(numbers_to_saltar(count))
			i += 1

	return saltos
			

			
c3 = [0, 0, 1, 0, 0, 1, 0]
c2 = [0, 0, 0, 1, 0, 0]
c1 = [0, 0, 0, 0, 1, 0]
c = [0, 0, 1, 0, 0, 1, 0]
print('saltos: ',jumpingOnClouds(c))
