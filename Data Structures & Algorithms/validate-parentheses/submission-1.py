class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        for num in s:
            if num=="[" or num=="(" or num=="{":
                stack.append(num)
            else:
                if not stack:
                    return False
                top=stack.pop()
                if num=="]" and top!="[":
                    return False
                elif num==")" and top!="(":
                    return False
                elif num=="}" and top!="{":
                    return False
        return len(stack)==0

        