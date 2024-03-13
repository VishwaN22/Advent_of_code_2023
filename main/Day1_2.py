substrings =['one','two','three','four','five','six','seven','eight','nine']

with open ('input.txt','r') as file:

   
    line = file.readline().strip()
    sum =0
    while line:
        first=None
        last = None
        first_index=-1
        last_index=-1
        #for substrings
        for substring in substrings:
            if substring in line:
                if first is None:
                    first = substring
                    first_index=line.find(substring)
                last = substring
                last_index = line.find(substring)

        #for digits
        for char in line:
            if char.isdigit():
                if first is None or first_index>line.index(char):
                    first = char
                if last_index<line.index(char):
                    last = char

        #for first and last to integer
        if last in substrings:
            lastnum = last_index + 1
        else:
            last = int(last)

        if first in substrings:
            firstnum = first_index + 1
        else:
            first = int(first)


        callibration = first + last
        sum+=callibration

        line = file.readline().strip()

    print(sum)

    file.close()