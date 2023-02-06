class Base:
    def cal_sum(self,a,b):
        return a+b
class Derived(Base):
    def cal_mul(self,a,b):
        return a * b

n1 = int(input("Enter 1st No. : "))
n2 = int(input("Enter 2st No. : "))

d = Derived()

print("(from base class) Addition is : ",d.cal_sum(n1,n2))
print("(from derived class) Multiplication is : ",d.cal_mul(n1,n2))