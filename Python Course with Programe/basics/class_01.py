class employee:
    loc="Hyderabad"                     #class variable
    def __init__(self,Empno,Ename,Sal):
        self.Empno=Empno                #instance variable
        self.Ename=Ename                #instance variable
        self.Sal=Sal                    #instance variable
    def display(self):
        print("Emp number is ",self.Empno)
        print("Emp name is ",self.Ename)
        print("Emp Salary is ",self.Sal)
        print ("Emp Location is ",employee.loc)
        
emp1=employee(101,"Sai",10000)
emp1.display()
emp2=employee(102,"Nani",20000)
emp2.display()
emp3=employee(103,"Renu",30000)
emp3.display()