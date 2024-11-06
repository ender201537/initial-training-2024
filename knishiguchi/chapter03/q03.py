#以下の要素を持つ3×3のNumPy配列を作成するプログラムを作成してください

import numpy as np

#すべての要素が0
a = np.zeros((3, 3))
print(a)

#すべての要素が1
b = np.ones((3, 3))
print(b)

#-1から1の間のランダムな要素
c = np.random.uniform(-1,1,(3,3))
print(c)

#対角の要素（0行0列成分，1行1列成分，2行2列成分）が2で，他の要素が0
d = np.diag([2,2,2])#np.diag([]) 一次元配列を指定するとその配列を対角成分とした対角行列を生成できる
print(d)