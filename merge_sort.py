def merge_sort(nums: list[int]):
    nums_len = len(nums)

    if nums_len < 2:
        return nums

    mid = nums_len // 2

    sorted_left_side = merge_sort(nums[:mid])
    sorted_right_side = merge_sort(nums[mid:])
    
    return merge(sorted_left_side, sorted_right_side)

def merge(a: list[int], b: list[int]) -> list[int]:
    final_list = []
    i = 0
    j = 0

    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            final_list.append(a[i])
            i += 1
        else:
            final_list.append(b[j])
            j += 1
    
    while i < len(a):
        final_list.append(a[i])
        i += 1

    while j < len(b):
        final_list.append(b[j])
        j += 1


    return final_list

my_list = [5, 20, 6, 78, 4]
my_sorted_list = merge_sort(my_list)
print(my_sorted_list)
