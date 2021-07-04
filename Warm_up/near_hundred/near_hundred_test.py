'''
test for near_hundred function

'''
# pylint: disable=unused-variable
#import the code here
from near_hundred import near_hundred


def describe_number_is_10_near_100_or_200():
    
    '''
    We are mainly worried about the function being within 10 digits away from 100 or 200. 
    if it is, then it will return true and if not then it will return false.
    '''
    def that_determines_whether_or_not_number_is_near_100_or_200():

        assert near_hundred(101) == True # not within 10 of 100 
        assert near_hundred(120) == False # not within 10 of 100 
        assert near_hundred(195) == True # within 10 of 100 
        assert near_hundred(96) == True # within 10 of 100 
        assert near_hundred(91) == True # within 10 of 100 
        assert near_hundred(290) == False # not within 10 of 200 
        assert near_hundred(202) == True # within 10 of 200 
        assert near_hundred(19) == False # not within 10 of 100 
        assert near_hundred(39) == False # not within 10 of 100 
        assert near_hundred(87) == False # not within 10 of 100 
        assert near_hundred(98) == True #  within 10 of 100 
    

#     integar = 10
#     acutal = near_hundred(integar)
#     assert acutal == False

# def test_number_is_95_near_100_or_200():
#     integar = 95
#     acutal = near_hundred(integar)
#     assert acutal == True

# def test_number_is_195_near_100_or_200():
#     integar = 195
#     acutal = near_hundred(integar)
#     assert acutal == True

# begin writing test
