
def pancakeSort(arr):
    if not arr: return []
    k_list = []
    max_value = len(arr)
    while max_value > 1:
        max_value_idx = arr.index(max_value)
        if max_value_idx != max_value - 1:
            if max_value_idx != 0:
                arr[:max_value_idx + 1] = arr[:max_value_idx + 1][::-1]
                k_list.append(max_value_idx + 1)
            arr[:max_value] = arr[:max_value][::-1]
            k_list.append(max_value)
        max_value -= 1
    return  k_list

sort_list = [5, 2, 4, 1, 3]
print(pancakeSort(sort_list))

