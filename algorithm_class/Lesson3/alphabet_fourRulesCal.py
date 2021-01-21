def calMax():
    if cnt == n:
        return

    if operSym[oper_cnt] == '-':
        for i in range(1, 4):
        alpha[cnt] = i
        calMax(cnt+1, oper_cnt+1)
    else:
        alpha[cnt] = 4


equa = input()
alpha = []
operSym = []
for i in range(n):
    if i % 2 == 0:
        operSym.append(equa[i])
    else:
        alpha.append(equa[i])
calMax(cnt, oper_cnt)
