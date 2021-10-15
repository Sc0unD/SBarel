a = int(input('A: '))
b = int(input('B: '))

chisla=[]
for n in range(a,b+1):
    delitili=[]
    s=0
    for i in range(1,b+1):
        if n%i == 0:
            delitili.append(i)
    for i in delitili: 
        s+=i        
    if s%2 == 0:
        chisla.append(n)

print(chisla)





