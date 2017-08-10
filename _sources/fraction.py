class Fraction:

    def __init__(self,top,bottom):

        self.num = top        #the numerator is on top
        self.den = bottom     #the denominator is on the bottom


    def __repr__(self):
        if self.num > self.den:
            retWhole = self.num / self.den
            retNum = self.num - (retWhole * self.den)
            return str(retWhole) + " " + str(retNum)+"/"+str(self.den)
        else:
            return str(self.num)+"/"+str(self.den)

    def show(self):
        print self.num,"/",self.den

    def __add__(self,otherfraction):
        # convert to a fraction
        otherfraction = self.toFract(otherfraction)

        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum,newden)

        return Fraction(newnum/common,newden/common)

    def __radd__(self,leftNum):
        otherfraction = self.toFract(leftNum)            
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den

        common = gcd(newnum,newden)

        return Fraction(newnum/common,newden/common)

    def __cmp__(self,otherfraction):

        num1 = self.num*otherfraction.den 
        num2 = self.den*otherfraction.num

        if num1 < num2:
           return -1
        else:
           if num1 == num2:
              return 0
           else:
              return 1

    def toFract(self,n):
        if isinstance(n,int):
            otherfraction = Fraction(n,1)
        elif isinstance(n, float):
            wholePart = int(n)
            fracPart = n - wholePart
            # convert to 100ths???
            fracNum = int(fracPart * 100)
            newNum = wholePart * 100 + fracNum
            otherfraction = Fraction(newNum,100)
        elif isinstance(n,Fraction):
            otherfraction = n
        else:
            print "Error: cannot add a fraction to a ", type(n)
            return None
        return otherfraction

#gcd is a helper function for Fraction

def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn

    return n
