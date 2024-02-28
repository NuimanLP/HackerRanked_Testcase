def caesarCipher(s, k):
    text_low = 'abcdefghijklmnopqrstuvwxyz'
    text_up = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    after = ''
    for i in s:
        if i.isalpha():
            if i.islower():
                num = text_low.index(i)
                after +=  text_low[(num+k)%26]
                
            if i.isupper() :
                num = text_up.index(i)
                after +=  text_up[(num+k)%26]
        else:
            after += i
    return after

print(caesarCipher('Chavatik Thorarit', 4)) # PknG