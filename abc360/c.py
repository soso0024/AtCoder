N = int(input())
A = list(map(int, input().split()))
W = list(map(int, input().split()))

num_boxes = N

boxes = [[] for _ in range(num_boxes)]

# print(boxes)
# [[], [], [], [], []]

for i in range(num_boxes):
    box_index = A[i] - 1  # インデックスは0始まりなので1を引く
    boxes[box_index].append(W[i])

# Check Values
# for i in range(num_boxes):
#     print(f"Box {i+1}: {boxes[i]}")
# Box 1: []
# Box 2: [33, 40]
# Box 3: [2, 12]
# Box 4: []
# Box 5: [16]

cost = 0
for i in range(num_boxes):
    if len(boxes[i]) >= 2:
        cost += sum(boxes[i]) - max(boxes[i])

print(cost)

# print([0] * 10)
# [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
