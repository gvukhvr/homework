#1
import re

pattern = r'ab*'

def match_pattern(string):
    return re.fullmatch(pattern, string) is not None

print(match_pattern("a"))    
print(match_pattern("ab"))   
print(match_pattern("ac"))   



#2
import re
pattern = r'ab{2,3}'
def match_pattern(string):
    if re.fullmatch(pattern, string):
        return True 
    else:
        return False

print(match_pattern("ab"))   
print(match_pattern("abb"))   
print(match_pattern("abbb")) 
print(match_pattern("abbbb")) 

#3
import re

pattern = r'[a-z]+_[a-z]+'

def findletter(string):
    return re.findall(pattern, string)

print(findletter("hello_world"))  
print(findletter("great")) 

#4
import re
pattern = r'[A-Z][a-z]+'

def find_sequences(string):
    return re.findall(pattern, string)

print(find_sequences("HelloWorld")) 
print(find_sequences("Hello_Great"))  

#5
import re
pattern = r'a.*b$'

def match_pattern(string):
    if re.fullmatch(pattern, string):
        return True 
    else:
        return False

print(match_pattern("ab"))       
print(match_pattern("aaaab")) 
print(match_pattern("ac"))      

#6
import re
pattern = r'[ ,.]'

def replace(string):
    return re.sub(pattern, ':', string)

print(replace("Hello, world"))  
print(replace("Funny day.")) 

#7
import re
def change(str):
    components = str.split('_')
    return components[0] + ''.join(x.title() for x in components[1:])

print(change("hello_world"))  # helloWorld
print(change("python_is_great"))  # pythonIsGreat

