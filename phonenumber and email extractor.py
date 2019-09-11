#shebang
#! python3

# importing the necessary modules
import re,pyperclip,pprint

#importing the text from the clipboard
file = pyperclip.paste()
# making the regex for phone and email
pregex = re.compile(r'''(
(\d{3}|\(\d{3}\))?
(-|\s|\.)?
(\d{3})
(\s|-|\.)
(\d{4})
)''',re.VERBOSE)
eregex = re.compile('''(
[A-Za-z0-9._]+
@
[A-Za-z0-9._]+
(\.[A-Za-z0-9._]{2,4})
)''',re.VERBOSE)
# making search for phone and email
plist = pregex.findall(file)
elist = eregex.findall(file)



# making a combined list for searched and selected phone and email
file_handler = []
for i in plist:
    file_handler.append(i[0])
for j in elist:
    file_handler.append(j[0])
    

# transforming the data form the list into a string and pasting on the clipboard
if file_handler != None:
    pyperclip.copy('\n'.join(file_handler))
    print()
    print('Searched material copied to the clipboard !')
else:
    print('Phone numbers or email could not be found in the text on the clipboard ')

    
    
