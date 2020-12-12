import argparse

parser = argparse.ArgumentParser(description = 'Process some files.')
parser.add_argument('files', type=argparse.FileType('r'), nargs='+')
parser.add_argument('-w','--write_to',help='Output filename')
parser.add_argument('-n','--numbers',action='store_true',help='Line numbers')

args = parser.parse_args()

if(args.write_to):
    out = open(args.write_to,'w')

line_number=1

for file in args.files:
    if(args.write_to):
        if(args.numbers):
           for line in file:
               out.write(f'\t{line_number}\t{line}\n') 
               line_number += 1
        else:
            out.write(file.read())
    else:
        if(args.numbers):
           for line in file:
               print(f'\t{line_number}\t{line}',end='\n') 
               line_number += 1
        else:
            print(file.read())
    file.close()
if(args.write_to):
    out.close()