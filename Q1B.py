#modify your functions such that summation starts from 5 instead of 1
#Then further genaralize such that the start value is entered by the user.
#sum 5 to 100 using for loop
def sumnum_1():
    total=0

    for num in range(5,101):
        total+=num

    print(f"sum of 5 to 100 is {total}")

#sum 5 to 100 using while loop
def sumnum_2():
    total = 0
    num = 5

    while num <100:
        total += num
        num = 1

    print(f"sum of 5 to 100 is {total}")


#sum from the start value entered by user to 100 using for loop
def sumnum_3():
    first_num=int(input("Enter a number below 100: "))

    if first_num>=100:
        print("print enter number below 100")
        return
    total=0

    for num in range(first_num,101):
        total += num

    print(f" sum of {first_num} to 100 is {total}")
def sumnum_4():
    
    num=int(input("Enter a number below 100: "))

    first_num=num
    
    if num>=100:
        print("please enter a number below 100")
        return
    total=0

    while num<=100:
        total+= num
        num+=1

    print(f"sum of{first_num} to 100 is {total} ")

sumnum_1()
print()
sumnum_2()
print()
sumnum_3()
print()
sumnum_4()





    

    





