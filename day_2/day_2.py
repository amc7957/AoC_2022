#read from text file
with open("data.txt") as f:
    rps_list = f.readlines()

# remove new line characters
rps_list = [x.strip() for x in rps_list]
print(len(rps_list))
moves = [rps_list[x:x+1] for x in range(0, len(rps_list))]

#part 1, present the possible cases for rps
# def turn(move):
#     #print(move)
#     match move:
#         case ['A X']:
#             return [3,1]
#         case ['A Y']:
#             return [6,2]
#         case ['A Z']:    
#             return [0,3]
#         case ['B X']:
#             return [0,1]
#         case ['B Y']:
#             return [3,2]
#         case ['B Z']:    
#             return [6,3]
#         case ['C X']:
#             return [6,1]
#         case ['C Y']:
#             return [0,2]
#         case ['C Z']:    
#             return [3,3] 

#part 2
def turn(move):
    #print(move)
    match move:
        case ['A X']:
            return [3,0]
        case ['A Y']:
            return [1,3]
        case ['A Z']:    
            return [2,6]
        case ['B X']:
            return [1,0]
        case ['B Y']:
            return [2,3]
        case ['B Z']:    
            return [3,6]
        case ['C X']:
            return [2,0]
        case ['C Y']:
            return [3,3]
        case ['C Z']:    
            return [1,6]  

total_score = 0
for x in moves:
    score = sum(turn(x))
    total_score = total_score + score   
print(total_score)
        