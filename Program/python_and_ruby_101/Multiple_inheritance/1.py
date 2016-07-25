class C1():
    def c1_m(self):
        print("c1_m")
    def m(self):
        print("C1 m")

class C2():
    def c2_m(self):
        print("c2_m")
    def m(self):
        print("C2 m")

#다중상속 인자로 여러개 받음
class C3(C1, C2):
    pass

c = C3()
c.c1_m()
c.c2_m()
c.m()
print(C3.__mro__)
