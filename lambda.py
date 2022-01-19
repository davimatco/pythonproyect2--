def run():
    # numbers =[i**2 for i in range(1, 6) ]

    # print(numbers)

    my_list = [1, 2, 3, 4, 5]
    numbers = list(map(lambda x: x**2, my_list))
    print(numbers)


if __name__=="__main__":
    run()