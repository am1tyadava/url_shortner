import math
import string


def convert_to_base_62(num, base_value=62):
    """
    Return a encoded string or a hash based on the given num

    Parameters
    ----------
    num: int
        This is basically a index in an array that will be converted to some kinda of hash
    base_value: int
        How many chars will be used

    Returns
    -------
    encoded_hash: str
        This will return an encoded hash for the given number

    Examples
    --------
    >>> from amityadav_url_shortner.services import convert_to_base_62
    >>> convert_to_base_62(100)
    '1C'

    >>> convert_to_base_62(1000000000000000)
    '4zXyLE1Gw'

    """
    if base_value <= 0 or base_value > 62:
        return 0

    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    rem = num % base_value
    res = base[rem]
    quot = math.floor(num / base_value)
    while quot:
        rem = quot % base_value
        quot = math.floor(quot / base_value)
        res = base[int(rem)] + res
    return res


def convert_to_base_10(encoded_str, base_value=62):
    """
    Return an integer based on the given str encoded_str

    Parameters
    ----------
    encoded_str: str
        This is the encoded string that we want to convert into a integer so that we can
        query our database by making this as id
    base_value: int

    Returns
    -------
    a number: int

    Examples
    --------
    >>> from amityadav_url_shortner.services import convert_to_base_10
    >>> convert_to_base_10('1C')
    100
    >>> convert_to_base_10('4zXyLE1Gw')
    1000000000000000

    """
    base = string.digits + string.ascii_lowercase + string.ascii_uppercase
    res = 0
    for i in range(len(encoded_str)):
        res = base_value * res + base.find(encoded_str[i])
    return res
