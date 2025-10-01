#task 5 
def repeat(func, times, values):
    result = values
    for _ in range(times):
        result = func(result)
    return result
print (repeat(lambda x:x+1,3,5))  