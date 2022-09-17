# namegen.py

Namegen is useful during the OSINT phase of a pen test/red team to assist with account generation. These accounts can later be validated and then used for pass spraying. 

Namegen takes files comprised of first and/or last names, formats them based upon a selection (e.g., first.last), appends a chosen domain (if specified), and outputs to a file.

usage: namegen.py [-h] [-f FIRST] [-l LAST] [-o OUTPUT] [-d DOMAIN]

Example: ./namegen.py -f first.txt -l last.txt -o output.txt -d domain.com (select a '#' when prompted)

Results are written to namegen-output.txt if no output file is specified.
