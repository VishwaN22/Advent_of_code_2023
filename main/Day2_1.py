import re
with open ('input2.txt','r') as file:

    line= file.readline()
    sum =0

    while line:

        dict={'red':[],'blue':[],'green':[]}

        game= re.split(',|;|:',line)

        for i in range(1,len(game)):

            item = game[i].split() #one red or blue or green per game
            item[0]=int(item[0])
            dict[item[1]].append(item[0]) 
            
            

        
        #after one game finding min
        max_red=max(dict['red'])
        max_blue=max(dict['blue'])
        max_green=max(dict['green'])

        power = max_blue*max_green*max_red
           
            
            
        sum+=power
        line=file.readline()

    print(sum)
    file.close()