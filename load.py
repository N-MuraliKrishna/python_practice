import json
with open ('details.json','r')as fobj:
    data=fobj.read()
    pd=json.loads(data)
    print(pd)

import json
with open('details.json','r')as fobj:
    pd=json.load(fobj)
    print(pd)

num=5
copy=num
for line in range(num,0,-1):
    for col in range(line):
        print(line,end='')
    print()
    copy-=1


num=4
spaces=num-1
for val in range(1,num*2+1,2):
    for sp in range (spaces):
        print(" ",end='')
    for line in range (val,0,-1):
        print(line,end='')
    print()
    spaces-=1


def series(num):
    a=0
    b=1
    print()
    for val in range(num):
        print(a,end='')
        c=a+b
        a, b = b, c
print(list(filter(series,range(1,10))))


def function(**kwargs):
    print(kwargs)
function(a=1,b=2,c=3)


s='murali'
res=s[::-1]
print(res)


s='murali'
res=''
for ch in s:
    if ch in 'aeiouAEIOU':
        res=res+ch
print(res)


m='saiVENKa'
res=''
for ch in m:
    if 'A'<=ch<='Z':
        res=res+ch
print(res)


n='@$_murali'
res=''
for ch in n:
    if ch.isalnum()==False:
        res=res+ch
print(res)

def function(num,fact=1):
    yield 1
    for val in range (1,num+1):
        fact=fact*val
        yield val
obj=function(5)
for ind in obj:
    print(ind)


import re
s='murali123@gmail.com'
if (re.match('^[a-zA-Z0-9-.-]+@gmail[.]com$',s) and ('--' not in s) and ('__' not in s) and ('..' not in s)):
    print('valid')


class car():
    name='murali'
    def __init__(self):
        self.age=24
        self.gender='male'
        self.qualifiation='b-tech'
c1=car()
print(c1.age)
