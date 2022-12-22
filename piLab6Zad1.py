try:
    file = open("text.txt", 'r', encoding="utf-8")
    with file as f:
        w_j = f.readline().split(": ")
        w_j = w_j[1].split(",")
except:
    print(EOFError)
    print(FileNotFoundError)

Subs_j = ("CO", "CO2", "CH4")
mas = []
def a():
     y_j = input()
     y_i = input()
     w_m = 0
     count = 0
     zcm = 0
     for k in Subs_j:
        for indexYJ in y_j:
            w_m += indexYJ * w_j[count]
            zcm += 0.291 - 0.08 * w_m
            mas.append(k)
            mas.append(indexYJ)
            mas.append(zcm)
            w_m = 0
            zcm = 0
        for i in y_i:
            w_m += i * w_j[count]
            zcm += 0.291 - 0.08 * w_m
            mas.append(k)
            mas.append(indexYJ)
            mas.append(zcm)
            w_m = 0
            zcm = 0
        count += 1
     return zcm
print(a())
try:
    file1 = open("final.txt", 'w', encoding="utf-8")
    file1.write("вещество |\t Ошибка |\t Ошибка\n")
    file1.write("-----------------------------\n")
    for i in range(len(mas)):
        file1.write("\t\t{0}\t\t| \t{1:.5f}\n| \t{1:.5f}\n".format(i+1, mas[i]))
except:
    print(FileNotFoundError)
