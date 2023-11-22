def pallindrome(s):
    return s == s[::-1]
s=str(input());
ans=pallindrome(s)
if ans:
    print("yes")
else:
    print("not")