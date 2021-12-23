# coding: utf-8

"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution1:
    def lengthOfLongestSubstring(self, s: str) -> int:

        candidates, current_substring = set(), ''

        for char in s:
            if char not in current_substring:
                current_substring += char
            else:
                candidates.add(current_substring)

                first_substring, second_substring = current_substring.split(char)
                if first_substring:
                    candidates.add(first_substring + char)
                if second_substring:
                    candidates.add(char + second_substring)

                current_substring = second_substring + char

        candidates.add(current_substring)

        return len(max(candidates, key=len, default=set()))


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seen = {}
        left = output = 0

        for right, char in enumerate(s):
            # char hasn't been seen or is not in the current window: increase the window size
            if char not in seen or seen[char] < left:
                output = max(output, right - left + 1)
            else:
                # char has been seen and is inside the current window: move left pointer to seen[char] + 1
                left = seen[char] + 1

            seen[char] = right

        return output
