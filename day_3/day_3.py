import string

#make a key for each letter option
lc = list(string.ascii_lowercase)
uc = list(string.ascii_uppercase)
priority_key = lc + uc

#read from text file
with open("data.txt") as f:
    contents = f.readlines()

# remove new line characters
contents = [x.strip() for x in contents]

#part 1
#break each string of data in half, find the common letter between halves
total_priority = 0
for items in contents:
    L = len(items)
    x = list((set(items[:L//2]) & set(items[L//2:])))
    priority = priority_key.index(x[0])
    total_priority = total_priority + priority + 1

print(total_priority)   

#part 2
#break data into groups of 3, find which letter the 3 have in common
group_list = []
total_priority = 0
for i in range(0, len(contents), 3):
    group_list = contents[i:i + 3]
    x = list((set(group_list[0]) & set(group_list[1]) & set(group_list[2])))
    priority = priority_key.index(x[0])
    total_priority = total_priority + priority + 1

print(total_priority)