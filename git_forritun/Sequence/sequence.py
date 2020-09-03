#We are going to design a algorithm that generates the fyrst n number in following sequence: 1,2,3,6,11,20,37....
#First user will input the length of the sequence
#The algorith need to keep track of the last 3 integers, next number is the sum of that
#To get the first integers the first number will be 0, the second number 0 and the third number 1. So it will be 0 + 0 + 1 = 1
#To get the second the first number will be 0, second 1 and third 1. So it will be 1 + 0 + 1 = 2
#The third number in the sequence will then be 0 + 1 + 2 = 3
#The forth will then be 1 + 2 + 3 = 6 and so on
#first number = second number, second number = third number, and third number is the total of all three numbers

n = int(input("Enter the length of the sequence: ")) # Do not change this line
next_number = 0
num_1 = 0
num_2 = 0
num_3 = 1
#The following loop adds the numbers to geter and moves 
for algorithm in range(0,n):
    num_1 = num_2
    num_2 = num_3
    num_3 = next_number
    next_number = num_1 + num_2 + num_3
    print(next_number) 
        
