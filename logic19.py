def main(x):
    """
    Given an integer x, return true if x is palindrome integer.
    An integer is a palindrome when it reads the same backward as forward.

    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    s1=x%10
    s2=x%10//10
    s3=x//10
    return 9<x and x<1000 and (s1*100+s2*10+s3*1==x or x%10==x//10)
print(main(22))    