import argparse


def subtract(number1, number2):
    """get the difference between 2 numbers

    Parameters
    ----------
    number1 : int
        the number to be subtracted from
    number2 : int
        The number to subtract

    Returns
    -------
    int
        the difference between two numbers
    """
    return number1 - number2


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
        raise ValueError("list arg needs at least 2 numbers to multiply")
    product = 1
    for n in list_of_numbers:
        product = product * n
    return product
    

def divide(number1, number2):
    pass


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
    parser_subtract.add_argument("ints_to_subtract", nargs=2, type=int)

    parser_multiply = subparser.add_parser("multiply", help="multiply integers")
    parser_multiply.add_argument("ints_to_multiply", nargs="+", type=int)
    
    args = parser.parse_args()  # 3

    if args.subcommand == "add":
        sum_result = sum(args.ints_to_sum)
        print(f"the sum is: {sum_result}")

    elif args.subcommand == "subtract":
        difference = subtract(args.ints_to_subtract[0], args.ints_to_subtract[1])
        print(f"the difference is: {difference}")
    
    elif args.subcommand == "multiply":
        product = multiply(args.ints_to_multiply)
        print(f"the product is: {product}")

    elif args.subcommand == "divide":
        pass
