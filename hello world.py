def fibonacci(n): 
    """fibonacci series
        
    Args:
        n (int): input number
        
    """
    list = [0,1]
    if n == 1 or n == 0:
        return 0
    else:
        for index in range(1, n-1):
            list.append(list[index]+list[index-1])
        return list
    

print(fibonacci(5))
