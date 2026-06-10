def merge_sort(nums: list[int]) -> list[int]:
    nums_len = len(nums)

    if nums_len < 2:
        return nums

    mid = nums_len // 2
    sorted_left = merge_sort(nums[:mid])
    sorted_right = merge_sort(nums[mid:])

    return merge(sorted_left, sorted_right)


def merge(a: list[int], b: list[int]) -> list[int]:
    i = 0
    j = 0
    a_len = len(a)
    b_len = len(b)
    final_list = []

    while i < a_len and j < b_len:
        if nums[i] <= nums[j]:
            final_list.append(nums[i])
            i += 1
        else:
            final_list.append(nums[j])
            j += 1


    
