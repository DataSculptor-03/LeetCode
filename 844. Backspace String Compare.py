class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def process(string):
            stack = []
            for i in range(len(string)):
                if string[i] == "#":
                    if stack:
                        stack.pop()
                else:
                    stack.append(string[i])
            return "".join(stack)

        return process(s) == process(t)
