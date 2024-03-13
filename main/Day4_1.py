with open('input4.txt','r') as file:

    line = file.readline()
    sum=0

    while (line):

        card = line.split('|')
        values=card[0].split(':')
        winning =values[1].split()
        available=card[1].split()
        total=0

        for num in available:
            if num in winning:
                total+=1

        sum+= int(2**(total-1))



        line = file.readline()


print(sum)