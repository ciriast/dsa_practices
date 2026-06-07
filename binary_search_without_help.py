my_arr = [9, 67, 65, 87, 900, 100, 29, 30, 46, 75, 87, 89, 90, 54, 23, 78, 65, 46]
sorted_arr = sorted(my_arr)
arr_len = len(sorted_arr)

low = 0
high = arr_len - 1

print(sorted_arr)
my_value = 9001
index = -1

while low <= high:
    mid = (low + high) // 2

    if sorted_arr[mid] == my_value:
        print("Found it at index: ", mid)
        index = mid
        break

    if sorted_arr[mid] < my_value:
        low = mid + 1
    elif sorted_arr[mid] > my_value:
        high = mid - 1

if index == -1:
    print("No found it")
