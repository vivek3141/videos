import sys

with open(sys.argv[1], "r") as f:
    code = f.read()

li = []
ind = 0
while(True):
    ind = code.find("class", start=ind)
    if ind == -1:
        break
    li.append(code[ind+1:code.find(" ", start=ind+2)])

print(li)

