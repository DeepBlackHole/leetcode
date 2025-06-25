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
# solution = Solution()
# print(solution.romanToInt("III"))  # Output: 3
# print(solution.romanToInt("IV"))   # Output: 4
# print(solution.romanToInt("IX"))   # Output: 9
# print(solution.romanToInt("LVIII"))  # Output: 58
# print(solution.romanToInt("MCMXCIV"))  # Output: 199
# print(solution.romanToInt("XLII"))  # Output: 42
# print(solution.romanToInt("MMXXIII"))  # Output: 2023
# print(solution.romanToInt("CDXLIV"))  # Output: 444    


        