n = int(input().strip())
ar = input().strip()

count = 0
cur = 0

for step in ar:
    if cur == -1 and step == "U":
        count += 1
        cur = 0
    else:
        cur = cur - 1 if step == "D" else cur + 1
        
print(count)