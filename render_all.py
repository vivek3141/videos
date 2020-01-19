import sys

with open(sys.argv[1], "r") as f:
    code = f.read()
    
ind = 0
while(True):
    ind = code.find("class", start=ind)
