"""
core: 因为nums1的长度是m+n. 直接把nums2放到nums1中即可。
仨指针，p1, p2 分别指向nums1和nums2的尾部，进行二者的比较。
谁大，就把谁放到nums1的末尾，此时  tail指针和p指针向前移动一位。重复这个过程，直到把nums2全部放到1中。
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        p1, p2 = m - 1, n - 1
        tail = m + n - 1
        # j1: 当1和2数组长度都没比较完时，重复过程
        while p2 >= 0 and p1 >= 0:
            if nums2[p2] >= nums1[p1]:
                nums1[tail] = nums2[p2]
                tail -= 1
                p2 -= 1
            else:
                # j3：tail处位置是用来放1或1数组值的，他的大小无所谓，直接赋值就行，不用交换
                nums1[tail] = nums1[p1]
                tail -= 1
                p1 -= 1
        # j2：都1或2比较完了，此时看看2有没有完，若都放完了，ok。没有的话，继续把2放入。
        while p2 >=0:
            nums1[tail] = nums2[p2]
            p2 -= 1
            tail -= 1
        return nums1