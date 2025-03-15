a=25
b=30
c=67
if a > b and a > c or b > c and b > a or c > a and c >b:
    print(a,b,c)

s=int(input('enter integer'))
res=0
while s!=0:
    rem=s%10
    res=res+rem
    s=s//10
print(res)



num=5
for val in range(1,num+1):
    print(val*2,end=' ')

a = list(map(int,input().split()))
target = int(input())
low = 0
high = len(a)-1
while low <= high:
    mid = (low+high)//2
    if a[mid] < target:
        low = mid + 1
    elif a[mid] > target:
        high = mid -1
    elif a[mid] == target:
        print(a[mid])
        break
else:
    print(-1)