# Corinne Bradford
# 9/25/2021
# Fall 361

with open("CS361_Exercise_0_2021_f1_Drivers.txt") as file:
    data = file.readlines()

for i in range(len(data)):
    data[i] = data[i].split()


def pretty_print(data, style):
    print(" \n2021 F1 Drivers - ", style)
    print("=========================")
    for i in range(len(data)):
        for j in range(len(data[i])):
            print(data[i][j], end=" ")
        print("")


alpha = sorted(data, key = lambda x: x[1])
num = sorted(data, key = lambda x: int(x[2]))

pretty_print(alpha, "alphabetical")
pretty_print(num, "driver number")
