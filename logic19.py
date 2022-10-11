def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    
    return 9<x and x<1000 and type(x)==type(1) and x%10==x//10
print(main(22))    