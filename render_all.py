import sys

with open(sys.argv[1], "r") as f:
    code = f.read()

li = []
ind = 0
while(True):
    ind = code.find("class", ind+1)
    if ind == -1:
        break
    head = code[ind+6:code.find(":", ind+7)]
    if head.find("(") == -1:
        li.append(head)
    else:
        li.append(head.replace(head[head.index("("):head.index(")")], ""))

print(li)

