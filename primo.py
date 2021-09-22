# una función que valida si es un número primo, utilizando tipado estático.
def is_prime(number: int) -> bool:
	if number < 2:
		return False
	elif number == 2:
		return True
	elif number > 2 and number % 2 == 0:
		return False
	else:
		for i in range(3, number): # Apartir de 3 hasta el numero
			if number % i == 0:
				return False
	return True

def run():
    print(is_prime(5))

if __name__ == '__main__':
    run()
