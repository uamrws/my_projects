def check_price(prices):
    n = ans = len(prices)
    for i in range(n):
        j = i + 1
        while j < n:
            if prices[j] == prices[j - 1] - 1:
                ans += 1
            else:
                break
            j += 1
    return ans


def check_price(prices):
    ans = 1
    prev = 1
    for i in range(1, len(prices)):
        if prices[i] == prices[i - 1] - 1:
            prev += 1
        else:
            prev = 1
        ans += prev
    return ans


print(check_price([3, 2, 1, 4]))
print(check_price([4, 3, 2, 1]))
print(check_price([8, 6, 7, 7]))
print(check_price([1]))

7
10
4
1
