def solution(snapshots, transactions):
    answer = [[]]
    idx = []
    new_arr = []
    for i in transactions:
        if i[0] not in idx:
            idx.append(i[0])
            new_arr.append(i)
    for i in range(len(new_arr)):
        ck = False
        for j in range(len(snapshots)):
            if new_arr[i][2] == snapshots[j][0]:
                ck = True
                break

        if ck:
            if new_arr[i][1] == "SAVE":
                for j in range(len(snapshots)):
                    if new_arr[i][2] == snapshots[j][0]:
                        temp = int(snapshots[j][1])
                        temp += int(new_arr[i][3])
                        snapshots[j][1] = str(temp)
                        break
            elif new_arr[i][1] == "WITHDRAW":
                for j in range(len(snapshots)):
                    if new_arr[i][2] == snapshots[j][0]:
                        temp = int(snapshots[j][1])
                        temp -= int(new_arr[i][3])
                        snapshots[j][1] = str(temp)
                        break
        else:
            snapshots.append([new_arr[i][2], new_arr[i][3]])
    return snapshots


solution(
    [["ACCOUNT1", "100"], ["ACCOUNT2", "150"]],
    [
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["2", "WITHDRAW", "ACCOUNT1", "50"],
        ["1", "SAVE", "ACCOUNT2", "100"],
        ["4", "SAVE", "ACCOUNT3", "500"],
        ["3", "WITHDRAW", "ACCOUNT2", "30"],
    ],
)
