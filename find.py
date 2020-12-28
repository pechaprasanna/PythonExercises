import argparse as ap
from pathlib import Path



def name_find(start_path, args):
    for child in start_path.rglob(args.name):
        print(child)

def type_find(start_path, args):
    for child in start_path.rglob(args.name or "*"):
        if args.type == 'd' and child.is_dir():
            print(child)
        elif args.type == 'f' and child.is_file():
            print(child)

def parse_args():
    parser = ap.ArgumentParser()
    parser.add_argument('path', type=str,nargs=1)
    parser.add_argument('-n','--name')
    parser.add_argument('-t','--type',choices=['f','d'])
    return parser.parse_args()

def find_files(args):
    start_path = Path(args.path[0])

    if args.name and not args.type:
        name_find(start_path,args)
    elif args.type:
        type_find(start_path,args)
    else:
        args.name = "*"
        name_find(start_path,args)       

find_files(parse_args())