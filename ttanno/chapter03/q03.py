"""
以下の要素を持つ 3×3のNumPy配列を作成するプログラムを作成してください．
すべての要素が0
すべての要素が1
-1から1の間のランダムな要素
対角の要素（0行0列成分，1行1列成分，2行2列成分）が2で，他の要素が0
"""
import numpy as np

a = np.zeros((3, 3))
print(a)  # すべての要素が0

b = np.ones((3, 3))
print(b)  # すべての要素が1の配列

c = np.random.uniform(-1, 1, (3, 3))
print(c)  # -1から1の間のランダムな要素を持つ配列

d = np.diag([2, 2, 2])
print(d)  # 対角の要素が2で他の要素が0の配列