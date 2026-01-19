from collections import Counter

def find_anagram_indices(s, p):


    need = Counter(p)
    window = Counter()
    result = []
    m = len(p)

    for i in range(len(s)):
        window[s[i]] += 1

        if i >= m:
            if window[s[i - m]] == 1:
                del window[s[i - m]]
            else:
                window[s[i - m]] -= 1

        if window == need:
            result.append(i - m + 1)

    return result
print(find_anagram_indices("cbaebabacd", "abc"))


