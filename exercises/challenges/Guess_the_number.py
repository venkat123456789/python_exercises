# used the libraries seed and randinit from random
# seed is the one call that we use for random calls
from random import seed
from random import randint
seed(1)
for _ in range(1):
	value = randint(0, 19)
print(value)
# printing all the 20 random values 

# creating a input value
number = input("Enter your value : ") 
# making number as an integer data type
number = int(number)

# passing the conditions
if number < value:
    print ("That's too low, try again.")
else:
    print ("That's too high, try again.")

