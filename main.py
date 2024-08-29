#naive implementation only using basic recursion
import time
def den_to_bin(n,curr): # defines the function
    if n == 0:
        return '0' + curr # base case 1, if the number is 0 return 0
    elif n == 1:
        return '1' + curr # base case 2, if the number is 1 return 1
    else:
        return den_to_bin(n//2,str(n%2) + curr) # recursive case, if number more than 1, call the
                                                # function itself and append the remainder after diving
                                                #the number by 2 to the leftmost


#memoized and more efficient implementation
global all_nums
all_nums = {0:'0',1:'1'} #dictionary with the base cases defined

def memoize(n,curr):
    if n in all_nums.keys():
        return all_nums.get(n) + curr #checks if the number is already calcualted
                                      #allows to check for base cases because they are already
                                      #in the dictionary so it returns the right
    else:
        all_nums[n] = memoize(n//2,str(n%2) + curr) #if not in the dictionary, it
    return all_nums[n]

t1 = time.time()
for i in range(1000000):
    den_to_bin(i,'')
print(time.time() - t1)

t2 = time.time()
for i in range(1000000):
    memoize(i,'')
print(time.time()-t2)

