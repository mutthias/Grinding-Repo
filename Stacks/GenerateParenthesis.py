class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def BT(openPs, closePs, stack):
            if openPs == closePs == n:
                res.append("".join(stack))
                stack = []
            if openPs < n:
                stack.append("(")
                BT(openPs + 1, closePs, stack)
                stack.pop()
            if closePs < openPs:
                stack.append(")")
                BT(openPs, closePs + 1, stack)
                stack.pop()
        
        BT(0, 0, [])
        return res