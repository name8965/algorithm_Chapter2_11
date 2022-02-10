# https://programmers.co.kr/learn/courses/30/lessons/43105


def solution(triangle):
    answer = 0
    N = len(triangle)
    INF=int(1e9)
    memo = [[INF] * (i+1)for i in range(len(triangle))]
    memo[0][0] = triangle[0][0]

    def dp(r, c):
        if not (0 <= r < N and 0 <= c < len(triangle[r])):
            return 0

        if memo[r][c] != INF:
            return memo[r][c]

        memo[r][c] = triangle[r][c] + max(dp(r - 1, c - 1), dp(r - 1, c))
        return memo[r][c]


    for col in range(N):
        dp(N - 1, col)

    print(max(memo[N - 1]))
    answer = max(memo[N - 1])
    return answer


tc = [[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]

solution(tc)
