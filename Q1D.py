#modify the function such that numbers increment by 2


#sum from 1 to value entered by the user incrementing by 2 using for loop

def sumnum_1():
    last_num =int(input("Enter a number greater than 1: "))

    if last_num<= 1:
        print("please enter a number greater than 1: ")
        return
    total=0

    for num in range(1,last_num+1,2):
        total+=num

    print(f"sum of 1 to {last_num} while stepping 2 is {total}")

#sum from 1 to value entered by the user incrementing by 2 using a while loop
def sumnum_2():
    last_num=int(input("Enter a number greater than 1: "))

    if last_num<= 1:
        print("please enter a number greater than 1")
        return
    
    total=0
    num=1

    while num<= last_num:
        total+=num
        #increment by 2
        num+=2
        
    print(f"sum of 1 to{last_num} while stepping 2 is {total} ")

sumnum_1()
print()
sumnum_2()
