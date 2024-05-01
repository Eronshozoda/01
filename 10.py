num=input()
ben=len(num)
binar=0
cnt=0
res=0
for i in range(ben):
    binar=int(num)%10
    res=int(res)+binar*2**cnt
    cnt+=1
    num=int(num)//10
print(res)