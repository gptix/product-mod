from functools import reduce

def productExceptSelf(nums, m):
    """for a list of integers (l1)  [n0, n1...ni], return the int that
    would be returned by:
    - create a list (l2) that holds the results, for each n in l1, 
    multiplying all OTHER elements in l1
    - then sum these into an int
    - then modulo that result."""
 
    l = nums # just renaming to fit code I built in Jupyter
    
    known_products = {} # cache
    
    def get_prod_mod(x,y,m):
        """Check cache for a known product of x and y, and use if there.
        Otherwise, multiply x * y, then take the mod (and cache)."""
        if (x,y) in known_products:
            return known_products[(x,y)]

        prod = x * y % m
        known_products[(x,y)] = prod
        return prod
        
    
    def helper(l,m):
        """ Inner function to do most of the work."""

        # Case to stop recursion.
        if len(l) == 1:
            return ([1], l[0]) 

        # By problem spec, input list will always have at least two
        # elements, so recursion will always start.
        mid = len(l) // 2

        # recursion will return a list and a product (mod m) of the elements
        # in the list
        left_result = helper(l[:mid], m)
        right_result = helper(l[mid:], m)

        l_prod = left_result[1]
        r_prod = right_result[1]

        # Apply multiplication and modding.
        left_list = [get_prod_mod(c, r_prod, m) for c in left_result[0]]
        right_list = [get_prod_mod(c, l_prod, m) for c in right_result[0]]

        # Combine left and right lists.
        result_list = left_list + right_list

        # Calculate product of this level of recursion.
        product = left_result[1] * right_result[1]

        # return from recursive call.
        return (result_list, product)

    # Outer function calls helper.
    help = helper(l,m)

    # return result of outer function.
    return reduce(lambda x,y: (x + y) % m, help[0])


### test data

ns = [1, 2, 3, 4]
m = 12

ns = [2, 100]
m = 24

ns = [5, 8, 6, 3, 2]
m = 8

### call
productExceptSelf(ns,m)
