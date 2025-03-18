#   map (): if we want to perform some common operation on each evry element prsent inside elements list
#  map(fun,sequence):
#  where fun is used to write maping logic and sequence may list ,tuple ,set,...


# example 


# def double(num):
#     return num*2

# nums=[1,2,3,4,5]
# out =list(map(double,nums))
# print(out)


# l=[1,2,3,4,5,6,7,8,9,10,11,12]

# # (list)

# out =list(map(lambda x:x*2,l))
# print(out)

# # (set)

# out =set(map(lambda x:x*2,l))
# print(out)

# # (tuple)

# out =tuple(map(lambda x:x*2,l))
# print(out)


# write a function which takes a list and add developer in each element*****


# def add_dev(l):
#     out =list(map(lambda x:x+" developer",l))
# print(add_dev(["sushil","subham","bhagesh","vishal","akshay","yes"]))


# num=["sushil","subham","bhagesh","vishal","akshay","yes"]
# out =list(map(lambda x:x+" developer",num))
# print(out)



# filter():

# l =  [1,2,3,4,5,6,7,8,9,10,11,12]

# out = list(filter(lambda x:x%2==0,l))
# print(out)


# num=["sushil","subham","bhagesh","vishal","akshay","yes"]
# out =list(filter(lambda x:len(x)%2==0,num))
# print(out)


#Q1). string from user and print vovels present in string using filter and lambda 

# vovels=["a","e","i","o","u","A","E","I","O","U"]
# string=input("Enter string:")
# out=tuple(filter(lambda x:x in vovels,string))
# print(out) 


# Q2).


num=[
    {'pid':111,'pname':'samsung-S24','price':125000,'cat':'Mobile'},
     {'pid':222,'pname':'Apple','price':125000,'cat':'Mobile'},
      {'pid':333,'pname':'hP','price':115000,'cat':'Laptop'},
      {'pid':444,'pname':'honor','price':145000,'cat':'Laptop'},
    ]

out=list(filter(lambda x:x['cat']=='Mobile',num))
print(out)


