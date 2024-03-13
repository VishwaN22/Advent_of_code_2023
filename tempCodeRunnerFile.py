
steps=0
for direction in directions:

    if(pos!='ZZZ'):
        
        if(direction=='L'):

            pos = dict[pos][0]
        
        else:
            pos = dict[pos][1]

        steps+=1   

    else:

        break

print(steps)

