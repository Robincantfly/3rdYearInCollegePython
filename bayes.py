#有有10种可能，那我建立att2=[10*att1],用于存放att1
att2=[[0.0 for x in range(0,2*2)] for x in range(0,2)]
# a b c
c=[
[0, 0, 0], [0, 0, 1 ],

[0, 0, 0], [0, 0, 1],

[1, 1, 0], [1, 0, 1],

[1, 1, 0], [1, 1, 1]]
for i in range(0,8):
    for j in range(0,2):
        res=int(c[i][2])
        if c[i][j]==0:
            att2[res][2*j]+=1
        else:
            att2[res][2*j+1]+=1
print(att2)