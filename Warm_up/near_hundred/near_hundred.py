'''
The following is the code that we are trying to solve.

Given an int n, return True if it is within 10 of 100 or 200. 
Note: abs(num) computes the absolute value of a number.

'''
def near_hundred(n):
    '''
    takes interger and indicates whether it is within 10 digits of 100 or 200 
    '''
    if abs(100 - n) <=  10 or abs(200 - n) <= 10:
        return True
    else:
        return False
    

    '''
    code given from webstite
    return ((abs(100 - n) <= 10) or (abs(200 - n) <= 10))
    '''
   