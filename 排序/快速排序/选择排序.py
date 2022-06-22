def select_sort(arr):
    """
    将最小值放到数组前面。
    :param arr:
    :return:
    """
    length = len(arr)
    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr
print(select_sort([2,6,4,1,0,5]))    