class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        """
        core: 维护了一个不严格的单调递减队列。每次窗口的移动涉及两个操作：出窗口和入窗口。
        出窗：如果出窗元素等于当前最大值，则将最大值出队
        入窗：一直判断入窗元素是否大于queue[-1],从而将它放在该放的位置，维持队列递减性质。
        时间复杂度：从头到尾遍历nums一遍O(n)，在窗口内找最大值是O(1),时间复杂度为O(n)
        """

        res = []
        queue = collections.deque()
        n = len(nums)
        # j1：i的遍历范围是(1-k, n-k), j的遍历范围是（0, n-1）,刚开始滑动时只有一个元素入队，这样后面可以方便的维护队列的递减性质
        for i, j in zip(range(1 - k, n + 1 - k), range(n)):

            # j2：i 到1的时候才涉及到出窗
            # j3：顺序问题：如果将while放到前面，需要判断队列是否为空
            # if i >= 1 and queue and nums[i-1] == queue[0]:
            if i >= 1 and nums[i - 1] == queue[0]:
                queue.popleft()
            # j4：先入先出，维护队列递减的性质
            while queue and nums[j] > queue[-1]:
                queue.pop()
            queue.append(nums[j])

            # j5：形成窗口时，记录结果
            if i >= 0:
                res.append(queue[0])
        return res