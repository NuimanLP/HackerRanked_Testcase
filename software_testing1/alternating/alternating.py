def alternatingChar(s):
    ans = []
    for i in range(0, len(s)-1):
        if s[i] == s[i+1]:
            ans.append(s[i])
    num = len(ans)
    return f'{num}'