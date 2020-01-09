import random
a=[]
b=[]
ak=10
for i in range(0,ak):
    k=random.randint(1,1000)
    a.append(k)
    print(k,end=" ")
print()
b=sorted(a)
for i in b:
    print(i, end=" ")
my = input()
print()
print(b[int(my)-1])
