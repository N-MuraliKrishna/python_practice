num=1234
res=0
while num!=0:
    rem=num%10
    if num%2==0:
     res=res+rem
    num= num//10
print(res)


num=12321
res=0
dup=num
while num!=0:
    rem=num%10
    res=res*10+rem
    num=num//10
if dup==res:
    print('p')
else:
    print('n')




num=145
copy=num
res=0
while num!=0:
    rem=num%10
    fact=1
    for val in range (1,rem+1):
        fact=fact*val
    res=res+fact
    num=num//10
if res==copy:
    print('strong')
else:
    print('not strong')



num=100
while num>9:
    res=0
    while num!=0:
        rem=num%10
        res=res+rem**2
        num=num//10
    num=res
if num==1 or num==7:
    print ('happy')
else:
    print('not ha')


num=3
for val in range(1,num+1):
    for line in range(1,num+1):
        print('*',end=' ')
    print()


num=5
copy=num
for val in range(num,0,-1):
    for col in range(val,num+1):
        print(col,end='')
    print()



def series(num):
    a=0
    b=1
    print()
    for val in range (num):
        c=a+b
        print(a, end='')
        a,b=b,c
print(list(filter(series,range(1,10))))




num=5
for val in range(1,num+1,1):
    for col in range (val,0,-1):
        print(col,end='')
    print()


num=100
for val in range (1,num+1):
    if num%val==0:
       print(val)



num=100
fact=1
for val in range (1,num+1):
    if num%val==0:
        fact=fact+1
print(fact)

num = 10
while num != 21:
    if num % 2 == 0:
        print(num)
    num += 1

r=input()
res=0
while res!=len(r):
    print(r[res])
    res+=1
