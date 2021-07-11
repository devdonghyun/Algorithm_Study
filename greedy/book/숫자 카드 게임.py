# greedy - 숫자 카드 게임
# 굳이 입력 내용을 이중 리스트에 저장할 필요 없음


def numberCardGame():
    card_list = []
    for i in range(n):
        min_num = min(grid[i])
        card_list.append(min_num)

    return max(card_list)


n, m = map(int, input().split())
grid = []
for i in range(n):
    for j in range(m):
        row = [int(x) for x in input().split()]
        grid.append(row)

print(numberCardGame())
