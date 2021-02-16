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

class C(A):
    c1=300
    def methodC1(self):
        print('this is methodC1 belongs to class C')
    def methodC2(self):
        print('this is methodC2 belongs to class C')

class D(A):
    d1=400
    def methodD1(self):
        print('this is methodD1 belongs to class D')
    def methodD2(self):
        print('this is methodD2 belongs to class D')

ObjD=D()
print(ObjD.d1)
ObjD.methodD1()
ObjD.methodD2()

print(ObjD.a1)
ObjD.methodA1()
ObjD.methodA2()

ObjC=C()
print(ObjC.c1)
ObjC.methodC1()
ObjC.methodC2()

print(ObjC.a1)
ObjC.methodA1()
ObjC.methodA2()

ObjB=B()
print(ObjB.b1)
ObjB.methodB1()
ObjB.methodB2()

print(ObjB.a1)
ObjB.methodA1()
ObjB.methodA2()