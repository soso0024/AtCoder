N = int(input())
A = list(map(int, input().split()))


def cal(a1, a2):
    return a1 * a2


ans = []
for i in range(N - 1):
    ans.append(str(cal(A[i], A[i + 1])))

print(" ".join(ans))
