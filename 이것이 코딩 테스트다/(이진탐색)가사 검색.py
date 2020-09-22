from bisect import bisect_left, bisect_right


def count_by_range(a, s, e):
    right_index = bisect_right(a, e)
    left_index = bisect_left(a, s)

    return right_index - left_index


def solution(words, queries):
    arr = [[] for _ in range(10001)]
    reverse_arr = [[] for _ in range(10001)]
    ans = []

    for w in words:
        arr[len(w)].append(w)
        reverse_arr[len(w)].append(w[::-1])

    for i in range(1, 10001):
        arr[i].sort()
        reverse_arr[i].sort()

    for q in queries:
        # 접미사면
        if q[-1] == "?":
            count = count_by_range(
                arr[len(q)], q.replace("?", "a"), q.replace("?", "z")
            )
        # 접두사면
        else:
            count = count_by_range(
                reverse_arr[len(q)], q[::-1].replace("?", "a"), q[::-1].replace("?", "z")
            )

        ans.append(count)

    print(ans)
    return ans


solution(
    ["frodo", "front", "frost", "frozen", "frame", "kakao"],
    ["fro??", "????o", "fr???", "fro???", "pro?"],
)

