with open ('input.txt','r') as file:

   
    line = file.readline().strip()
    sum =0
    while line:
        first=None
        last = None
        for char in line:
            if char.isdigit():
                if first is None:
                    first = char
                last = char

        callibration = int(first + last)
        sum+=callibration

        line = file.readline().strip()

    print(sum)

    file.close()