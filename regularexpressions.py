#1.a python program for all cases which can chck a string  contains only a certain set of char(a-z,A-Z,0-9 here)
import re
def is_allowed_specific_char(string):
    charRe = re.compile(r'[^a-zA-Z0-9.]')
    str = charRe.search(string)
    return not bool(str)
print (is_allowed_specific_char("abcdefABCDEF0123452"))
print(is_allowed_specific_char("!12.<:;AZDHarani@#%&*")) 

#2.A pyt prgrm that matches a word containing 'ab'
import re 
def word_match(text):
    patterns='\w*ab.\w+'
    if re.search(patterns,text):
        return "Match Found!"
    else:
        return "Match not found!"
print(word_match("anbcstgffj"))
x=input("String :")
if 'ab' in x:
    print("Match found!")
else:
    print("Match not found!")

#3.A pyt prgrm to check for a num at the end of word/sentence
import re 
def num_at_end(string):
    charRe = re.compile(r"^.*[0-9]$")
    str = charRe.search(string)
    return bool(str)
print(num_at_end("12abcdharani"))
print(num_at_end("anDvach23"))
#4.search num from 0-9 of length b/w 1-3 lngth in a given string
results = re.finditer(r"([0-9]{1,3})","Excercises number 1,34,56,12,4546 and345 are important")
print("Number of length 1 to 3")
for n in results:
    print(n.group(0))

#5.A prgrm to match a string that contains only uppercase leters
def uppercase_str(string):
    charRe = re.compile(r'[^A-Z.]')
    str=charRe.search(string)
    return not bool(str)
print(uppercase_str("DHARANIMOUNICHINNU"))
print(uppercase_str("dharanimounichinnu"))
