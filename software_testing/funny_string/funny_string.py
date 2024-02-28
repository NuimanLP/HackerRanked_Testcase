def funny_String(s):
    r=s[::-1]
    s_list = []
    r_list = []
    for i in range(0,len(r)-1):
        s_list.append(abs(ord(s[i])-ord(s[i+1])))  
        r_list.append(abs(ord(r[i])-ord(r[i+1])))
    if s_list == r_list : 
        return 'Funny'
    else:
        return 'Not Funny'