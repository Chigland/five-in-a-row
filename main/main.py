chessBord = [['-']*10 for i in range(10)]
lis2 = ['A','B','C','D','E','F','G','H','I','J']
def printChess():
    print('——————————————————————')
    print('  1 2 3 4 5 6 7 8 9 10')
    for i in range(10):
        for j in range(10):
            if j == 9:
                print(chessBord[i][j])
            elif j == 0:
                print(lis2[i] + ' ' +chessBord[i][j],end=' ')
            else:
                print(chessBord[i][j],end=' ')
    print('——————————————————————')
def playChess():
    temp = 0
    n = 0
    temp1 = 0
    temp2 = 0
    temp3 = 0
    flag = 0
    while temp == 0:
        while flag != 1:
            printChess()
            blackChoice = input('请输入*棋子坐标（例如A1）：')
            if int(blackChoice[1]) > 10 or int(blackChoice[1]) < 1:
                print('***您输入的坐标有误，请重新输入！***')
                pass
            else:
                for i in range(10):
                    if lis2[i] == blackChoice[0]:
                        if chessBord[i][int(blackChoice[1]) - 1] == '-':
                            chessBord[i][int(blackChoice[1]) - 1] = '*'
                            n = i
                            flag = 1
                            # 遍历列
                            lis1 = []
                            flag1 = 0
                            for i in range(10):
                                lis1.append(chessBord[i][int(blackChoice[1])-1])
                            if n == 0:
                                flag1 = flag1
                            else:
                                for item in lis1[n-1::-1]:
                                    if item == chessBord[n][int(blackChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if n ==9:
                                flag1 = flag1
                            else:
                                for item in lis1[n + 1:10:1]:
                                    if item == chessBord[n][int(blackChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if flag1 >= 4:
                                temp1 = 1
                            # 遍历行
                            flag1 = 0
                            if int(blackChoice[1])-1 ==0:
                                flag1 = flag1
                            else:
                                for item in chessBord[n][int(blackChoice[1])-2:0:-1]:
                                    if item == chessBord[n][int(blackChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if int(blackChoice[1])-1 == 9:
                                flag1 = flag1
                            else:
                                for item in chessBord[n][int(blackChoice[1]):10:1]:
                                    if item == chessBord[n][int(blackChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if flag1 >= 4:
                                temp2 = 1
                            # 遍历对角线
                            flag1 = 0
                            if int(blackChoice[1])-1 == 0:
                                flag1 = flag1
                            else:
                                for i in range(int(blackChoice[1]) - 2, -1, -1):
                                    for j in range(10):
                                        if abs(j - n) == abs(i - int(blackChoice[1]) + 1):
                                            if chessBord[j][i] == chessBord[n][int(blackChoice[1]) - 1]:
                                                flag1 += 1
                                            else:
                                                flag1 = flag1
                                                break
                                    if flag1 == 0:
                                        break
                            if int(blackChoice[1])-1 == 9:
                                flag1 = flag1
                            else:
                                for i in range(int(blackChoice[1]) , 10, 1):
                                    for j in range(10):
                                        if abs(j - n) == abs(i - int(blackChoice[1]) + 1):
                                            if chessBord[j][i] == chessBord[n][int(blackChoice[1]) - 1]:
                                                flag1 += 1
                                            else:
                                                flag1 = flag1
                                                break
                                    if flag1 == 0:
                                        break
                            if flag1 >= 4:
                                temp3 = 1
                            temp = temp3+temp2+temp1
                            if temp != 0:
                                printChess()
                                print('*棋胜利！***')
                                flag == 2
                                break
                            pass
                        elif chessBord[i][int(blackChoice[1]) - 1] == '*' or chessBord[i][
                            int(blackChoice[1]) - 1] == 'o':
                            print('******您输入位置已有其他棋子，请重新输入！')
                            flag = 2
                            pass
            if flag == 0:
                print('***您输入的坐标有误，请重新输入！***')
        if temp != 0 :
            flag = 1
        else:
            flag = 0
        while flag != 1:
            printChess()
            whiteChoice = input('请输入o棋子坐标（例如J5）：')
            if int(whiteChoice[1]) > 10 or int(whiteChoice[1]) < 1:
                print('***您输入的坐标有误，请重新输入！***')
                pass
            else:
                for i in range(10):
                    if lis2[i] == whiteChoice[0]:
                        if chessBord[i][int(whiteChoice[1]) - 1] == '-':
                            chessBord[i][int(whiteChoice[1]) - 1] = 'o'
                            n = i
                            flag = 1
                            # 遍历列
                            lis1 = []
                            flag1 = 0
                            for i in range(10):
                                lis1.append(chessBord[i][int(whiteChoice[1]) - 1])
                            if n == 0:
                                flag1 = flag1
                            else:
                                for item in lis1[n - 1::-1]:
                                    if item == chessBord[n][int(whiteChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if n == 9:
                                flag1 = flag1
                            else:
                                for item in lis1[n + 1:10:1]:
                                    if item == chessBord[n][int(whiteChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if flag1 >= 4:
                                temp1 = 1
                            # 遍历行
                            flag1 = 0
                            if int(whiteChoice[1]) - 1 == 0:
                                flag1 = flag1
                            else:
                                for item in chessBord[n][int(whiteChoice[1]) - 2:0:-1]:
                                    if item == chessBord[n][int(whiteChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if int(whiteChoice[1]) - 1 == 9:
                                flag1 = flag1
                            else:
                                for item in chessBord[n][int(whiteChoice[1]):10:1]:
                                    if item == chessBord[n][int(whiteChoice[1]) - 1]:
                                        flag1 += 1
                                    else:
                                        flag1 = flag1
                                        break
                            if flag1 >= 4:
                                temp2 = 1
                            # 遍历对角线
                            flag1 = 0
                            if int(whiteChoice[1]) - 1 == 0:
                                flag1 = flag1
                            else:
                                for i in range(int(whiteChoice[1]) - 2, -1, -1):
                                    for j in range(10):
                                        if abs(j - n) == abs(i - int(whiteChoice[1]) + 1):
                                            if chessBord[j][i] == chessBord[n][int(whiteChoice[1]) - 1]:
                                                flag1 += 1
                                            else:
                                                flag1 = flag1
                                                break
                                    if flag1 == 0:
                                        break
                            if int(whiteChoice[1]) - 1 == 9:
                                flag1 = flag1
                            else:
                                for i in range(int(whiteChoice[1]), 10, 1):
                                    for j in range(10):
                                        if abs(j - n) == abs(i - int(whiteChoice[1]) + 1):
                                            if chessBord[j][i] == chessBord[n][int(whiteChoice[1]) - 1]:
                                                flag1 += 1
                                            else:
                                                flag1 = flag1
                                                break
                                    if flag1 == 0:
                                        break
                            if flag1 >= 4:
                                temp3 = 1
                            temp = temp3 + temp2 + temp1
                            if temp != 0:
                                printChess()
                                print('o棋胜利！***')
                                flag == 0
                                break
                            pass
                        elif chessBord[i][int(whiteChoice[1]) - 1] == '*' or chessBord[i][
                            int(whiteChoice[1]) - 1] == 'o':
                            print('******您输入位置已有其他棋子，请重新输入！')
                            flag = 2
                            pass
            if flag == 0:
                print('***您输入的坐标有误，请重新输入！***')
        if temp!= 0 :
            flag = 1
        else:
            flag = 0
playChess()

