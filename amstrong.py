n=153
num=n
total=0
lod=len(str(n))
while num>0:
    id=num%10
    total=total+(id**lod)
    num=num//10
print(n==total)
