import math

def find( p ):
    return math.ceil(math.sqrt(2 * 365 *
                     math.log(1/(1-p))))
# Driver Code
print(find(0.50))