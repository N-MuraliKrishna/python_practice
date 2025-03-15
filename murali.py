class car:
    name="bmw"
    def __init__(self,color,model,power,engine,price):
      self.color=color
      self.model=model
      self.power=power
      self.engine=engine
      self.price=price
    def car_details(self):
          print(f''' 
             name:{self.name}
             color:{self.color}
             model:{self.model}
             power:{self.power}
             engine:{self.engine}
             price:{self.price}
    ''')
p1=car('white','m5',536,'v6','1 crp')
car.car_details(p1)
print(p1.model)



s="helo world"
l=s.split()
a=[]
for val in range(len(l)):
    b=l[val]
    a.append(b[::-1])
    c=' '.join(a)
print(c)


s='happy'
for sv in range(len(s)):
    for ev in range(sv+1,6):
        print(s[sv:ev])


s='engineering'
print({ch:s.count(ch) for ch in s})



s='racecar'
for val in range(len(s)//2):
    if s[val]!=s[-val-1]:
        print(' not palindrone')
        break
else:
   print(' palindrone')



def prime(num):
    for den in range(2,num//2+1):
        if num%den==0:
            return False
    return True
print(list(filter(prime,range(100,200))))



def armstrong(num,power,res=0):
    while num!=0:
        rem=num%10
        res=res+rem**power
        num=num//10
    return res
num=153
print('armstrong'if armstrong(num,len(str(num)))==num else 'not arm')



def armstrong(num,res=0):
    power=len(str(num))
    dup=num
    while num!=0:
        rem=num%10
        res=res+rem**power
        num=num//10
    if res==dup:
        print( 'armstrong')
    else:
        print('not arm')
num=153



















