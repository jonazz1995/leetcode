def isValid(s: str) -> bool:
        if not s:
            return True
        para = {")": "(", "}": "{", "]": "["}
        stack = []
        for i in range(len(s)):
            if s[i] in [")", "}", "]"]:
                if not stack or para.get(s[i]) != stack.pop():
                    return False
            else:
                stack.append(s[i])
        return True

s = "["
print(isValid(s))