                           # return #
                    
# def sip(amnt):
#     returnamnt = amnt + 1000
#     return returnamnt

# # rv=sip(5000)
# # print(rv)
# # print(sip(9000))

# print("***welcom to qst plan***")
# name=input("ENTER YOUR NAME")
# amnt=int(input("ENTER YOUR AMOUNT"))
# total_amnt =sip(amnt)
# if total_amnt >=10000:
#     print("your total return value is 9.8%")
# elif total_amnt >= 5000 and total_amnt < 10000:
#     print("your total return value is 7.5%")
# else:
#     print("your total return value is 5%")


# def add(n1,n2):
#     add = n1 + n2
#     sub = n1 - n2
#     mul = n1 * n2
#     div = n1 / n2
#     return add,sub,mul,div
    
# n1,n2=input("ENTER YOUR 1 NUMBER")
# n1,n2=input("ENTER YOUR 2 NUMBER")
# add,sub,mul,div=add(n1,n2)
# print("ADDITION:",add)
# print("SUBTRACTION:",sub)
# print("MULTIPLICATION:",mul)
# print("DIVISION:",div)



def Zigzag(num):
    if num %3 == 0 and num %5 == 0:
        return "zigzag"
    elif num %3 == 0:
        return "zig"
    elif num %5 == 0:
        return "zag"
    else:
       print(f"return number {num}is not divisible by 3 or 5")
        
    
print(Zigzag(3))
print(Zigzag(25))
print(Zigzag(30))
(Zigzag(7))



    



