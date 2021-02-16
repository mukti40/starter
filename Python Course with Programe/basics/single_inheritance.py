class A:
    a1=100
    def methodA1(self):
        print('this is methodA1 belongs to class A')
    def methodA2(self):
        print('this is methodA2 belongs to class A')
class B(A):
    b1=200
    def methodB1(self):
        print('this is methodB1 belongs to class B')
    def methodB2(self):
        print('this is methodB2 belongs to class B')

ObjB=B()
print(ObjB.b1)
ObjB.methodB1()
ObjB.methodB2()
print(ObjB.a1)
ObjB.methodA1()
ObjB.methodA2()