# 3. Longest Substring Without Repeating Characters
# Medium

# Given a string s, find the length of the longest substring without repeating characters.

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0

        len_sub = 1

        for i in range(len(s)):
            elems = set(s[i:i+len_sub])
            if len(elems) < len_sub:
                continue

            for j in range(len_sub , len(s) - i):
                new_elem = s[i+j]

                if new_elem in elems:
                    break
                else:
                    elems.add(new_elem)
                    len_sub += 1

        return len_sub
