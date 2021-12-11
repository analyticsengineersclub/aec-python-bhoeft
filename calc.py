import argparse

# Notes from docs
# 1: holds all info necessary to parse the command line into py data types
# 2: tells parser how to take strings from the command line and turn into objects

parser = argparse.ArgumentParser(description="command-line calculator")  # 1

parser.add_argument("integers", nargs="+", type=int, help="integers for the accumulator")  # 2
parser.add_argument("--sum", dest="accumulate", action="store_const", const=sum, default=max,
                    help="sum the integers (default: max)")

args = parser.parse_args()
print(args.accumulate(args.integers))
