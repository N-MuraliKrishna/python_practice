def prime(num):
    for den in range(2,num//2+1):
        if num%den==0:
            return 'np'
    return "p"
print(list(map(prime,range(10,20))))

print(list(map(lambda num:'even'if num%2==0 else 'odd',range(10,20))))


num=22
pos=1
res=0
while num!=0:
    rem=num%2
    res=res+rem*pos
    pos=pos*10
    num=num//2
print(res)



num=101
pos=1
res=0
while num!=0:
    rem=num%10
    res=res+rem*pos
    pos=pos*2
    num=num//10
print(res)


def happy(num,res=0):
    while num >9:
        while num !=0:
            rem=num%10
            res=res+rem**2
            num=num//10
        num==res
    if num==1 or num==7:
        return(True)
print(list(filter(happy,range(100,200))))

num=100
ms=num
while num >9:
    res=0
    while num !=0:
        rem =num%10
        res=res+rem**2
        num=num//10
    num==res
if num==1 or num ==7 :
    print(f'{ms} is a happy number')
else:
    print(f'{ms} is not happy number')



m = 'world'
res=""
for ch in m:
    res=ch+res
print(res);





s='murali'
res=''
for ind in range (-1,-(len(s)+1),-1):
    res=res+s[ind]
print(res)





p='lofer'
res=''
for ind in range (len(p)-1,-1,-1):
    res=res+p[ind]
print(res)




a=10
b=20
a=a+b
b=a-b
a=a-b
print(a,b)



a=10
b=20
a,b=b,a
print(a,b)


a=20
b=90
c=a
a=b
b=c
print(a,b)



num1=8
num2=9
num1=num1*num2
num2=num1//num2
num1=num1//num2
print(num1,num2)


num=5
for val in range(1,11,1):
    print(f'{num}*{val}={num*val}')

num=7
if bin(num)[-1]=='1':
    print('odd')
else:
    print('even')


num=int(input('enter a num'))
sum=0
for val in range(1,num):
    if num%val==0:
        sum=sum+val
if sum==num:
    print('p')
else :
    print('na')


num=5
spaces=0
for ev in range(4,-1,-1):
    for sp in range(spaces):
        print(' ',end='')
    for val in range(num,ev,-1):
        print(val,end='')
    print()
    spaces-=1



num=5
for ev in range(num-1,-1,-1):
    for line in range(5,ev,-1):
        print(line,end=' ')
    print()







































