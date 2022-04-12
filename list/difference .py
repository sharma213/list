# list1=[1,2,3,4,5,6]
# list2=[2,3,1,0,6,7]
# i=0
# list3=[]
# while i<len(list1):
#     if list1[i] not in list2:
#         print(list1[i])
#     i=i+1 


a=[12,67,98,415]
sum=0
i=0
while i<len(a):
    k=a[i]%10
    k1=a[i]//10
    k2=a[i]/10
    sum=k+k1
    print(sum,end=" ")
    i=i+1