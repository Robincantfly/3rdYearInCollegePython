import random
min=int(input())
max=int(input())
temp=set()
for i in range(0,8):
    temp.add(random.randint(min,max))
print(temp)
file_handle=open('1.txt',mode='a')
for a in temp:
    file_handle.write('{} '.format(a))
file_handle.write('\n')
file_handle.close()