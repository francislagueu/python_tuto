import argparse

#parser = argparse.ArgumentParser()
# parser.add_argument("echo", help="echo the string you use here") #argument the program is willing to accept echo is a variable that store the argument past
# args = parser.parse_args()
# print(args.echo)

# parser.add_argument("square", help="Display a square of a given number", type=int) #options are treated as string unless explicitly specified
# args = parser.parse_args()
# print(args.square**2)

#OPTIONAL ARGUMENTS
# parser.add_argument("-v","--verbose", help="increase output verbosity", action="store_true") #option is now more of a flag rather than something that requires a value action=store_true means that if option is specified, assign the value True to args.verbose. it complains when you specify a value. -v is for short options
# args = parser.parse_args()
# if args.verbose:
#     print("verbosity turned on")

#COMPLEXITY
# parser.add_argument("square", type=int, help="Display a square of a given number")
# #parser.add_argument("-v", "--verbose", action="store_true", help="Increase output verbosity")
# #parser.add_argument("-v", "--verbosity", type=int, help="Increase output verbosity") #ability to have multiple verbosity values
# #parser.add_argument("-v", "--verbosity", type=int, choices=[0, 1, 2], help="Increase output verbosity") #Restriction on the values verbosity can have
# parser.add_argument("-v", "--verbosity", action="count", default=0, help="Increase output verbosity") #count the number of occurence of the optional argument
# args = parser.parse_args()
# answer = args.square**2
# #replace == with >= to fix a bug
# if args.verbosity >= 2:
#     print("The square of {} equals {}".format(args.square, answer))
# elif args.verbosity >= 1:
#     print("{}^2 == {}".format(args.square, answer))
# else:
#     print(answer)

#ADVANCED
# parser.add_argument("x", type=int, help="the base")
# parser.add_argument("y", type=int, help="the exponent")
# parser.add_argument("-v", "--verbosity", action="count", default=0)
# args = parser.parse_args()
# answer = args.x**args.y
# # if args.verbosity >= 2:
# #     print("{} to the power {} equals {}".format(args.x, args.y, answer))
# # elif args.verbosity >= 1:
# #     print("{}^{} == {}".format(args.x, args.y, answer))
# # else:
# #     print(answer)
# #DISPLAY MORE TEXT
# if args.verbosity >= 2:
#     print("Running '{}'".format(__file__))
# if args.verbosity >= 1:
#     print("{}^{} == ".format(args.x, args.y),end = '') #end='' is specific to python3 doesn't work in python 2.7
# print(answer)

#CONFLICTING OPTIONS
parser = argparse.ArgumentParser(description="Calculate X to the power of Y")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("x", type=int, help="the base")
parser.add_argument("y", type=int, help="the exponent")
args = parser.parse_args()
answer = args.x**args.y

if args.quiet:
    print(answer)
elif args.verbose:
    print("{} to the power {} equals {}".format(args.x, args.y, answer))
else:
    print("{}^{} == {}".format(args.x, args.y, answer))
