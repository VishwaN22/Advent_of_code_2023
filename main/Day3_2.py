from functools import reduce
def isvalid( row,col):
    directions = [(-1,-1),(-1,0),(-1,1),(0,-1),(0,1),(1,0),(1,-1),(1,1)]
    for dx,dy in directions:
        if(0<=row + dx<len(schematic) and 0<=col + dy<len(schematic[row])):
            if(issymbol(schematic[row + dx][col + dy])):
               boolean_result= True
               index_row=row+dx
               index_col=col+dy
               return boolean_result,index_row,index_col
    return False,0,0      

def issymbol(char):
    return  (char=='*')



with open ('input3.txt','r') as file:

    ratios = file.read()

    schematic = [list(row) for row in ratios.split("\n")]
    gears={}
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
                    result=isvalid(i,x)
                    if(result[0]):

                        star=(result[1],result[2])
                        if star in gears.keys():
                            gears[star].append(int(num))
                        else:
                            gears[star]=[int(num)]
                        break

            #wether or not a digit
            j+=1

sum=0
for value in gears.values():

    if(len(value)>1):
        sum+= reduce(lambda x, y: x * y, value)

print(sum)


                

                





