#comment on what would be the difference,in general, between using X>0 or x!=0 as the while condition, when x is a float. note that floats are not always exact.
#answer: there is no difference using x>0 or x!=0 because in both cases the loop runs when x is not 0.

def division_1():
    x=1.0

    while x !=0:
        x=x/2
        print(x)

def division_2():
    x=1

    while x >0:
        x=x/2
        print(x)

#division
print()
division_2()

