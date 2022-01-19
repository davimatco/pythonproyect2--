def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {"firstname": "david", "lastname": "acosta"}

    super_list = [                         
        {"firstname": "david", "lastname": "acosta"},
        {"firstname": "facundo", "lastname": "acosta"},
        {"firstname": "ernestor", "lastname": "acosta"},
        {"firstname": "jose", "lastname": "acosta"},
    ]  #esta es una lista que contiene diccionarios 

    super_dicc = {
        "natal_num": [1, 2, 3, 4, 5],
        "integer_nums": [-1, -2, -3, -4],
        "floating_num": [1.1, 1.3, 5.67]
    }

    for key, value in super_dicc.items():
        print(key, "-", value)
if __name__=="__main__":
    run() 