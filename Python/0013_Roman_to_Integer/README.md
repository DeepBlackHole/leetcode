# 13. Roman to Integer

Solved
Easy
Topics
premium lock icon
Companies
Hint
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol Value
I 1
V 5
X 10
L 50
C 100
D 500
M 1000
For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9.
X can be placed before L (50) and C (100) to make 40 and 90.
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.

## Example 1:

| Input: s = "III"
Output: 3
Explanation: III = 3.

## Example 2:

| Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

## Example 3:

| Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

Constraints:

1 <= s.length <= 15
s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
It is guaranteed that s is a valid roman numeral in the range [1, 3999].

# Solution

```python
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
```

## Explanation from ChatGPT

### 1 Creating the lookup table

```python
roman = {
    'I': '1',  'V': '5',
    'X': '10', 'L': '50',
    'C': '100','D': '500',
    'M': '1000'
}
```

- Each Roman symbol is mapped to its **decimal value**.
- The values are stored as **strings**, but that’s mainly incidental—you later convert them to `int`. Most people store them directly as integers (`'I': 1`, etc.), which avoids the cast later.

---

### 2 Initialising state

```python
prev = 0     # value of the symbol we just processed (to the right)
output = 0   # running total
```

- `prev` lets you decide whether to **add or subtract** the current numeral, following the Roman rule “smaller value in front = subtraction”.

---

### 3 Scanning the string right-to-left

```python
for i in reversed(s):
```

- Roman-to-decimal conversion is easiest if you read from **right to left**:
  _You already know the value of everything to the right, so you can tell whether the current symbol should be added or subtracted._

---

### 4 Core loop body

```python
value = int(roman[i])   # decimal value of the current symbol
if value < prev:        # smaller than the one on its right?
    output -= value     #   → subtract
else:
    output += value     #   → add
    prev = value        #   and remember it as the new “rightmost” value
```

**Why this works**

| Pattern                       | What happens              | Example                                                                                                            |
| ----------------------------- | ------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| Smaller numeral before larger | `value < prev` ⇒ subtract | In “IV”, you visit `V` first (`prev = 5`). Then `I` (`value = 1`) is `< prev`, so you do `output -= 1`. Result: 4. |
| Otherwise                     | add                       | In “VI”, visit `I` first (`prev = 1`), then `V` (`value = 5` ≥ 1) so you add. Result: 6.                           |

---

### 5 Return the total

```python
return output
```

---

## Complexity

- **Time:** `O(n)` — one pass through the string.
- **Space:** `O(1)` — constant extra memory.

---

## Tiny clean-ups you could make

1. Store integers in the dictionary to skip `int()` casts:

   ```python
   roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50,
            'C': 100, 'D': 500, 'M': 1000}
   ```

2. Rename `prev` to something like `prev_value` for clarity.

Functionally, though, your logic is spot-on and efficient. Hope that helps!

## Explanation from Gemini

The Python code you've provided defines a class `Solution` with a method `romanToInt` that converts a Roman numeral string to its integer equivalent. Let's break down the code step by step.

### `Solution` Class and `romanToInt` Method

```python
class Solution:
    def romanToInt(self, s: str) -> int:
```

- This defines a class named `Solution`. It's a common practice in competitive programming platforms to encapsulate solutions within a class.
- `def romanToInt(self, s: str) -> int:`: This is the method that performs the conversion.
  - `self`: Refers to the instance of the `Solution` class.
  - `s: str`: Specifies that the input `s` is a string (the Roman numeral).
  - `-> int`: Indicates that the method is expected to return an integer.

### Roman Numeral Mapping

```python
        roman = {
            'I' : '1', 'V' : '5',
            'X' : '10', 'L' : '50',
            'C' : '100', 'D' : '500', 'M' : '1000'
        }
```

- `roman = {...}`: This dictionary maps Roman numeral characters to their corresponding integer values.
  - **Correction/Suggestion**: The values in your dictionary are currently strings (e.g., `'1'`, `'5'`). It's better to store them as integers directly to avoid `int()` conversion inside the loop, which can be slightly less efficient.
    ```python
    roman = {
        'I' : 1, 'V' : 5,
        'X' : 10, 'L' : 50,
        'C' : 100, 'D' : 500, 'M' : 1000
    }
    ```

### Initialization

```python
        prev = 0
        output = 0
```

- `prev = 0`: This variable will store the integer value of the _previous_ Roman numeral character processed. It's initialized to `0`. This is crucial for handling the subtractive cases (e.g., IV, IX).
- `output = 0`: This variable will accumulate the total integer value as we iterate through the Roman numeral string.

### Iteration and Conversion Logic

```python
        for i in reversed(s):
            value = int(roman[i]) # Or just roman[i] if values are integers
            if value < prev:
                output -= value
            else:
                output += value
                prev = value
```

- `for i in reversed(s):`: This is the core of the algorithm. It iterates through the input Roman numeral string `s` **from right to left**. This approach simplifies handling the subtractive rules.
  - **Example**: For "IV", it will first process 'V', then 'I'. For "MCMXCIV", it will process 'V', then 'I', then 'C', then 'X', etc.
- `value = int(roman[i])`: Retrieves the integer value corresponding to the current Roman numeral character `i` from the `roman` dictionary. (As noted above, if `roman` stores integers, `int()` is not needed here).
- `if value < prev:`: This condition checks for the **subtractive rule**.
  - If the current `value` is less than the `prev` (value of the character immediately to its right), it means we have a subtractive case (e.g., in "IV", when `i` is 'I', `value` is 1, and `prev` was 5. Since 1 \< 5, `output` is reduced by 1).
  - `output -= value`: Subtracts the `value` from the `output`.
- `else:`: If the current `value` is greater than or equal to the `prev` value, it's an additive case.
  - `output += value`: Adds the `value` to the `output`.
  - `prev = value`: Updates `prev` to the current `value`. This `prev` will be used in the next iteration when comparing with the character further to the left.

### Return Value

```python
        return output
```

- After iterating through all characters, `output` will hold the final integer representation of the Roman numeral, which is then returned.

### How the Logic Handles Roman Numerals (Right-to-Left)

This right-to-left approach is very clever for Roman numeral conversion:

1.  **Additive Cases (e.g., "III", "LVIII")**:

    - "III":
      - Process 'I': `value`=1, `prev`=0. `1 < 0` is false. `output` = 1, `prev` = 1.
      - Process 'I': `value`=1, `prev`=1. `1 < 1` is false. `output` = 1+1=2, `prev` = 1.
      - Process 'I': `value`=1, `prev`=1. `1 < 1` is false. `output` = 2+1=3, `prev` = 1.
      - Result: 3.
    - "LVIII":
      - Process 'I': `output`=1, `prev`=1
      - Process 'I': `output`=2, `prev`=1
      - Process 'I': `output`=3, `prev`=1
      - Process 'V': `value`=5, `prev`=1. `5 < 1` is false. `output`=3+5=8, `prev`=5.
      - Process 'L': `value`=50, `prev`=5. `50 < 5` is false. `output`=8+50=58, `prev`=50.
      - Result: 58.

2.  **Subtractive Cases (e.g., "IV", "IX", "MCMXCIV")**:

    - "IV":
      - Process 'V': `value`=5, `prev`=0. `5 < 0` is false. `output`=5, `prev`=5.
      - Process 'I': `value`=1, `prev`=5. `1 < 5` is true. `output`=5-1=4. (No update to `prev` for subtractive cases, which is correct).
      - Result: 4.
    - "MCMXCIV":
      - ... (various additive steps) ...
      - When processing 'X' (from 'XC'): `value`=10, `prev`=100 (from 'C'). `10 < 100` is true. `output` -= 10.
      - When processing 'I' (from 'IV'): `value`=1, `prev`=5 (from 'V'). `1 < 5` is true. `output` -= 1.

### Example Usage (Uncommented)

The example usage you provided correctly demonstrates how to create an instance of the `Solution` class and call the `romanToInt` method with different Roman numeral strings.

```python
# solution = Solution()
# print(solution.romanToInt("III"))  # Output: 3
# print(solution.romanToInt("IV"))   # Output: 4
# print(solution.romanToInt("IX"))   # Output: 9
# print(solution.romanToInt("LVIII"))  # Output: 58
# print(solution.romanToInt("MCMXCIV"))  # Output: 1994 (Your comment says 199, but it's 1994)
# print(solution.romanToInt("XLII"))  # Output: 42
# print(solution.romanToInt("MMXXIII"))  # Output: 2023
# print(solution.romanToInt("CDXLIV"))  # Output: 444
```

**Correction on "MCMXCIV" output**:

- M = 1000
- CM = 900 (1000 - 100)
- XC = 90 (100 - 10)
- IV = 4 (5 - 1)
- Total = 1000 + 900 + 90 + 4 = 1994. Your comment `Output: 199` for "MCMXCIV" is incorrect; it should be `1994`.

Overall, the code is well-structured and efficiently solves the Roman to Integer conversion problem using a common and effective right-to-left parsing strategy. The only minor improvement would be to store integer values directly in the `roman` dictionary.
