# make a python script that will take a number and return the sum of all the digits of the number


def sum_of_digits(num):
    # initialize a variable to hold the running sum
    sum = 0

    # iterate through each digit of the input integer
    while num > 0:
        # add the last digit to the running sum
        sum += num % 10
        # remove the last digit from the input integer
        num = num // 10

    # return the final sum of digits
    return sum


print(sum_of_digits(123))

# or


def sum_of_digits(num):
    return sum(int(i) for i in str(num))


print(sum_of_digits(123))
