#LeetCode Problem #412 "Fizz Buzz"
#	Given an integer n, return a string array answer (1-indexed) where:
#	answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
#	answer[i] == "Fizz" if i is divisible by 3.
#	answer[i] == "Buzz" if i is divisible by 5.
#	answer[i] == i (as a string) if none of the above conditions are true.

# Worked on by: Dylan Hermosillo

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        #create a list
        list = []
        #loop through nth integer
        for i in range (1, n + 1):
            #FizzBuzz if divisible by 3 & 5
            if i % 15 == 0:
                list.append("FizzBuzz")
            #Fizz if divisible by 3
            elif i % 3 == 0:
                list.append("Fizz")
            #Buzz if divisible by 5
            elif i % 5 == 0:
                list.append("Buzz")
            else:
                list.append(str(i))
        return list
