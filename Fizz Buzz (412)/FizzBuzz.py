# FizzBuzz Solution
# Description:
# If a number is divisible by 3 print fizz, if divisible by 5 print buzz,
# if divisible by both 3 and 5 print FizzBuzz
# Worked on by: Hunter Copening



for i in range(1, 101):

    #FizzBuzz
    if i%5==0 and i %3==0:
        print("FizzBuzz")

    #Fizz
    elif i%3==0:
        print("Fizz")

    #Buzz
    elif i%5==0:
        print("Buzz")
    
    # If none of the above
    else:
        print(i)
