class monday():
    def __init__(self):
        self.var1=90
    def method(self):
        print(self.var1)
obj=monday()
print(obj.var1)
obj.method()

class tuesday():
    def __init__(self):
        self._var2=79
    def method(self):
        print(self._var2)
obj=tuesday()
obj.method()
print(obj._var2)


class wednesday():
    def __init__(self):
        self.__var3=19
    def method(self):
        print(self.__var3)
    def getter(self):
        return self.__var3
    def setter(self):
        self.__var3=90
obj=wednesday()
obj.method()
print(obj.getter())
obj.setter()
print(obj.getter())

class friday():
    def add(self,v1,v2):
        print(v1+v2)
    def add(self,v1,v2,v3):
        print (v1+v2+v3)
obj=friday()
obj.add(1,7,9)


class thursday():
    def add(self,*args):
        count=0
        for va in args:
            count+=va
        print(count)
obj=thursday()
obj.add(1,2,3)

class saturday():
    def add(self,v1=0,v2=0,v3=0,v4=0):
        print(v1+v2 +v3+ v4)
obj=saturday()
obj.add(1,2,3)


from abc import ABC,abstractmethod
class re(ABC):
    @abstractmethod
    def engine(self):
        pass
    def gears(self):
        print('5gears')
class gt(re):
    def engine(self):
      print('350cc')
class himalayan(re):




