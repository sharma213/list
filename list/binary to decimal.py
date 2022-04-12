number = [1, 0, 0, 1, 1, 0, 1, 1]
i=len(number)-1
decimal=0
c=1
while i>=0:
       decimal=decimal+number[i]/c
       c=c/2
       i=i-1
print(decimal)



# i=0
# while i<5:
# #      i=i+1
#      print(i)
#      if i==3:
#        break
      #  i=i+1
       

# i=0
# while i<=5:
#       i=i+1
#       if i==3:
#         continue
#       print(i)


# i=10
# while i>=-10:
      # print(i)
      # i=i-1



# list=[1,2,3,4]
# counter=0
# while list[counter:]:
#      counter=counter+1
# print(counter)


# a=[0,[1,2,3,4,[8,9,10],11,13,[14]]]
# print (a[0])
# print(a[1][7][0])

# a=[1,2,3,4,5,6,8]
# b=[3,4,5,6,7,8,7]
# i=0
# c=[]
# while i<=len(a):
#       if a[i] not in b:
#             c.append(a[i])
#       i=i+1
# print(c)
  
# a=["a","b"]
# i=0
# while i<len(a):
#       num=int(input("enter your number"))
#       a=a[i]*int (num)
#       print(a)
#       i=i+1