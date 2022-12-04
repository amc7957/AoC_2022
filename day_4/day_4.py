import numpy as np

#read from text file
with open("data.txt") as f:
    contents = f.readlines()

# remove new line characters
contents = [x.strip() for x in contents]

i = 0
for items in contents:
    elves = items.split(',')
    range_1 = elves[0].split('-')
    range_2 = elves[1].split('-')

    #make a list that contains entire range
    elf_1 = np.arange(int(range_1[0]),int(range_1[1])+1,1).tolist()
    elf_2 = np.arange(int(range_2[0]),int(range_2[1])+1,1).tolist()

    #see what elements overlap
    x = set(elf_1) & set(elf_2)

    #sorry bout the nested if lol
    #Part 1
    #check to see if there is an overlap and if the overlap is either of the full ranges
    # if ((len(x) > 0)):
    #     if (len(x) == len(elf_1)):
    #         i = i +1 
    #     elif (len(x) == len(elf_2)):
    #         i = i+1  
    #     else:     
    #         print('No full overlap')         
    # else:
    #     print('No overlap')   

    #Part 2
    #check to see if there is any overlap
    if ((len(x) > 0)):
            i = i +1      
    else:
        print('No overlap')       

print(i)      