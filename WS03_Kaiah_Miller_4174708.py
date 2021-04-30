
def inSet(n, myset):
    for x in myset:
        if x == n:
            return True
    return False
    
def minSet(a):
    myMinSet = []
    for x in a:
        count = 0;
        for y in myMinSet:
            if x == y:
                count = count + 1
        if count == 0:
           myMinSet.append(x)  
         
    return myMinSet
    
def cardinality(a):
   return len(minSet(a))
    
def equalSets(a,b):
    setOne = minSet(a)
    setTwo = minSet(b)
    if len(setOne) != len(setTwo):
        return False
    else:
        for elem in setOne:
            count = 0
            for item in setTwo:
                if elem == item:
                    count = count + 1
            if count > 0:
                continue
            else:
                return False
    return True

#where a is subset of b
def subSet(a,b):
    if equalSets(a,b):
        return True
    seta = minSet(a)
    setb = minSet(b)
    if len(seta) > len(setb):
        return False
    for elem in seta:
        count = 0
        for item in setb:
            if elem == item:
                count = count + 1
    if count == 0:
        return False
    return True
    
def lstfactor(n):
    itr = 1
    factors = []
    while (itr <= n):
        if n % itr == 0:
            factors.append(itr)
        itr = itr + 1
    return factors
    
#question 1a
c = [0,1,2,3]
print("question 1a - in set")
print("is 2, in set", c)
print(inSet(2, c ) )
print("\n")

#question 1b
print("question 1b - minset function")
d = [0,1,2,2,3,6,7]
print("Min set of", d)
print ( minSet(d) )
print("\n")

#question 1c
print("question 1c - cardinality")
print("Cardinality of ", c, "is :")
print( cardinality(c) )
print("\n")

#question 1d
print("question 1d - equal sets")
print("Are set ", c, "and set", d, "equal?")
print( equalSets(c,d))
print("\n")

#question 1e
print("question 1d - subset")
print("Is set ", c, "a  subset of ", d)
print( subSet(c,d))
print("\n")
#question2 
print("question 2")
U = [41,42,43,44,45,46,47,48,49,50]
A = [41,43,45,47,49]
print("Using set U = ", U)
print("\n")
#question2a
# set where x is a multiple of 3
print("question 2a - subset of U where x is a multiple of 3")
B = []
for x in U:
    if x % 3 == 0:
        B.append(x)
print(B)
print("\n")

#question2b
# set where x is a prime number
print("question 2b - subset of U where x is a prime number")
C = []
for x in U:
    if len(lstfactor(x)) == 2:
        C.append(x)
print(C)
print("\n")   

#question2c
# set where x is a prime number
print("question 2c - set of A intersect C")
print("set A : ", A)
print("set C : ", C)
aic = []
for x in A:
    for y in C:
        if x == y:
            aic.append(x)
print(aic)
print("\n")

#question2d
print("question 2d - set of B union C, complment")
print("set B : ", B)
print("set C : ", C)
buc = []
#union opperation first
buc = B + C
#complment opperation 
result = []
for x in U:
    if inSet(x, buc) == False:
        result.append(x)
print(result)
print("\n")

#question2e
print("question 2e - set of A union C, \B")
print("set A : ", A)
print("set C : ", C)
auc = []
#union opperation first
auc = B + C
#complment opperation 
result = []
for x in B:
    if inSet(x, buc) == False:
        result.append(x)
print(result)
print("\n")


#question2f
print("question 2e - set of A union B union C, complment")
print("set A : ", A)
print("set C : ", C)
auc = []
#union opperation first
aubuc = A + B + C
#complment opperation 
result = []
for x in U:
    if inSet(x, aubuc) == False:
        result.append(x)
print(result)
print("\n")

#question 3a
print("question 3a - lstfactor(n) function")
print ( "factors of 4", lstfactor(4))
print ("factors of 7", lstfactor(7))
print ("factors of 16", lstfactor(16))

#question 3b

#create set U first
U =[]
i = 0 
j = 20
m = []
n = []
p = []
mnp = []
while i <= j:
    U.append(i)
    i +=1
for x in U:
    if len(lstfactor(x)) == 2:
        m.append(x)
    if len(lstfactor(x)) == 3:
        n.append(x)
    if len(lstfactor(x)) == 4:
        p.append(x)
print("m integers have exactly 2 positive factors : ", m)
print("n integers have exactly 3 positive factors : ", n)
print("p integers have exactly 4 positive factors : ", p)
mnp = m + n + p 
print("Union m, n, p :", mnp)
resultSum = 0 
for x in mnp:
    resultSum += x 
print("Sum of the values x in set mnp : ", resultSum)

