import re 

s = "dwa:"
hBox = re.compile("^\s*(\w)+\:?\s*((\-?\w)*)?($|(\s*\/{2}))")
text = re.compile("(\s)*(\w)+\:?")
print(hBox.match(s))
print(re.split("\s+", s.strip()))