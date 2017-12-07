#!/usr/bin/env python

num=498860100962
even=0
odd=0

for i in range(0, len(str(num))):
    if(i%2==0):
        odd+= int(num/(10**i))%10
        # print("odd:", odd)
    else:
        even+= int(num/(10**i))%10
        # print("even:", even)

odd*=3
ans=10-((odd+even)%10)

print("Check-Degit:", " \t", ans)
print("JAN-Code:", " \t", str(num)+str(ans))
