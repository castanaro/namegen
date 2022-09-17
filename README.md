# namegen.py

Namegen is useful during the OSINT phase of a pen test/red team to assist with account generation. These accounts can later be validated and then used for pass spraying. 

Namegen takes files comprised of first and/or last names, formats them based upon a selection (e.g., first.last), appends a chosen domain (if specified), and outputs to a file.

usage: namegen.py [-h] [-f FIRST] [-l LAST] [-o OUTPUT] [-d DOMAIN]

Example: ./namegen.py -f first.txt -l last.txt -o output.txt -d domain.com (select a '#' when prompted)

Results are written to namegen-output.txt if no output file is specified.

If no domain is specified, will output only names in specified format.

![image](https://user-images.githubusercontent.com/66240320/190865244-03c2745d-8def-45b4-9986-f09e344b3e74.png)

![image](https://user-images.githubusercontent.com/66240320/190867967-5e96c513-098c-4811-9f7f-88c118eed6d3.png)

![image](https://user-images.githubusercontent.com/66240320/190868014-f2cfc9ee-eee4-4400-a088-6883f5491918.png)

![image](https://user-images.githubusercontent.com/66240320/190867990-704f3c6c-ebeb-4b0a-b448-f0ae00cc735d.png)
