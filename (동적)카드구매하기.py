# dp[i] : i개 카드 구매시 가장 비싼 가격

N = int(input())
card = list(map(int, input().split()))
dp = [0] * (N + 1)
for i in range(len(card)):
    dp[i + 1] = card[i]
for i in range(2, len(card) + 1):
    for j in range(1, (i // 2) + 1):
        dp[i] = max(dp[i], dp[j] + dp[i - j])
print(dp[N])
