#read from text file
with open("data.txt") as f:
    contents = f.readlines()

# remove new line characters
contents = [x.strip() for x in contents]  

placement = contents[0:8]
print(placement)
directions = contents[11:512]
#print(directions)

col_1 = []
col_2 = []
col_3 = []
col_4 = []
col_5 = []
col_6 = []
col_7 = []
col_8 = []
col_9 = []
for items in placement:
    if(len(items)<32):
        col_9.append(' ')
    else:
        col_9.append(items[33])    
    col_1.append(items[1]) 
    col_2.append(items[5]) 
    col_3.append(items[9]) 
    col_4.append(items[13]) 
    col_5.append(items[17]) 
    col_6.append(items[21]) 
    col_7.append(items[25]) 
    col_8.append(items[29])  

print(list(reversed(col_1)))
print(list(reversed(col_2)))
print(list(reversed(col_3)))
print(list(reversed(col_4)))
print(list(reversed(col_5)))
print(list(reversed(col_6)))
print(list(reversed(col_7)))
print(list(reversed(col_8)))
print(list(reversed(col_9)))

for items in directions:
    quantity = items[1]
    init_loc = items[3]
    final_loc = items[5]