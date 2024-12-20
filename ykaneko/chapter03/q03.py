import numpy as np
#Numpyをnpという名前でインポート　短縮形で使える
# すべての要素が0の3x3配列
c1 = np.zeros((3,3)) 
#np.zeros 関数を使用
print(c1)

# すべての要素が1の3x3配列
c2 = np.ones((3,3))
#np.ones 関数を使用
print(c2)

# -1から1の間のランダムな要素の3x3配列
c3 = np.random.uniform(-1,1,(3,3))
#np.random.uniform(-1, 1, (3, 3)) 関数を使用
print(c3)

# 対角要素が2で、他の要素が0の3x3配列
c4 = np.diag([2,2,2])
#np.diag([2,2,2])関数を使用　指定した対角要素を持つ対角行列を作成
print(c4)