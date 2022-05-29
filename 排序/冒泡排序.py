def bubble_sort(arr):
    """
    时间复杂度：O(n**2)
    外循环为比较的轮数，将最大值（小），次大值（小）依次放到最后；
    内循环为比较的过程，将大的值依次往后移动
    simplify：数组length次遍历，遍历余数组，冒出最大值
    """
    length = len(arr)
    for i in range(length):

        for j in range(0, length - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr

print(bubble_sort([8,3,1,6,9,0]))