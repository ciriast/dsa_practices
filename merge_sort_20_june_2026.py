def merge_sort(nums: list[int]) -> list[int]:
    nums_len = len(nums)

    if nums_len < 2:
        return nums

    mid = nums_len // 2
    left = merge_sort(nums[:mid])
    right = merge_sort(nums[mid:])

    return merge(left, right)

def merge(a: list[int], b: list[int]) -> list[int]:
    i = 0
    j = 0
    a_len = len(a)
    b_len = len(b)
    final_list = []

    while i < a_len and j < b_len:
        if a[i] < b[j]:
            final_list.append(a[i])
            i += 1
        else:
            final_list.append(b[j])
            j += 1

    while i < a_len:
        final_list.append(a[i])
        i += 1

    while j < b_len:
        final_list.append(b[j])
        j += 1

    return final_list

print(merge_sort([12, 184, 78, 98, 144]))
