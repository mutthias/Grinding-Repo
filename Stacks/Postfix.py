class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        res = 0

        for n in tokens:
            if n == "+":
                v1, v2 = stack.pop(), stack.pop()
                total = v2 + v1
                stack.append(total)
            elif n == "-":
                v1, v2 = stack.pop(), stack.pop()
                difference = v2 - v1
                stack.append(difference)
            elif n == "*":
                v1, v2 = stack.pop(), stack.pop()
                product = v2 * v1
                stack.append(product)
            elif n == "/":
                v1, v2 = stack.pop(), stack.pop()
                quotient = v2 / v1
                if quotient > 0:
                    quotient = math.floor(quotient)
                else:
                    quotient = math.ceil(quotient)
                stack.append(quotient)
            else:
                stack.append(int(n))
        
        return stack[-1]
        