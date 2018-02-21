### [Haihui Cao's answer on 5-1-1 Nested ("Wrapped") Functions]
### The arguments of the functions are intergers.
### Disclaimer:this program didn't check the exception errors from the wrong input type.


# sum_digits function

def sum_digits(num):
    "takes an int and returns the sum of its (positive value) digits."

    # turn num into a list using comprehension. disregard the minus sign if num is negative.
    lst = [int(i) for i in str(num) if i in "0123456789"]

    # add all numbers in lst
    return sum(lst)

# diff_sum_digits function

def diff_sum_digits(num):
    "calls sum_digits function and compute the input number minus the sum of digits of input number."

    temp_val = sum_digits(num)
    return num - temp_val


# wraps_diff_sum_digits function

def wraps_diff_sum_digits(num):
    """calls diff_sum_digits function.
    If diff_sum_digits returns a result that has more than one digit(either negative or positive),
    have this new function replace the result with the sum of the digits of the result.
    Do this repeatedly until the result has just one digit, then display it."""

    result = diff_sum_digits(num)

    while len(str(result)) > 1:
        result = sum_digits(result)

    return result
