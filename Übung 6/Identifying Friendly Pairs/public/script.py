# You are completely free to change this variables to check your algorithm.
num1 = 2.6
num2 = 28


# Function to check whether two numbers are friendly pairs or not.
def isFriendlyPair():
    # You need to complete this function.
    # You need to return a boolean variable . If num1 and num2 are friendly pairs return True.
    # If they are not return False. 
    # The numbers must be valid according to description before determining friendly parity situations. 
    # Return "Invalid" if they are not valid.

    # check if numbers are the same or if numbers are not natural
    if num1 == num2 or (num1 <= 0 or num2 <= 0) or not (isinstance(num1, int) and isinstance(num2, int)): #see de Morgans Law
        return str("Invalid")

    # check abundancy of first number
    divisors_1 = 0
    for i in range(num1, 0, -1):
        if num1 % i == 0:
            divisors_1 += i
    abundancy_1 = divisors_1/num1


    # check abundancy of second number
    divisors_2 = 0
    for j in range(num2, 0, -1):
        if num2 % j == 0:
            divisors_2 += j
    abundancy_2 = divisors_2/num2


    # check if num1 and num2 are friendly numbers
    if abundancy_1 == abundancy_2:
        return True
    else:
        return False


# This line prints your method's return so that you can check your output.
print(isFriendlyPair())
