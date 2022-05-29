class Solution:
    def leastInterval(self, tasks, n):
        task_occur_num = sorted([takes.count(take) for take in set(takes)])
        max_occur_number = task_occur_num[-1]
        max_occur_number_time = task_occur_num.count(max_occur_number)
        return max(((max_occur_number - 1) * (n+1) + max_occur_number_time), len(takes))



s = Solution()
takes = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(s.leastInterval(takes, 2))