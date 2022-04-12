# def show ():
#     a=[50,40,23,70,56,12,5,12,5,10,7]
#     i=0
#     max=0
#     while i<len(a):
#         if a[i]>max:
#             max=a[i]
#         i=i+1
#     print(max)
# show () 





heights=[4,2,1,10,5,9,7,20,6]
prints=[7,8,3,1,6,2,30,5]
i=0
b=[]
while i<len(heights):
    j=0
    count=0
    while i<len(heights):
        if heights[i]<heights[j]:
            count=count+1
    j=j+1
i=i+1
b.append(count)
print(b)