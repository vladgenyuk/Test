class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        tape = ''

        for i in s:
            if len(tape) > k:
                return tape[k-1]
            if i not in '1234567890':
                tape += i
            else:
                tape = tape * int(i)

        return tape[k-1]


s = Solution()

print(s.decodeAtIndex('leet2code3', 10))
print(s.decodeAtIndex('ha22', 5))
print(s.decodeAtIndex('a234567899999999', 10))
