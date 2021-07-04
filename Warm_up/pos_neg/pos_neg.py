'''
We want to solve the following problem
Given 2 int values, return True if one is negative and one is positive.
Except if the parameter "negative" is True,
then return True only if both are negative.

'''

def pos_neg(a, b, negative):
  '''
  if negative then we check to see if the a and b are negative. If not negative then we check to see if one of the interger is positive>"
  '''
  if negative:
    if (a < 0 and b < 0):
      return True
    else:
        return False
  else:
    if (a < 0 and b > 0) or (b < 0 and a > 0):
      return True
    else:
      return False
