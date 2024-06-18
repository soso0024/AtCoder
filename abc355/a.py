A, B = map(int, input().split())

candidates = [1, 2, 3]

if A != B:
    # print("Can Decide")
    bad_guy = [
        candidate for candidate in candidates if candidate != A and candidate != B
    ]
    print(bad_guy[0])
else:
    print(-1)

# リスト内包表記（List Comprehensions）は、Pythonの強力で簡潔な構文で、リストを生成する方法です。通常のループや`map`関数を使うよりも簡潔にリストを生成できます。リスト内包表記は、特定の条件を満たす要素をリストに追加したり、リストの各要素に対して操作を行ったりする場合に特に便利です。

# 基本的な構文は次のとおりです：

# ```python
# [式 for 変数 in イテラブル]
# ```

# 条件を付ける場合は、`if`を追加します：

# ```python
# [式 for 変数 in イテラブル if 条件]
# ```

# ### 使用例

# 1. **基本的な例**

# リストの各要素を2倍にする例です。

# ```python
# numbers = [1, 2, 3, 4, 5]
# doubled = [x * 2 for x in numbers]
# print(doubled)  # 出力: [2, 4, 6, 8, 10]
# ```

# 2. **条件付きリスト内包表記**

# リストの要素のうち、偶数のみを抽出する例です。

# ```python
# numbers = [1, 2, 3, 4, 5, 6]
# evens = [x for x in numbers if x % 2 == 0]
# print(evens)  # 出力: [2, 4, 6]
# ```

# 3. **ネストされたループ**

# 二重ループを使用して、2つのリストの全ての組み合わせを生成する例です。

# ```python
# colors = ['red', 'blue']
# objects = ['ball', 'cube']
# combinations = [(color, obj) for color in colors for obj in objects]
# print(combinations)  # 出力: [('red', 'ball'), ('red', 'cube'), ('blue', 'ball'), ('blue', 'cube')]
# ```

# 4. **文字列操作**

# 文字列の各文字を大文字に変換する例です。

# ```python
# text = "hello"
# uppercased = [char.upper() for char in text]
# print(uppercased)  # 出力: ['H', 'E', 'L', 'L', 'O']
# ```

# 5. **辞書のキーと値の操作**

# 辞書のキーと値を入れ替える例です。

# ```python
# original_dict = {'a': 1, 'b': 2, 'c': 3}
# swapped_dict = {value: key for key, value in original_dict.items()}
# print(swapped_dict)  # 出力: {1: 'a', 2: 'b', 3: 'c'}
# ```

# 6. **多重条件**

# 複数の条件を指定する例です。

# ```python
# numbers = [1, 2, 3, 4, 5, 6]
# filtered = [x for x in numbers if x % 2 == 0 and x > 3]
# print(filtered)  # 出力: [4, 6]
# ```

# ### リスト内包表記の利点
# - **可読性**: 簡潔な構文で、コードがより読みやすくなります。
# - **パフォーマンス**: 通常のループよりもパフォーマンスが高い場合があります。

# ### 注意点
# - **複雑なロジック**: 複雑なロジックを含む場合は、リスト内包表記がかえって読みにくくなることがあります。その場合は通常のループを使用した方が良いです。
# - **メモリ使用量**: 大きなリストを生成する場合、メモリ使用量が増加することがあります。その場合はジェネレータ内包表記（`()`を使用）を検討してください。

# リスト内包表記を使うことで、Pythonのコードをより簡潔で効率的に書くことができます。
