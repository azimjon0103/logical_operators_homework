def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is even".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return 9<a and a<100 and (a//10+a%10)%2==0
print(main(22)) 