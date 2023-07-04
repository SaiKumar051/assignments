#Print First 10 natural numbers using while loop
# sum = 1
# while sum <= 10:    
#   print(sum) 
#   sum += 1  

# Calculate the sum of all numbers from 1 to a given number

# n = int(input("enter number : "))
# sum = 0
# i = 1
# while i<= n:
#    sum=sum+i
#    i+=1
# print("the sum of ",n," number is : ",sum)


#  Write a program to print multiplication table of a given number

# num = int(input("Enter a number: "))
# s = 1
# while s <= 10:
#     answer = num * s
#     print(num, "*", s, "=", answer)
#     s += 1

# Display numbers from a list using loop

# l1= [10,20,30,40,50]
# n = 0
# while n < len(l1):
#    print(l1[n])
#    n += 1 

# Count the total number of digits in a number

# n = int(input("enter your number: "))
# num = str(n)          # converting number to string to give no of digits
# count = len(num)
# print("no of digits", count)

# Print list in reverse order using a loop

# num = (10,20,30,40,50)
# n = len(num) -1  
# while n >= 0:
#     print(num[n])
#     n -= 1  # here decrementing the value

# Display numbers from -10 to -1 using for loop

# for num in range(-10, 0):
#     print(num)
# else :
#     print("done")   

# Write a program to display all prime numbers within a range

start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))
print("Prime numbers between", start, "and", end, "are:")
num = start
while num <= end:
    if num > 1:
        prime = True
        divisor = 2
        while divisor <= int(num ** 0.5):
            if num % divisor == 0:
                prime = False
                break
            divisor += 1
        if prime:
            print(num)
      #   num += 1


# for i in range(5):
#     for j in range(i+1):
#         print("*",end="")
#     print()   

# for i in range(5, 0, -1):
#     for j in range(i):
#         print("*", end="")
#     print()



# for i in range(5):
#     for j in range(5 - i - 1):
#         print(" ", end="")
#     for k in range(i + 1):
#         print("*", end="")
#     print()

# for i in range(5):
#     for j in range(i):
#         print(" ", end="")
#     for k in range(5 - i):
#         print("*", end="")
#     print()
