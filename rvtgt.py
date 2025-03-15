def king(height):
    for i in range (height):
        for j in range (height):
            if j==0 or j==height -1 or j==i:
                print('*',end='')
            else:
                print(' ',end='')
        print()
height=7
print(king(height))

import re
s='adcdef@gmail.com'
if (re.match('^[a-z A-Z 0-9 ._-]+@gmail.com$',s)and('..' not in s)and('__' not in s) and('--' not in s)):
    print('valid')


s=['wrali','prishna','z','yeddy']
for val in range(len(s)-1):
    for ind in range(len(s)-1-val):
        if s[ind]>s[ind+1]:
            s[ind],s[ind+1]=s[ind+1],s[ind]
print(s)

import calendar
yy=2002
mm=7
print(calendar.month(yy,mm))


t=[12,23,45,67,79]
itobj=iter(t)
print(next(itobj))

class seq():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __iter__(self):
        return self
    def __next__(self):
        val=self.num1
        self.num1+=1
        return val
start=11
end=14
obj=seq(start,end)
itob=iter(obj)
print(itob)
print(next(itob))
print(next(itob))
print(next(itob))
print(next(itob))
print(next(itob))
print(next(itob))

class serial():
    def __init__(self,num1,num2):
        self.num1=num1
        self.num2=num2
    def __iter__(self):
        return self
    def __next__(self):
        val = self.num1
        if val>self.num2:
            raise StopIteration
        self.num1+=1
        return val
start=11
end=14
obj=serial(start,end)
itob=iter(obj)
while  True:
    try:
      print(next(itob))
    except StopIteration:
        print('error')
        break

num=9
try:
    for val in range(2,num//2+1):
        if num%val==0:
            raise Exception
except:
    print('not prime number')
else:
    print('prime nummber')
finally:
    print('no exception')


num=8
try:
    assert num%2!=0,'even'
except AssertionError as msg:
    print(f'msg={msg}')
else:
    print('0dd number')

s='racecar'
res=0
while res!=len(s)//2:
    if s[res]!=s[-res-1]:
        print('not palindrone')
        break
    res=res+1
else:
    print('palindrone')


num=4
spaces=num-1
for i in range(1,num+1):
    for sp in range (spaces):
        print(" ",end='')
    num=i
    step=2
    for j in range(i):
        print(num,end='')
        num=num+step
    num-=step
    for j in range(i-1):
        num-=step
        print(num,end='')
    print()
    spaces=spaces-1

s='harah'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        if s[sv:ev]== s[sv:ev][::-1]:
            print(s[sv:ev])


s='wararra'
res=''
for va in range(len(s)):
    for ch in range(len(s)-1-va):
        if s[ch] not in res :
            res=res+ch
        else:
            print(ch)

import re
if (re.match('^[a-zA-Z0-9-.-]+@gmail[.]com$',s) and ('--' not in s) and ('__' not in s) and ('..' not in s)):
 print('valid')











