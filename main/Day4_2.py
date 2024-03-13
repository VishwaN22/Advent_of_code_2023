with open('input4.txt','r') as file:

    contents = file.read().split('\n')
    
    
    dictionary = {}
    
    for index,line in enumerate(contents):

        id = int(line.split(':')[0][4:])
        dictionary[id] = 1
    
    for index,line in enumerate(contents):

        card = line.split('|')
        values=card[0].split(':')
        winning =values[1].split()
        available=card[1].split()
        total=0

        n = dictionary[index+1]

        
        while n>0:
            for num in available:
                if num in winning:
                    total+=1

            while total>0:
                i=index + total

                if i<len(contents):
                    dictionary[i+1]+=1  

                else:
                    break

                total-=1

            n-=1

    sum=0  
    for keys,values in dictionary.items():
        sum+=values


    print(sum)

    
