# namegen.py

Namegen is useful during the OSINT phase of a pen test/red team to assist with account generation. These accounts can later be validated and then used for pass spraying. 

Namegen takes files comprised of first and/or last names, formats them based upon a selection (e.g., first.last), appends a chosen domain (if specified), and outputs to a file.

usage: namegen.py [-h] [-f FIRST] [-l LAST] [-o OUTPUT] [-d DOMAIN]

Example: ./namegen.py -f first.txt -l last.txt -o output.txt -d domain.com (select a '#' when prompted)

Results are written to namegen-output.txt if no output file is specified.

If no domain is specified, will output only names in specified format.


## Example Screenshots:

![image](https://user-images.githubusercontent.com/66240320/190865244-03c2745d-8def-45b4-9986-f09e344b3e74.png)

![image](https://user-images.githubusercontent.com/66240320/190868619-a3b1702d-4f7e-4d7d-a5ae-be0aabed2ed8.png)

![image](https://user-images.githubusercontent.com/66240320/190867967-5e96c513-098c-4811-9f7f-88c118eed6d3.png)

![image](https://user-images.githubusercontent.com/66240320/190868656-37f8a3b6-69cf-4fa7-a7cb-1310ef95bf5d.png)

If no domain is specified:

![image](https://user-images.githubusercontent.com/66240320/190869038-f3566b40-6452-46eb-a23b-3183223d30b3.png)

![image](https://user-images.githubusercontent.com/66240320/190869057-92cc5062-0d0b-4292-a6c9-11d42ec39a96.png)
