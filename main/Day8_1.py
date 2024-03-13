

with open('input8.txt','r') as file:

    content=file.read().strip().split('\n')


directions=list( content[0] )
dict={}
for i in range (2,len(content)) :

    key,tuples = content[i].strip().split('=')

    key=key.strip()

    values = tuple(value.strip() for value in tuples.strip()[1:-1].split(','))

    dict[key]= values

   


pos='AAA'
steps=0

i=0
while(i<len(directions) ):

    direction = directions[i]
    if(pos!='ZZZ'):
        
        if(direction=='L'):

            pos = dict[pos][0]
        
        else:
            pos = dict[pos][1]

        steps+=1   

    else:

        break

    i+=1

    if(i==len(directions) and pos!='ZZZ'):
        i=0

print(steps)

