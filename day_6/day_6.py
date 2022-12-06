with open("data.txt") as f:
    contents = f.readlines()

contents = [*contents[0]]   

#for part 1 change the 14 to a 4
for x in range(len(contents)):
    a = contents[x:x+14]
    dupes = [x for n, x in enumerate(a) if x in a[:n]] 
    if (dupes == []):
        print(x+14)
        break
    else:
        pass