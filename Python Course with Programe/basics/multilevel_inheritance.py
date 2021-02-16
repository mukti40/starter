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

class C(B):
    c1=300
    def methodC1(self):
        print('this is methodC1 belongs to class C')
    def methodC2(self):
        print('this is methodC2 belongs to class C')

class D(C):
    d1=400
    def methodD1(self):
        print('this is methodD1 belongs to class D')
    def methodD2(self):
        print('this is methodD2 belongs to class D')

ObjD=D()
print(ObjD.d1)
ObjD.methodD1()
ObjD.methodD2()

print(ObjD.c1)
ObjD.methodC1()
ObjD.methodC2()

print(ObjD.b1)
ObjD.methodB1()
ObjD.methodB2()

print(ObjD.a1)
ObjD.methodA1()
ObjD.methodA2()