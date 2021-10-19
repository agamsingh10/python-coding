s=input()
a=[]
for i in s:
    a.append(i)

a.reverse()

listToStr = ''.join(map(str, a))
if(s== listToStr):
    print("Pallindrome")
    
else:
    print("Not a Pallindrome")


