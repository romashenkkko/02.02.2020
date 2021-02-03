x=str(int(input('Numere pare si impare: ')))
p=0
i=0
for k in x:
    if int(k)%2==0:
        p+=1
    if int(k)%2!=0:
        i+=1
print('Numere pare', p)
print('Numere impare', i)