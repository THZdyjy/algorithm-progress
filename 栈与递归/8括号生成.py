class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []

        def generate(left, right, n, s):
            # terminator
            if left == n and right == n:
                result.append(s)
                return
                # process current logic:
            # drill down
            if left < n:
                generate(left + 1, right, n, s + "(")

            if left > right:
                generate(left, right + 1, n, s + ")")

        generate(0, 0, n, "")
        return result