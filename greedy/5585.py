def changeCount():
    count = 0
    change = 1000 - n
    coins = [500, 100, 50, 10, 5, 1]
    for coin in coins:
        if change == 0:
            break
        count += change // coin
        change %= coin

    return count


n = int(input())
print(changeCount())
