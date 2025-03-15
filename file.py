fobj=open('file1.txt','r')
count=0
for var in fobj:
    l=var.split()
    for sp in l:
      count=count+1
print(count)


fobj=open('file1.txt','r')
res=''
count=0
for line in fobj:
    l=line.strip('\n')
    for ch in l:
        if ('a'<=ch<='z') or ('A'<=ch<='z'):
            res=res+ch
            count=count+1
print(res)
print(count)



fobj=open('file1.txt','r')
res=''
count=0
for line in fobj:
    l=line.strip('\n')
    for ch in l:
        if ch in ('a','e','i','o','u'):
            res=res+ch
            count=count+1
print(res)
print(count)



s='Lofer'
res=''
for ch in s:
    if 'A'<=ch<='Z':
        res+=chr(ord(ch)+32)
    else:
        res+=chr(ord(ch)-32)
print(res)


num=5
spaces=num//2
stars=1
for row in range(1,num+1):
    for sp in range(spaces):
        print(' ',end='')
    for line in range(1,stars+1):
        print('*',end='')
    print()
    if row<num//2+1:
        stars+=1
        spaces-=1
    else:
        stars-=1
        spaces+=1



