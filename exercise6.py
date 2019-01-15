from pathlib import Path
import sys
import argparse

def name_find(start, args):
    for f in start.rglob(args.name):
        print(f)

def find_all(start, args):
    for f in start.rglob(args.name or "*"):
        if f.is_dir():
            print("{} is a directory".format(f))
        elif f.is_file():
            print("{} is a file".format(f))

def type_find(start, args):
    if args.type not in ['d', 'f']:
        print(f"Unknown type: {args.type}")
        sys.exit(1)

    for f in start.rglob(args.name or "*"):
        if args.type == "d" and f.is_dir():
            print("{} is a directory".format(f))
        elif args.type == "f" and f.is_file():
            print("{} is a file".format(f))

def find_files(args):
    start_path = Path(args.start[0])
    if args.name and not args.type:
        name_find(start_path, args)
    elif args.type:
        type_find(start_path, args)
    elif args.all:
        find_all(start_path, args)
    else:
        print("You need --name, --type, --all")
        sys.exit(1)

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('start', type=str, nargs=1)
    parser.add_argument('-n', '--name', type=str, help="Print the name of the args")
    parser.add_argument('-t','--type', type=str, help="Print the name and the type of the argument with the 'd' or 'f' flag")
    parser.add_argument('--all', type=str, help="Print the name and type of all arguments")
    return parser.parse_args()

find_files(parse_args())
