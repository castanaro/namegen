#!/usr/bin/python3

'''

namegen.py by Michael Castanaro

A name generator useful for OSINT phases in penetration testing/red teaming.

Inspiration from superkojiman's namemash.py.

'''

from argparse import RawTextHelpFormatter
import argparse
import sys
import hashlib
import os
import random

if __name__ == '__main__': 

    parser = argparse.ArgumentParser(description='Namegen takes files comprised of first and/or last names, formats them based upon a selection (e.g., first.last), appends a chosen domain (if specified), and outputs to a file. \n\nExample: ./namegen.py -f first.txt -l last.txt -o output.txt -d domain.com (select a \'#\' when prompted)\n\nResults are written to namegen-output.txt if no output file is specified.\n\n---------------------------------------------------------------------------------', formatter_class=RawTextHelpFormatter)
    parser.add_argument('-f', '--first', help='select a file with first names (one name per line)')
    parser.add_argument('-l','--last', help='select a file with last names (one name per line)')
    parser.add_argument('-o','--output', help='select an output file (doesn\'t need to exist)')
    parser.add_argument('-d','--domain', type=str, help='select a domain to append to the names (e.g., domain.com)')
    parser.add_argument('-r','--randomize', action='store_true', help='randomize the order of names within the final output file (helpful for large lists where user lacks the time to spray entire list)')
    if len(sys.argv)==1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()
    
first = args.first
last = args.last
out = args.output
domain = args.domain


#if no output file specified, write to namegen-output.txt
if args.output is None:
    out = 'namegen-output.txt'

#check if first name file exists
while True:
    if args.first is None:
        break 
    elif os.path.isfile(args.first):
        break
    else:
        print('\nThe file ' + '\'' + args.first + '\''+' does not exist. Please select a file with first names.\n')
        sys.exit()

#check if last name file exists
while True:
    if args.last is None:
        break 
    elif os.path.isfile(args.last):
        break
    else:
        print('\nThe file ' + '\'' + args.last + '\''+' does not exist. Please select a file with last names.\n')
        sys.exit()

#supply options menu format dependent upon domain flag
if args.domain is not None:
    print("\nFormat Options: \n")
    print("|------------------------------|")
    print("| 1 - firstlast@domain.com     |")
    print("| 2 - first.last@domain.com    |")
    print("| 3 - lastfirst@domain.com     |")
    print("| 4 - last.first@domain.com    |")
    print("| 5 - flast@domain.com         |")
    print("| 6 - f.last@domain.com        |")
    print("| 7 - lastf@domain.com         |")
    print("| 8 - last.f@domain.com        |")
    print("| 9 - lfirst@domain.com        |")
    print("| 10 - firstl@domain.com       |")
    print("| 11 - first@domain.com        |")
    print("| 12 - last@domain.com         |")
    print("|______________________________|\n")
else:
    print("\nFormat Options: \n")
    print("|---------------------|")
    print("| 1 - firstlast       |")
    print("| 2 - first.last      |")
    print("| 3 - lastfirst       |")
    print("| 4 - last.first      |")
    print("| 5 - flast           |")
    print("| 6 - f.last          |")
    print("| 7 - lastf           |")
    print("| 8 - last.f          |")
    print("| 9 - lfirst          |")
    print("| 10 - firstl         |")
    print("| 11 - first          |")
    print("| 12 - last           |")
    print("|_____________________|\n")

#ensure selection is within Format Options
while True:
    try:
        choice = int(input("Select desired format #: "))
    except ValueError:
        print('\nPlease select a number from the above options.\n')
    else:
        if choice not in (range(1, 13)):
            print("\nSelect a number from the above options.\n")
        else:
            break

#firstlast
if choice == 1:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = []
    list1 = open(first,'r')
    total = '' 
    for i in list1: 
        fulllist.append(i.strip()) 
    list1.close() 
    for list_item in fulllist: 
        list2 = open(last,'r')
        for i in list2: 
            final = str(list_item)+str(i.lower()) 
            total = total+final 
    list2.close()

    file = open(out, 'w')
    file.write(total)
    file.close()
  

#first.last
elif choice == 2:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = [] 
    list1 = open(first,'r') 
    total = ''
    for i in list1: 
        fulllist.append(i.strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(last,'r')
        for i in list2: 
            final = str(list_item)+"."+str(i.lower()) 
            total = total+final 
    list2.close()

    file = open(out, 'w+')
    file.write(total)
    file.close()

#lastfirst
elif choice == 3:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = []
    list1 = open(last,'r') 
    total = '' 
    for i in list1: 
        fulllist.append(i.strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(first,'r') 
        for i in list2: 
            final = str(list_item)+str(i.lower()) 
            total = total+final
    list2.close()

    file = open(out, 'w+')
    file.write(total)
    file.close()

#last.first
elif choice == 4:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = [] 
    list1 = open(last,'r') 
    total = '' 
    for i in list1: 
        fulllist.append(i.strip())
    list1.close()
    for list_item in fulllist: 
        list2 = open(first,'r') 
        for i in list2: 
            final = str(list_item)+"."+str(i.lower())
            total = total+final 
    list2.close()

    file = open(out, 'w+')
    file.write(total)
    file.close()

#flast
elif choice == 5:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = []
    list1 = open(first,'r') 
    total = '' 
    for i in list1: 
        fulllist.append(i[0].strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(last,'r') 
        for i in list2: 
            final = str(list_item)+str(i.lower()) 
            total = total+final
    list2.close()

    file = open(out, 'w+')
    file.write(total)
    file.close()

#f.last
elif choice == 6:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = [] 
    list1 = open(first,'r')
    total = '' 
    for i in list1: 
        fulllist.append(i[0].strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(last,'r') 
        for i in list2:
            final = str(list_item)+"."+str(i.lower()) 
            total = total+final
    list2.close()

    file = open(out, 'w')
    file.write(total)
    file.close()

#lastf
elif choice == 7:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = [] 
    list1 = open(last,'r') 
    total = '' 
    for i in list1: 
        fulllist.append(i.strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(first,'r') 
        for i in list2: 
            final = str(list_item) + str(i[0].lower() +"\n")
            total = total+final 
    list2.close()

    file = open(out, 'w')
    file.write(total)
    file.close()


#last.f
elif choice == 8:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = [] 
    list1 = open(last,'r') 
    total = '' 
    for i in list1:
        fulllist.append(i.strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(first,'r') 
        for i in list2: 
            final = str(list_item) + "."+str(i[0].lower() +"\n") 
            total = total+final 
    list2.close()

    file = open(out, 'w')
    file.write(total)
    file.close()


#lfirst
elif choice == 9:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = [] 
    list1 = open(last,'r')
    total = '' 
    for i in list1: 
        fulllist.append(i[0].strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(first,'r') 
        for i in list2: 
            final = str(list_item) + str(i.lower()) 
            total = total+final 
    list2.close()

    file = open(out, 'w+')
    file.write(total)
    file.close()

#firstl
elif choice == 10:
    if args.first is None or args.last is None:
        print("\nPlease supply a file containing first and last names using the -f and -l flags (e.g., -f first.txt -l last.txt).")
        sys.exit() 

    fulllist = [] 
    list1 = open(first,'r') 
    total = ''
    for i in list1: 
        fulllist.append(i.strip()) 
    list1.close()
    for list_item in fulllist: 
        list2 = open(last,'r') 
        for i in list2: 
            final = str(list_item) + str(i[0].lower() +"\n") 
            total = total+final
    list2.close()

    file = open(out, 'w+')
    file.write(total)
    file.close()


#first
elif choice == 11:
    if args.first is None:
        print("\nPlease supply a file containing first names using the -f flag (e.g., -f first.txt).")
        sys.exit()
    else:    
        fulllist = [] 

        list1 = open(first,'r') 
        total = '' 
        for i in list1: 
            fulllist.append(i.strip())
        list1.close()
        for list_item in fulllist: 
            final = str(list_item) + "\n" 
            total = total+final

        file = open(out, 'w+')
        file.write(total)
        file.close()

#last
elif choice == 12:
    if args.last is None:
        print("\nPlease supply a file containing last names using the -l flag (e.g., -l last.txt).")
        sys.exit()
    else:
        fulllist = [] 

        list1 = open(last,'r')
        total = '' 
        for i in list1: 
            fulllist.append(i.strip()) 
        list1.close()
        for list_item in fulllist: 
            final = str(list_item) + "\n" 
            total = total+final 

        file = open(out, 'w+')
        file.write(total)
        file.close()


#append the domain (if supplied) and write to file
newarray = []
newtotal = ''
newlist = open(out, 'r')
for i in newlist:
    newarray.append(i.strip())
for i in newarray:
    if domain is not None:
        final2 = str(i).lower() + "@" + domain + "\n"
        newtotal = newtotal + final2
    else:
        final2 = str(i).lower() + "\n"
        newtotal = newtotal + final2

with open(out, 'w') as fp:
    fp.write(newtotal)

#remove duplicate values
completed_lines_hash = set()
deduped = ''

with open(out, 'r') as fp:
    for line in fp:
        hashValue = hashlib.md5(line.rstrip().encode('utf-8')).hexdigest()
        if hashValue not in completed_lines_hash:
            completed_lines_hash.add(hashValue)
            deduped = deduped + line

#handle randomization of output if selected
randomized = ''
if args.randomize:
    with open(out, 'w') as fp:
        fp.write(deduped)
    with open(out,'r') as source:
        data = [ (random.random(), line) for line in source ]
    data.sort()
    with open(out,'w') as target:
        for _, line in data:
            target.write( line )
            randomized = randomized + line
    print("\n" + randomized)
else:
    print("\n" + deduped)
    with open(out, 'w') as fp:
        fp.write(deduped)

#write results to specified file or namegen-output.txt if none specified
print("Results written to file: " + out + ".")
