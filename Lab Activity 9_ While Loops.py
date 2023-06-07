#Marco Villegas
#6/7/23

#Problem 1
print("\n\nProgram 1 - Infinite.py")

a = 1
while a == 1: b = print("Infinite")
print("Welcome to  infinty loops!")
#This program has a = 1 and in the while loop we have, a == 1, so the program
#will infintely loop back to the print statement; thus printing the word
#infinite forever.
#COMMENT OUT line 8, the while loop for problem 1 to see other code.


#Problem 2
print("\n\nProgram 2 - NumList10.py")

L = []
i = 0
while i < 11:
    L.append(i)
    i += 1
print(L)
#This program loops through the list, it does so by having i = 0 in the
#beginning, and then be incrimited in the while loop by 1 each time it loops
#through the list. It will loop until i is less than 10 and stop.



#Problem 3
print("\n\nProgram 3 - NumList35.py")


lst = []
sum = 0
while sum <= 100:
    n = int(input("Please enter a number: "))
    sum += n
    lst.append(n)
print(lst)
#This program has an empty list and in the while loop it will ask the user to
#input a number and append it to the list. This will repeat until the number
#reaches over 100 and prints out the list of number to user inputed. 



#Problem 4
print("\n\nProgram 4 - NumListDivide.py")

count = 0
tens = []
while count < 50:
    count += 1
    if count % 10 == 0:
        tens.append(count)
print(tens)
#This program, much like program 3, has an empty list named tens, in the while
#loop it increases the count from 0 up to 50. Inside the while loop I also have
#an if statement, which states if the number in the count is divisible by 10 it
#should append that number to the tens list; thus giving a list of our answers.
