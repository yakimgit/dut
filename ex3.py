i = 0
while(i < 1000000):
    result = ""
    zero = 7 - len(str(i))
    for j in range(zero,zero>0,-1):
        result = result + str(0)
    result = result + str(i)

    firstHalf = result[0] + result[1] + result[2]
    seconHalf = result[3] + result[4] + result[5]

    if(firstHalf == seconHalf):
        print result, "Happy ticket"

    i = i + 1
