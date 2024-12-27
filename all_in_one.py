text="This is text to find length"
length=len(text)
Uppercase=text.upper()
replaces=text.replace("length", "Modules")
Splitted=text.split()
substring="to"
if substring in text:
    print(length,"\n",Uppercase,"\n",replaces,"\n",Splitted[5])
else:
    print("Not found")
