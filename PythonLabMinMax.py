Finish = 99999
Max = -9999
Min = 9999
T = int(input())

while T != Finish:
    if T > Max:
        Max = T
        print(Max, Min)
    if T < Min:
        Min = T
        print(Max, Min)
        break
else:
    print(Max, Min)




