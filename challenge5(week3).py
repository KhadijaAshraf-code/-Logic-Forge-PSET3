def longest_palindromic_substring(s):
    n = len(s)
    longest = ""

    def expand(l, r):
        while l >= 0 and r < n and s[l] == s[r]:
            l -= 1
            r += 1
        return s[l + 1:r]

    for i in range(n):
        odd = expand(i, i)
        even = expand(i, i + 1)
        longest = max(longest, odd, even, key=len)

    return longest
print(longest_palindromic_substring("babad"))



