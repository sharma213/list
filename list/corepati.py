a = [3000, 600000, 324990909, 90990900, 30000, 5600000, 690909090, 31010101, 532010, 510,4100]
i=0
c1=0
c2=0
c3=0
while i<len(a):
    if a[i]>10000000:
        c1=c1+1
        # i=i+1
    elif a[i]>100000:
        c2= c2+1
    else:
        c3=c3+1
    i=i+1
print("corepati",c1)
print("lakhpati",c2)
print("diwale",c3)


       