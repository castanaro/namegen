# namegen.py

Namegen is useful during the OSINT phase of a pen test/red team to assist with account generation. These accounts can later be validated and then used for pass spraying. 

Namegen takes files comprised of first and/or last names, formats them based upon a selection (e.g., first.last), appends a chosen domain (if specified), and outputs to a file.

usage: namegen.py [-h] [-f FIRST] [-l LAST] [-o OUTPUT] [-d DOMAIN]

Example: ./namegen.py -f first.txt -l last.txt -o output.txt -d domain.com (select a '#' when prompted)

Results are written to namegen-output.txt if no output file is specified.

If no domain is specified, will output only names in specified format.

Tip: A helpful place to start could be pulling down most common first and last names from Daniel Miessler's SecLists or using the provided lists within this repo. Enjoy!

https://github.com/danielmiessler/SecLists/tree/master/Usernames

### Flags:

-h help

-f accepts a file with first names

-l accepts a file with last names

-o accepts an output file, if ommitted, writes to namegen-output.txt

-d accepts a domain e.g., domain.com

-r randomizes the output which can be helpful for large alphabetical lists where the user won't have enough time to validate all of them

### Example Screenshots:

![image](https://user-images.githubusercontent.com/66240320/190875751-18dac881-d667-45f2-a894-8410653cb97b.png)

![image](https://user-images.githubusercontent.com/66240320/190868619-a3b1702d-4f7e-4d7d-a5ae-be0aabed2ed8.png)

![image](https://user-images.githubusercontent.com/66240320/190867967-5e96c513-098c-4811-9f7f-88c118eed6d3.png)

![image](https://user-images.githubusercontent.com/66240320/190868656-37f8a3b6-69cf-4fa7-a7cb-1310ef95bf5d.png)

If no domain is specified:

![image](https://user-images.githubusercontent.com/66240320/190869038-f3566b40-6452-46eb-a23b-3183223d30b3.png)

![image](https://user-images.githubusercontent.com/66240320/190869057-92cc5062-0d0b-4292-a6c9-11d42ec39a96.png)

If -r is specified, output will be randomized:

![image](https://user-images.githubusercontent.com/66240320/190875779-3ca2e03f-2823-446c-9e0d-6f112bcfa25f.png)

![image](https://user-images.githubusercontent.com/66240320/190875812-b7653e54-32da-4fd9-a6be-beac41d08604.png)
