
# 2nd solution

def main(): # step 1

    x = int(input("What's x?: "))
    if is_even(x):       # here we naively assume that the function is_even already exists, step 2
                         # here for the sake of the exercise David Malan CS50P calls this function is_even
        print("Even")
    else:
        print("Odd")

def is_even(n): # step 4

#   if n % 2 == 0: (this is totally fine as a function) step 5
        #
        #  return True
   # else:
        # return False

# another way to write the code here above is_
 # return True if n % 2 == 0 else False step 6

# or just write a better leaner function, one could write the above like this here below:
# here above as the operation has in any way a True or False value, asking a question with If is not necessary
# so David Malan re-writes the function one last time to have only this here below: video conditionals 

    return n % 2 == 0 # step 6 (This is Pythonical! ) step 7
    
    

main() # if we call main(), as is_even is not yet defined, the code will break, step 3

# step 8 David Malan uses the new syntax keyword Match, but it is only available on Python ≥ 3.10, not on this version: I tried, it doesn't work
# he moves to file house.py

# first function

# this is fine as a solution, but it is not Pythonical

x = int(input("What's x?: "))
if x % 2 == 0:
    print("Even")
else:
    print("Odd")