def isvalid( row,col):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]
    for dx,dy in directions:
        if(0<=row + dx<len(schematic) and 0<=col + dy<len(schematic[row])):
            if(issymbol(schematic[row + dx][col + dy])):
                return True
    return False      

def issymbol(char):
    return  (not char.isdigit() and char!='.')



with open ('input3.txt','r') as file:

    ratios = file.read()

    schematic = [list(row) for row in ratios.split("\n")]
    sum=0
    for i,row in enumerate(schematic):

        j =0
        
        while j<len(row):

            #if a digit
            if(schematic[i][j].isdigit()):
                num = schematic[i][j]
                init_j = j

                #get the entire string of number
                while((j+1)<len(row) and schematic[i][j+1].isdigit()):
                    j=j+1
                    num += schematic[i][j]
                

                #see if it is valid and add to sum

                for x in range (init_j,j+1):
                    if(isvalid(i,x)):
                        sum+=int(num)
                        break

            #wether or not a digit
            j+=1


print(sum)


                

                





