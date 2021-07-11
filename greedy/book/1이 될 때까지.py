# greedy - 1이 될 때까지
# /, // 주의해서 사용하기

def untilOne(n, k):
    count = 0
    while (n != 1):
        if n % k == 0:
            # n /= k
            n //= k  # n이 실수가 되는 일 방지
        else:
            n -= 1
        count += 1

    return count


n, k = map(int, input().split())
print(untilOne(n, k))
