#read from text file
with open("data.txt") as f:
    cals_list = f.readlines()

# remove new line characters
cals_list = [x.strip() for x in cals_list]

#add cals for each elf using whitespace as the delineation 
elf_list = []
total = 0
for items in cals_list:
    if items != '':
        total = total + int(items)
    elif items == '':   
        elf_list.append(total)
        total = 0

#answer for part 1 AoC 2022
print(max(elf_list))  

#order list descending and add top 3 values
elf_list.sort(reverse=True)
final = elf_list[0]+elf_list[1]+elf_list[2]

#answer for part 2 AoC 2022
print(final)