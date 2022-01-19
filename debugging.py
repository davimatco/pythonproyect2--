def division(num):
    division = []
    for i in range(1, num + 1):
        if num % i == 0:
            division.append(i)
        return division



def run():
    try: 
        num = int(input("ingresa un numero: "))
        print (division(num))
        print("termino")
    except ValueError: 
        print("debes ingresar un numero")


if __name__ == "__main__":
    run()