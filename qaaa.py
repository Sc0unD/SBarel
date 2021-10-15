n = int(input(':'))
s=0
d=0
while n > 0:
    a = n%10
    n = n//10
    s = s + a
print(s)
for i in range(2,s):
    for j in range(2,i):
        if s%i == 0 and i%j != 0:
            d = i
print(d)  