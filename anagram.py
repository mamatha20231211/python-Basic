t=int(input())
if 1<=t<=100:
    for i in range(t):
        str1,str2=map(str,input().split())
        if sorted(str1)==sorted(str2):
            print("anagram")
        else:
            print("not anagram")
else:
    print("invalid input")
