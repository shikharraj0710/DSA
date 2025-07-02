def solution(s):
    seen = {}
    max_len = 0
    start = 0

    for i in range(len(s)):
        if s[i] in seen and seen[s[i]] >= start:
            start = seen[s[i]] + 1
        seen[s[i]] = i
        max_len = max(max_len, i - start + 1)

    return max_len

print(solution("abcabcbb"))









