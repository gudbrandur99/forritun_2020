#Algorithmi
#User inputs intigers and the program prints them out
#The program runs until user inputs negative intiger

# Fill in the missing code
num_int=0
max_int= 0
while num_int >= 0:
    num_int = int(input("Input a number: "))    # Do not change this line
    if num_int > max_int:
        max_int = num_int
    elif num_int < max_int:
        max_int = max_int
 
print("The maximum is", max_int)    # Do not change this line