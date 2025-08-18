#ips = [i for i in range(21) if i%2==0 ]
#print(ips)
#oeimkd,m

#class Person:
  #  def __init__(self , name , age , city ):
   #     self.name = name
    #    self.age = age
      #  self.city = city
#x1=Person("mhmd" , "25" , "misurata")
   
#print(x1.name , x1.age , x1.city )
 
class BankAccount:

    def __init__(self , name , balance ):
        self.name = name    
        self.balance = balance
    
    def diposit(self , x):
       self.balance += x
       

    def withrow(self , balance , ):
        self.balance -= balance

x1=BankAccount("mhmd" , 1500)
x1.diposit(5000)
x1.withrow(2000)  
print(x1.name ,x1.balance ) 
      
#raise ValueError("")

                
