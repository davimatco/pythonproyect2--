def division(num):
    division = []
    for i in range(1, num + 1):
        if num % i == 0:
            division.append(i)
        return division



def run():
        num = input("ingresa un numero: ")
        assert num.isnumeric(), "debes ingresar un numero"              # afirmo que lo que ingreso el usuario es un numero
        print (division(int(num)))
        print("termino")
  


if __name__ == "__main__":
    run()