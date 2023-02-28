#!/usr/bin/python3
import argparse
import string
import os


'''

namegen.py by Michael Castanaro

A name generator useful for OSINT phases in penetration testing/red teaming.

Inspiration from superkojiman's namemash.py.

'''



    


# supply options menu format dependent upon domain flag
def printMethods():
    print("\nFormat Options: \n")
    print("|  1 - firstlast@domain.com")
    print("|  2 - first.last@domain.com")
    print("|  3 - lastfirst@domain.com")
    print("|  4 - last.first@domain.com")
    print("|  5 - flast@domain.com")
    print("|  6 - f.last@domain.com")
    print("|  7 - lastf@domain.com")
    print("|  8 - last.f@domain.com")
    print("|  9 - lfirst@domain.com")
    print("| 10 - firstl@domain.com")
    print("| 11 - first@domain.com")
    print("| 12 - last@domain.com")
    print("| 13 - first_last@domain.com")
    print("| 14 - last_first@domain.com")
    
# Remove lines with speical chars OR normalize chars.
def clean_list(filepath: string):
    returning_list = []
    with open(filepath, 'r') as file:
        lines = file.readlines()

        for name in lines:
            if name.strip().isalnum():  # Check to see if string is only alphanumeric
                returning_list.append(name.strip())
    return list(dict.fromkeys(returning_list)) # Remove Duplicates

def write_file(filepath: string,entries_list: list):
    with open(filepath, 'w') as file:
        for line in entries_list:
            file.write(f"{line}\n")
    

def methodMap(method_choice: int,first_name_list: list, last_name_list: list, domain: string, out_filepath: string):
    
    entries = [] 
    match method_choice:
        case 1:
            # firstlast@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{f}{l}@{domain}")
        case 2:
            # first.last@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{f}.{l}@{domain}")
            
        case 3:
            # lastfirst@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{l}{f}@{domain}")
            
            
        case 4:
            # last.first@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{l}.{f}@{domain}")
            
        case 5:
            # flast@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{f[0]}{l}@{domain}")
                    
        case 6:
            # f.last@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{f[0]}.{l}@{domain}")
                    
        case 7:
            # lastf@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{l}{f[0]}@{domain}")
            
        case 8:
            # last.f@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{l}{f[0]}@{domain}")
            
        case 9:
            # lfirst@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{l[0]}{f}@{domain}")
                    
        case 10:
            # firstl@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{f}{l[0]}@{domain}")
        case 11:
            # first@domain.com
            for f in first_name_list:
                    entries.append(f"{f}@{domain}")
            
        case 12:
            # last@domain.com
            for l in last_name_list:
                entries.append(f"{l}@{domain}")
            
        case 13:
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{f}_{l}@{domain}")
                    
        case 14:
            # last_first@domain.com
            for f in first_name_list:
                for l in last_name_list:
                    entries.append(f"{l}_{f}@{domain}")
        case _:
            printMethods()
            raise ValueError("Method choice invalid")
        
    entries = list(dict.fromkeys(entries)) #Remove Duplicates   
    write_file(filepath=out_filepath, entries_list=entries)

def main():
    parser = argparse.ArgumentParser(description='Namegen takes files comprised of first and/or last names, formats them based upon a selection (e.g., first.last), appends a chosen domain (if specified), and outputs to a file. \n\nExample: ./namegen.py -f first.txt -l last.txt -o output.txt -d domain.com (select a \'#\' when prompted)\n\nResults are written to namegen-output.txt if no output file is specified.\n\n---------------------------------------------------------------------------------', formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('-f', '--first',    help='First Name File',     type=str, required=True)
    parser.add_argument('-l', '--last',     help='Last Name File',      type=str, required=True)
    parser.add_argument('-d', '--domain',   help='Domain Name',         type=str, required=True)
    parser.add_argument('-m', '--method',    help="Method formatting",   type=int, required=True)
    parser.add_argument('-o', '--output',   help='select an output file',   default="namegen-output.txt",   required=False)
    
    args = parser.parse_args()


    # Instead of using sys.exit and printing a error manually, you can raise an exception
    if not os.path.isfile(args.first):
        raise FileNotFoundError(f"File {args.first} not found")
    
    firstname = clean_list(args.first)

    if not os.path.isfile(args.last):
        raise FileNotFoundError(f"File {args.last} not found")
    
    lastname = clean_list(args.last)
    
    methodMap(method_choice=args.method,first_name_list=firstname,last_name_list=lastname,domain=args.domain,out_filepath=args.output)
    
    
    

if __name__ == '__main__':
    main()


