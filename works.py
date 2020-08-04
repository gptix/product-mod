from functools import reduce

def productExceptSelf(nums, m):
    l = nums
    
    known_products = {} # cache
    
    def get_product_modulo(x,y,m):
        global known_products
        if (x,y) in known_products:
            return known_products[(x,y)]
        known_products[(x,y)] = x * y % m
    
    def helper(l,m):
        if len(l) == 1:
            return ([1], l[0]) # list (single element list) and 1 to multiply other half by
            
        mid = len(l) // 2
        
        left_result = helper(l[:mid], m)
        lr_0 = left_result[0]
        right_result = helper(l[mid:], m)
        rr_0 = right_result[0]
        
        left_product = left_result[1]
        right_product = right_result[1]
        
        left_list = [cell * right_product % m for cell in lr_0]
        right_list = [cell * left_product % m for cell in rr_0]

        result_list = left_list + right_list

        product = left_result[1] * right_result[1]

        return (result_list, product)

    
    help = helper(l,m)
    
    return reduce(lambda x,y: (x + y) % m, help[0])
