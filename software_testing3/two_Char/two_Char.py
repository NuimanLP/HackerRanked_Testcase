def permute(s):
    result = []
    hmap = {}
    
    for i in range(len(s)-1):
        for j in range(1, len(s)):
            if i != j and s[i] != s[j]:
                key = f"{s[i]}_{s[j]}"
                if key not in hmap:
                    result.append((s[i], s[j]))
                    hmap[key] = (s[i], s[j])
    return result
    
def alternate(s):
    permutes = permute(s)
    maxLen = 0
    
    for pair in permutes:
        substr = []

        for idx in range(len(s)):
            if s[idx] in pair:
                substr.append(s[idx])
        for j in range(len(substr)-1):
            if substr[j] == substr[j+1]:
                break
        
        if j == len(substr) - 2 and substr[j] != substr[j+1]:
            maxLen = max(maxLen, len(substr))
            
    return maxLen

