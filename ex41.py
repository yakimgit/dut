def clean_list(list_to_clean):
    chek_list = []
    for i in list_to_clean:
        if type(i) == float:
            if str(i) not in chek_list:
                chek_list.append(i)
        if i not in chek_list:
            chek_list.append(i)
    print (chek_list)

#clean_list([1, 2, 1, 1, 3, 4, 5, 4, 6, '2', 7, 8, 9, 0, 1, 2, 3, 4, 5])
#clean_list([32, 32.1, 32.0, -123])
#clean_list([1, 1.0, '1', -1, 1])
#clean_list(['qwe', 'reg', 'qwe', 'REG'])
