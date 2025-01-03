class Solution:
    def compress(self, chars: List[str]) -> int:
        def reverse(left, right):
            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1
        n = len(chars)
        write = left = 0  # j1：初始化write和left位chars开头位置。
        for read in range(n):
            if read != n - 1 and chars[read] == chars[read + 1]: continue
            # j2:到了该行，read指向的是连续字符的末尾， 开始对这一连续字符进行处理，首先写入
            chars[write] = chars[read]
            write += 1
            # j3:处理连续字符的数目, 注意这里减去的是left, 而不是write, 当num大于1时候，运用短除法+反转对数字进行处理
            num = read - left + 1
            if num > 1:
                # j4:因为运用短除法得到的数字是反的（举个例子就行），需要进行反转，所以需要记录是哪几位进行反转。
                # 这里左边是write, 然后写入的过程，write会加1，最后便得到反转的那几位。
                anchor = write
                # j5: 短除法
                while num > 0:
                    chars[write] = str(num % 10)
                    write += 1
                    num = num // 10
                reverse(anchor, write - 1)
            # j6：left位置更新，更新到下一个连续字符
            left = read + 1
        return write
"""
三指针， read指针找到连续字符的末尾，如aaaa.
        write指向chars中待写入的位置，从左往右依次写入。
        left指向当前连续字符的开头。
"""
