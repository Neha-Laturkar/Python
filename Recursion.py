def try_recursion(k):
    if (k > 0):
        result = k + try_recursion(k - 1)
        print(result)
    else:
        return 0
    return result
        
print("Recursion Example Results")
try_recursion(6)   
