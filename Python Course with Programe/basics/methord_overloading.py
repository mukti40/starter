class classA:
    def method1(self):
        print('this method belongs to class classA')

class classB:
    def method1(self,a):
        print('this method belongs to class classB')

ObjB=classB()
ObjB.method1(10)
#ObjB.method1()        #it will return error so overloading will not support