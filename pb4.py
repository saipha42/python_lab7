
class QuadraticEquation:

    def __init__(self, a, b, c) :
        self.__a = a
        self.__b = b
        self.__c = c
    

    def get_a(self) :
        return self.__a

    def get_b(self) :
        return self.__b
    def get_c(self) :
        return self.__c
    
    def getDiscriminant(self) :
        return (self.__b **2) - (4* self.__a * self.__c)
    
    def getRoot1(self) :

        if self.getDiscriminant() < 0 :
            return 0
        r1 = ( (-self.__b) + ( self.getDiscriminant() )**0.5 )/(2* self.__a)
        return r1
    def getRoot2(self) :

        if self.getDiscriminant() < 0 :
            return 0
        r2 = ( (-self.__b) - ( self.getDiscriminant() )**0.5 )/(2* self.__a)
        return r2



eq1 = QuadraticEquation(1,5,3)
res1 = eq1.getDiscriminant()

res1= eq1.getRoot1()
print(res1)

print(eq1.getRoot2())
