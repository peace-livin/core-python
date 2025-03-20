# cost price and seeling price profit loss using user input in if else

# cost=int(input("Enter cost:"))
# selling_price=int(input("Enter selling price:"))

# profit_loss=selling_price-cost
# if profit_loss>0:
#     print("Profit:",profit_loss)
# elif profit_loss<0:
#     print("Loss:",profit_loss)
# else:
#     print("No profit or loss")
    
    
    
# Q2). number even or odd using if else
# num=int(input("Enter number:"))
# if num%2==0:
#     print("Even Number")
# else:
#     print("Odd Number")
    
    
# Q3). name if the value start with k then print hello mr k else print hello guest
# name=input("Enter name:")
# if name.lower().startswith("k"):
#     print("Hello Mr",name)
# else:
#     print("Hello Guest")
    
    
# name=input("Enter name:")
# if name.startswith("a"):
#     print("hello mr ",name)
# else:
#     print("hello guest")


#Q4). take 5 subjects marks from user and pass or fail print total marks ,print percentage,
# print grade using if elif else

subjectOne = int(input("Enter a subjectOne Marks : "))
subjectTwo = int(input("Enter a subjectTwo Marks : "))
subjectThree = int(input("Enter a subjectThree Marks : "))
subjectFour = int(input("Enter a subjectFour Marks : "))
SubjectFive = int(input("Enter a SubjectFive Marks : "))

if subjectOne >= 35 and subjectTwo >= 35 and subjectThree >= 35 and subjectFour >= 35 and SubjectFive >= 35:
    print("Congratulations You have passed all subjects")
else:
    print("You have failed some subjects")

TotalMarks = subjectOne + subjectTwo + subjectThree + subjectFour + SubjectFive
print(TotalMarks)

totalPercentage = subjectOne + subjectTwo + subjectThree + subjectFour + SubjectFive
totalPercentage = totalPercentage / 5
print(totalPercentage)

if totalPercentage >= 90.0:
    print("Congratulations You have passed O Grade")
elif totalPercentage >= 60.0 and totalPercentage < 90.0:
    print("You have passed A Grade")
elif totalPercentage >= 40.0 and totalPercentage < 60.0:
    print("You have passed B Grade")
elif totalPercentage >= 35.0 and totalPercentage < 40.0:
    print("You have passed C Grade")
elif totalPercentage > 35 and subjectOne < 35 and subjectTwo < 35 and subjectThree < 35 and subjectFour < 35 and SubjectFive < 35:
    print("You have Failed")
else:
    print("Enter Valid")

# for loop

# s= "akshay"
# l=[1,2,3,4,5,6,7,8,9,10]

# for i in l:
#     print(i)
#     if i==5:
#       print("printing is enough")
#       break