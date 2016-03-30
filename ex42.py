def clean_list(list_to_clean):
    chek_list = []
    for i in list_to_clean:
        if type(i) == float:
            if str(i) not in chek_list:
                chek_list.append(i)
        if i not in chek_list:
            chek_list.append(i)
    return chek_list




def counter(a, b):
    a = str(a)

    a = " ".join(a)

    num1 = a.split()

    num1 = clean_list(num1)
    #print(num1)

    b = str(b)

    b = " ".join(b)
    #print(b)
    num2 = b.split()
    num2 = clean_list(num2)

    # print(num1)
    # print(num2)

    #num2 = clean_list(b)
    #print (num1)
    j = 0
    for i in num1:
        if i in num2:
            j = j + 1

    print (j)

counter(12345, 567)
