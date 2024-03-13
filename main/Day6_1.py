


product=1
with open('sample6.txt','r') as fp:

    file=fp.read().split('\n')
    list1=file[0].split(':')
    list2=file[1].split(':')
    
    time = list1[1].split()
    distance = list2[1].split()

    for i in range (0,len(time)):
        count=0
        n=1

        while(n<((int(time[i])/2))):
            
            if(((int(time[i])-n)*n)>int(distance[i])):

                count+=1
            n+=1
               

        product=product*count*2

print(product)

