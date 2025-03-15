s='hello world bye world'
l=[]
a=''
for val in range (len(s)-1,-1,-1):
    if s[val]!=' ':
        a=s[val]+a
    else:
        l.append(a)
        a=''
l.append(a)
print(l)



m='racecar'
for val in range(len(m)//2):
    if m[val]!=m[-val-1]:
        print('not palindrone')
        break
else:
    print('palindrone')


s='hello world'
l=s.split()
a=[]
for val in range(len(l)):
    b=l[val]
    a.append(b[::-1])
    c=' '.join(a)
print(c)





s='engineering'
print({ch:s.count(ch) for ch in s})


h='happy'
for val in range(len(h)):
    for ind in range(val+1,len(h)+1):
       print(h[val:ind])
    




j='punidha'
res=''
for val in range(len(j)):
     res=res+j[val]
     print(res)



num=5
spaces=0
for ev in range (num,-1,-1):
    for sp in range(spaces):
        print(' ',end='')
    for col in range(ev,0,-1):
        print(col,end='')
    print()
    spaces+=1


n=5
spaces=n//2
stars=1
for row in range(1,n+1):
    for sp in range(spaces):
        print(' ',end='')
    for line in range(1,stars+1):
        print('*',end='')
    print()
    if row<n//2+1:
        stars+=1
        spaces-=1
    else:
        stars-=1
        spaces+=1


def binary(num,mul=1):
    if num==0:
        return 0
    return(num%10*mul)+binary(num//10,mul*2)
num=1010
print(binary(num))


def integer(n,pos=1):
    if n==0:
        return 0
    return (n%2*pos)+integer(n//2,pos*10)
num=10
print(integer(num))

print(bin(10))

def sqt(values):
    if values==0:
        return 0
    return(values%10)**2+sqt(values//10)
def happy(num):
    if num<10:
        return num==1 or num==7
    return happy(sqt(num))
num=13
print('happy num'if happy(num) else'not happy num')

num=19
while num>9:
    res=0
    while num!=0:
        rem=num%10
        res=res+rem**2
        num=num//10
    num=res
if num==1 or num==7:
    print('happy')
else:
    print('not ha')


s='happy'
for sv in range(len(s)):
    for ev in range(sv+1,len(s)+1):
        word=(s[sv:ev])
        if word==word[ : :-1]:
            print(word)

s='MuraliKRISHNA'
res=''
for ch in s :
    if 'a'<=ch<='z':
        res=res+chr(ord(ch)-32)
    else:
        res=res+ch
print(res)


l=[10,80,90,70]
for ind in range(len(l)-1):
    for ind2 in range(len(l)-1-ind):
        if l[ind2]>l[ind2+1]:
            l[ind2],l[ind2+1]=l[ind2+1],l[ind2]
print(l)

s=[80,90,60,10]
for ind1 in range(len(s)-1):
    li=ind1
    for ind2 in range(ind+1,len(s)):
        if s[li]>s[ind2]:
            li=ind2
    s[li],s[ind1]=s[ind1],s[li]
print(s)


def quick(m):
    if len(m)<=1:
        return m
    pivot=m[0]
    left=[val for val in m[1:] if pivot>val]
    riht=[val for val in m[1:] if pivot<=val]
    return quick(left)+[pivot]+quick(riht)
m=[50,-1,40,10]
print(quick(m))
















