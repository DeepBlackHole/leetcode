class Solution:
    def romanToInt(self, s: str) -> int:

        roman = {
            'I' : '1', 'V' : '5',
            'X' : '10', 'L' : '50',
            'C' : '100', 'D' : '500', 'M' : '1000'
        }

        prev = 0
        output = 0

        for i in reversed(s):
            value = int(roman[i])
            if value < prev:
                output -= value
            else:
                output += value
                prev = value
        return output

# Example usage:
s = "XVI"
sol = Solution()
print(sol.romanToInt(s))