#write a function that finds the sum of numbers from 1-100(both included) using a for loop.
#write another function that does the same operation using a while loop.
#sum 1 to 100 usinf a for loop
def sumnum_1():
    total=0

    for num in range(1,101):
        total+=num

    print(f"sum of 1 to 100 is {total}")

#sum 1 to 100 using while loop
def sumnum_2():
    total = 0
    num = 1

    while num <101:
        total += num
        num = 1

    print(f"sum of 1 to 100 is {total}")


sumnum_1()

sumnum_2()
    
