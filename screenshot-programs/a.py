import random as rand

def gen_rand(x = 1, lower = 1, upper = 100):
    """
    Generates x random integers between lower and upper inclusive
    """
    ret_list = []; # create list for values to return
    for i in range(x): #generate numbers
        ret_list += [rand.randint(lower, upper)]
    return ret_list

n = input("How many random numbers do you want to generate: ")
l = input("What is the lower limit: ")
u = input("What is the upper limit: ")

nums = gen_rand(n,l,u)

for i in nums:
    print(i)
