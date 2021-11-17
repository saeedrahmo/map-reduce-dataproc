with open("NDBench-testing.csv") as file:
    for line in file:
        print(line.rstrip().split(',')[0])  # rstrip()
