class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        digit_stack = []
        for i in range(len(tokens)):
            token = tokens[i]
            if token in "+*-/":
                op2 = int(digit_stack.pop())
                op1 = int(digit_stack.pop())
                
                if token == "+":
                    digit_stack.append(str(op1 + op2))
                elif token == "*":
                    digit_stack.append(str(op1 * op2))
                elif token == "-": 
                    digit_stack.append(str(op1 - op2))
                elif token == "/":
                    digit_stack.append(str(int(op1 / op2)))
        
            else:
                digit_stack.append(token)
        
        return int(digit_stack[0])
        