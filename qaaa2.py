import math
e = float(input(':'))
a = 1
i = 1 
while abs(a) > e:
    a = ((-1)**i * 2**i)/math.factorial(i)
    print(a)
    i+=1
print(i)