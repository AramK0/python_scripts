import argparse

parser = argparse.ArgumentParser("Addition calculator")

parser.add_argument('-n1', '--number1', type=int, required=True, help="The first number")
parser.add_argument('-n2', '--number2', type=int, required=True, help="The seconds number")

args_group = parser.add_mutually_exclusive_group()

args_group.add_argument("-q", "--quiet", action="store_true", help="Prints little text")
args_group.add_argument("-v", "--verbose", action='store_true', help="Prints lots of text")

args = parser.parse_args()

if args.quiet:
    print(args.number1 + args.number2)
elif args.verbose:
    print(args.number1, "+", args.number2, "equals:", args.number1 + args.number2)
else:
    print(args.number1, "+", args.number2, "+", args.number1 + args.number2)

