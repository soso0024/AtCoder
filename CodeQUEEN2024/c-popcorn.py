num_shops, num_kinds = map(int, input().split())
shop_list = []

for _ in range(num_shops):
    S = input()
    shop_list.append(S)

# print(shop_list)

ans = num_kinds
for bit in range(2**num_shops):
    ans_shop = 0
    current_kinds = []
    for i in range(num_shops):
        if (bit >> i) & 1:
            ans_shop += 1
            for j in range(num_kinds):
                if shop_list[i][j] == "o":
                    current_kinds.append(j)

    if len(set(current_kinds)) == num_kinds:
        ans = min(ans, ans_shop)

print(ans)
