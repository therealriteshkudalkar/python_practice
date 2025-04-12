
class Solution:
    @staticmethod
    def is_palindrome(s: str) -> bool:
        left = 0
        right = len(s) - 1

        while left < right:
            # Find a valid alphanumeric character from the left
            while not s[left].isalnum() and left < len(s) - 1:
                left += 1
            while not s[right].isalnum() and right > 0:
                right -= 1
            # Find a valid alphanumeric character from the right
            if left < right and s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1

        return True
