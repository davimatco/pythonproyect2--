def read():                      #leer un archivo que va a contener numeros del 1 al 10 y convertirla a lista 
    numbers = []                 #lista
    with open("./archivos/numbers.txt", "r", encoding = "utf-8") as f:
        for line in f:           #leer cada linea con esta estructura 
            numbers.append(int(line))
    print(numbers)

def write():
    names = ["miguel", "david", "mateo", "valentina"]
    with open("./archivos/names.txt", "w", encoding=" utf-8") as f: 
        for name in names:
            f.write(name)
            f.write("/n")


def run():
    write()



if __name__ == "__main__":         #entri point
    run()