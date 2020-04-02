def my_function(fname):
    print(fname + " Referenes")
my_function("Emil")
my_function("Tobias")
my_function("Linus")
my_function("dropped")



# Examples 

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil", "Refsnes")

# Checks


def my_function(fname, lname):
  print(fname + "chcek1" + lname)

my_function(fname = "venakt", lname = "check")

# One example of reading it from integers
def my_function(*kids):
  print("The youngest child is " + kids[2])

my_function("Emil", "Tobias", "Linus")

# Example
def my_function(child3, child2, child1):
  print("The youngest child is " + child3)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")
