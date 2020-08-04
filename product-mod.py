from functools import reduce

def productExceptSelf(nums, m):
    l = nums
    
    known_products = {} # cache
    
    
    def get_prod_mod(x,y,m):
        if (x,y) in known_products:
            return known_products[(x,y)]

        prod = x * y % m
        known_products[(x,y)] = prod
        return prod
        
    
    def helper(l,m):
        if len(l) == 1:
            return ([1], l[0]) # list (single element list) and 1 to multiply other half by
            
        mid = len(l) // 2
        
        left_result = helper(l[:mid], m)
        right_result = helper(l[mid:], m)

        l_prod = left_result[1]
        r_prod = right_result[1]
        
        left_list = [get_prod_mod(c, r_prod, m) for c in left_result[0]]
        right_list = [get_prod_mod(c, l_prod, m) for c in right_result[0]]

        result_list = left_list + right_list

        product = left_result[1] * right_result[1]

        return (result_list, product)

    
    help = helper(l,m)
    
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
