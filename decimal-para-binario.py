def decimal_para_binario(decimal):
	binario = ''	
	while decimal > 0:
		binario+= str(decimal%2)
		decimal//= 2
	return binario[::-1]	

if __name__ == '__main__':
	num = int(input("Digite o número que deseja converter: "))
	print(decimal_para_binario(num))


