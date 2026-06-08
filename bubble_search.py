my_data = [10, 24, 67, 57, 59, 98, 14, 89, 94, 25, 46, 37, 466, 733, 532, 76, 87, 32, 342, 127]
my_data_len = len(my_data)
swapping = True

while swapping:
    swapping = False

    for i in range(1, my_data_len):
        if my_data[i - 1] > my_data[i]:
            my_data[i - 1], my_data[i] = my_data[i], my_data[i - 1]
            swapping = True

    my_data_len -= 1

print(my_data)
