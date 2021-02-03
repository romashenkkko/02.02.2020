with open ('input.txt', 'r') as f:
    n=str(int(f.readline()))
l1=[str(i) for i in str(n)]
l2=sorted(l1)
if (l1==l2):
    print('ordine crescatoare')
else:
    print('nu sunt in ordine crescatoare')