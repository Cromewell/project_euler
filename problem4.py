#biggest 3digit*3digit palindrome

def is_palindrome(n):
    s = str(n)
    if(len(s)%2==0): #even length
        s1 = s[:int(len(s)/2)]
        s2 = (s[::-1])[:int(len(s)/2)]
        return (s1 == s2)
    else:
        s1 = s[:int((len(s)-1)/2)]
        s2 = (s[::-1])[:int((len(s)-1)/2)]
        return (s1 == s2)
        

def calc_pal():
    max_pal = 0
    for i in range(999, 100-1, -1):
        for j in range(i, 100-1, -1): #start at i to ignore duplicates (i*j=j*i)
            n = i*j
            if(max_pal < n):
                if(is_palindrome(n)):
                    max_pal = n
    return max_pal


print(calc_pal())