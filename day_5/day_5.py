#read from text file
from re import L


with open("data.txt") as f:
    contents = f.readlines()

# remove new line characters
contents = [x.strip() for x in contents]  

placement = contents[0:8]
directions = contents[10:512]
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
for items in reversed(placement):
    #print(len(items))
    if(len(items)<32):
        pass
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

big_list =[col_1,col_2,col_3,col_4,col_5,col_6,col_7,col_8,col_9]

for i in range(9):
    remove_space = [x.strip(' ') for x in big_list[2]]
    big_list[i] = [ele for ele in big_list[i] if ele.strip()]
    

for items in directions:
    items = items.split()
    quantity = int(items[1])
    print(quantity)
    init_loc = int(items[3])-1
    print(init_loc)
    final_loc = int(items[5])-1
    print(final_loc)

    #for part 1
    #for i in range(quantity):
    #    big_list[final_loc].append(big_list[init_loc].pop())

    #for part 2
    print(big_list)
    chunk = big_list[init_loc][-1*quantity:]
    del big_list[init_loc][-1*quantity:]
    print(chunk[0:3])
    big_list[final_loc].extend(chunk[0:quantity])
    #big_list[final_loc].append(big_list[init_loc].pop())

final_list = []    
for i in range(9):
    final_list.append(big_list[i][-1])
#print(big_list)
print(final_list)