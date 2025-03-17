# anonymous_function : function without name 
# it is also called as lambda function or lambda expression
# adv of lamda func is just for instant use 

# def square(num):
#     return num*num
# print("Square of 5 is:",square(5))

# # lambda input_list : expression

# sq=lambda n:n*n
# print("Square of 5 is:",sq(6))


# # Q.1)create lamda function which take input as return total no.of chracter

lamda_func=lambda x:len(x)
print("Length of string is:",lamda_func("hello world"))

# even odd function
lamda_func=lambda x:x%2==0
print("Is number even or even?",lamda_func(4))
print("Is number even or even?",lamda_func(5))


