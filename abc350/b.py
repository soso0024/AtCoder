N, Q = map(int, input().split())
T = list(map(int, input().split()))

if Q != len(T):
    print("error")
    exit()

count_dict = {}

for num in T:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

count_plus = 0
for num, count in count_dict.items():
    if count % 2 == 0:
        count_plus += 1


# print(f"N: {N}\nQ: {Q}\nPlus: {count_plus}")
print(N - len(count_dict) + count_plus)
