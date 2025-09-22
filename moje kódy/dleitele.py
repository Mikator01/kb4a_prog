def delitel(cislo: int):
    delitel_list = []
    for i in range(1, cislo + 1):
        if cislo % i == 0:
            delitel_list.append(i)
    print(delitel_list)
    return delitel_list

#tsest#
delitel(500)