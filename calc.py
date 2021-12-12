import argparse


def subtract(list_of_2_numbers):
    """get the difference between 2 numbers

    Parameters
    ----------
    list_of_2_numbers : list
        the 2nd element will be subtracted from the first

    Returns
    -------
    int
        the difference between two numbers
    """
    list_size = len(list_of_2_numbers)
    if list_size != 2:
        raise ValueError(f"function needs a list of 2. yours has {list_size} elements")
    number1, number2 = list_of_2_numbers
    difference = number1 - number2
    print(f"the difference of {number1} minus {number2} is: {difference}")
    return difference


def multiply(list_of_numbers):
    """get the product of a list of more than 1 number
    
    Parameters
    ----------
    list_of_numbers : list
        the numbers you want to multiply.
    
    Returns
    -------
    int
        the product of the multiplication
    """
    if len(list_of_numbers) < 2:
        raise ValueError("list needs at least 2 numbers to multiply")
    product = 1
    for n in list_of_numbers:
        product = product * n
    print(f"the product is: {product}")
    return product
    

def divide(list_of_2_numbers, decimals=3):
    """get the quotient from dividing 2 numbers.
    
    Parameters
    ----------
    list_of_2_numbers : list
        1st element will be divided by, 2nd element is divisor
    decimals : int
        decimals to round to. default: thousandth

    Returns
    -------
    int
        the result of dividing number1 by number2
    """
    list_size = len(list_of_2_numbers)
    if list_size != 2:
        raise ValueError(f"function needs a list of 2. yours has {list_size} elements")
    
    number1, number2 = list_of_2_numbers
    if number2 == 0:
        raise ValueError("cannot divide, the divisor is 0")
    else:
        quotient = round(number1 / number2, decimals)
        print(f"the quotient of {number1} divided by {number2} is: {quotient}")
        return quotient


# invoking as a script
if __name__ == "__main__":
    
    # notes to future self from https://docs.python.org/3/library/argparse.html: 
    # 1: holds all info necessary to parse the command line into py data types
    # 2: method creates a special action object so program functionality can be broken into sub-commands
    # 3: parses arguments from strings to objects, assigns them as attributes of the namespace
    
    parser = argparse.ArgumentParser(description="command-line calculator", prog="Calculator",
                                     epilog="%(prog)s was built to help learn how dbt was built")  # 1

    subparser = parser.add_subparsers(title="subcommands", help="subcommand help", dest="subcommand")  # 2

    parser_add = subparser.add_parser(name="add", help="add integers")
    parser_add.add_argument("ints_to_sum", nargs="+", type=int)

    parser_subtract = subparser.add_parser("subtract", help="add 2 integers")
    parser_subtract.add_argument("ints_to_subtract", nargs="+", type=int)

    parser_multiply = subparser.add_parser("multiply", help="multiply integers")
    parser_multiply.add_argument("ints_to_multiply", nargs="+", type=int)

    parser_divide = subparser.add_parser("divide", help="divide 2 integers")
    parser_divide.add_argument("ints_to_divide", nargs="+", type=int)

    args = parser.parse_args()  # 3

    if args.subcommand == "add":
        sum_result = sum(args.ints_to_sum)
        print(f"the sum is: {sum_result}")

    elif args.subcommand == "subtract":
        subtract(args.ints_to_subtract)
    
    elif args.subcommand == "multiply":
        multiply(args.ints_to_multiply)

    elif args.subcommand == "divide":
        divide(args.ints_to_divide)