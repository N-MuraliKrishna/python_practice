class sbi:
    roi=0.07
    def __init__(self,name,mbno,aadhar,pan,gender,bal):
        self.name=name
        self.mbno=mbno
        self.aadhar=aadhar
        self.pan=pan
        self.gender=gender
        self.bal=bal
    def display(self):
        print(f''' 
                 name={self.name}
                 mbno={self.mbno}
                 aadhar={self.aadhar}
                 pan={self.pan}
                 gender={self.gender}
                 bal={self.bal}''')
    def withdraw(self):
        amount=int(input('enter the amounnt to withdraw '))
        if self.bal>=amount:
           self.bal-=amount
           print('amount debited successfully')
           print(f'available bal is {self.bal}')
        else:
            print('insufficient funds')
    def deposite(self):
        amount=int(input('enter the amount to deposite'))
        self.bal+=amount
        print('amount is deposited')
        print(f'available balance is {self.bal}')
cust1=sbi('raju',1234567891,123456789123,'abcd123','male',10000)
print(cust1.display())
print(sbi.roi)
cust1.withdraw()
cust1.deposite()
cust1.aadhar=45678910
print(cust1.display())








