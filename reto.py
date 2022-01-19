def run():
    range_for_4 =[i for i in range(1, 1001) if i % 6 == 0 if i % 4 == 0 if i % 9 == 0]
    print(range_for_4)

if __name__ == "__main__":
    run()