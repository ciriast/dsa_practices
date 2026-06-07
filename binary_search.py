my_data = [2, 10, 100, 400, 500, 766, 700, 123, 456, 765, 98, 19, 45, 66, 255, 86]
my_sorted_data = sorted(my_data)
my_sorted_len = len(my_sorted_data)
my_value = 2

low = 0
high = my_sorted_len - 1
index = -1

print(my_sorted_data)

while low <= high:
    mid = (low + high) // 2
    
    if my_sorted_data[mid] == my_value:
        print("Found it! Index:", mid)
        index = mid

        break
    
    if my_sorted_data[mid] < my_value:
        low = mid + 1
    elif my_sorted_data[mid] > my_value:
        high = mid - 1

if index == -1:
    print("No found it!")
