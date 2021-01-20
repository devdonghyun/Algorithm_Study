def maxBenefit(n, price):
    maxBenefit = 0
    for i in range(n):
        for j in range(i+1, n):
            if price[i] < price[j]:
                if maxBenefit < (price[j] - price[i]):
                    maxBenefit = price[j] - price[i]
    print(maxBenefit)


n = int(input())
price = [int(x) for x in input().split()]
maxBenefit(n, price)
