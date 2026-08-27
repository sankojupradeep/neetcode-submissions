class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        for num in operations:
            if num=="C":
                stack.pop()
            elif num=='D':
                stack.append(2*stack[-1])
            elif num=="+":
                stack.append(stack[-1]+stack[-2])
            else:
                stack.append(int(num))
        return sum(stack)



        