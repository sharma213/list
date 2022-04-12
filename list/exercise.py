# # Remove duplicates from a list.
# List = [1,2,3,1,2,2]
# # Output: [1,2,3]
# b=[]
# i=0
# while i<len(List):
#     if List[i] not in b:
#        b.append(List[i])
#     i=i+1
# print(b)



# Our task is to print the element which occurs 3 consecutive times in a Python list.
# Example:
# Input: [4, 5, 5, 5, 3, 8]
# Output: 5
# Input: [1, 1, 1, 64, 23, 64, 22, 22, 22]
# Output: 1, 22

# a=[[1,2,3,],[4,5,6,]]
# i=0
# new=[]
# whie i<len (a):
#     j=0
#     while j<len (a[i]):
#         if i==0:
#             sum=sum+a[i][j]
#         elif i==1 :
#             mul=mul*a[i][j]
#         j+=1
#     i+=1
# print(sum)
# print(mul)
# name=["a","b","c","d"]
# Rollno=[4,3,2,1]
# i=0
# # while i<len(name):
    # j=0/
#     # while j<len(Rollno):
#         print(name[i])
    # j=j+1
# i=i+1
# name=["a","b","c","d"]
# rollno=[4,3,2,1]
# i=0
# while i<len(name):
#     print(name[i],rollno[-i-1])
#     i=i+1

# a=[[2,4,6,8],4,[9,2,3,7,10],11]
# i=0
# sum=0
# sum1=0
# count=0
# count1=0
# while i<len(a):
#     j=0 
#     while j<len(a[i]):
#       if a[i]%2==0:
#         count=count+1
#         sum=sum+a[i][j]
#       else:
#         count1=count1+1
#         sum1=sum1+a[i][j]
#         j=j+1   
#     i=i+1
#     print(count,"even",sum)
#     print(count1,"odd",sum1)


# a=[[1,2,[4,5,8],10,15,[7,8,[4,10,15],20]]]
# a1=0
# b=[]
# while a1<len(a):
#     a[0][1].append.b
#     print(b)
# list = [["a"], ["b", "c"], ["d", "e", "f", "g"]]
# list=[[1,2,[4,5,8],10,15,[7,8,[4,10,15],20]]]
# one_list = [num for sublist in list for num in sublist]
# print(one_list)
# no=[4,7,2,3]
# name=["ansh","navya","nikita","pooja"]
# i=0
# while i<len(no):
#      print(no[i]* name[i])
#      i=i+1
# list=[2,3,[5,6,8,[2,3],6],8,9]
# print (list[1])
# print (list[2][0])
# print (list[2][3][0])
# print (list[2][4])
# print (list[3])

# list=[18,[2,3,4,],14,15,[6,11,18],1,9,[25,10,6]]
# print (list [1][0])
# print (list[3])
# print (list [4][2])
# print (list[6])
# print (list [7][1])
# List=[[[2,4,5,],[9,8,[48,7,6],40,7]]]
# print (List[0][0][1])
# print (List [1][1])
# print (List [1][2][3])
# print (List [1][3])





# list1=[[8,10,9],[2,5,4],[11,20,21]]
# i=0
# while i<len(list1):
#     j=0
#     max=0
#     while j<len(list1[i]):
#         if list1[i][j]>max:
#             max=list1[i][j]
#         j=j+1
#     print(max)
#     i=i+1



# sum=0
# number=1
# while number >0:
#     number=int(input("enter your number"))
#     if number>0:
#        sum=sum+number
# print("the sum of the number is",sum)



# num=int(input("enter your number"))
# num1=int(input("enter your number"))
# i=0
# sum=0
# while i<num:
#     j=0
#     while j<num1:
#         sum=num +num1
#         j=j+1
#     i=i+1

# print(sum)




# i=0
# sum=0
# while i<10:
#     num=int(input ("enter num
#     sum=sum+num
#     i=i+1
# print(sum)


# a="p","q"
# b=[1,2,3,4,5]
# i=0
# while i<len(b):
#     print(a+str(b[i]))
#     i=i+1

# a=["a","b"]
# n=int(input("enter your number"))
# i=1
# while i<=n:
#     j=0
#     while j<len(a):
#         print(a[j]+str(i))
#         j=j+1
#     i=i+1
# def compare_lists(llist1, llist2):
#     def compare_lists():
#     llist1=[1,2,3,4]
#     llist2=[1,2,3,4]
#     i=0
#     while i<len(llist1):
#         if llist1[i]==llist2[i]:
#             return 1
#         elif llist1!=llist2:
#             return 0
#         i=i+1
# print(compare_lists())
def compare_lists():
    def compare_lists():
        llist1=[1,2,3,4]
        llist2=[1,2,3,4]
        i=0
        while i<len(llist1):
            if llist1[i]==llist2[i]:
                return 1
            else:
                return 0
            i=i+1
print(compare_lists())


list=[1,2,3,4,5]
i=0
while i<=list:
    if list[i]%2==0:
        print(list[i])
    else:
        print("not divide ")
