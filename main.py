#WRITE YOUR CODE IN THIS FILE
def close10(x, y):
    if abs(x-10) < abs(y-10) :
        return x

    elif abs(x-10) > abs(y-10):
        return y 
    
    else:
        return "0"
