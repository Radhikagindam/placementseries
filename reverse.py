n=1234
num=n
result=0
while (num>0):
    ld=num%10 #to extract the ex:4 
    result=result*10+ld  # initial result is 0*10+4=4
    num=num//10 #apart from extracted value ex: 123
print(result) #print result 
