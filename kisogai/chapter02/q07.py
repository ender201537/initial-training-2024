def f(a):
    a = [6, 7, 8]

def g(a):
    a.append(1)

def somefunction():
    a0 = [1, 2, 3]
    f(a0)
    print(a0)

    a1 = [1, 2, 3]
    g(a1)
    print(a1)

somefunction()

#予想
#[1, 2, 3]
#[1, 2, 3, 1]
#somefunctionの関数内で、a0とa1が作成されて[1,2,3]の初期値を持つ
#関数f(a)でa=[6,7,8]で代入が行われている。
#ローカル変数aに新しいリスト[6,7,8]に再割り当てしているだけ。
#(f(a)内での代入a=[6,7,8]は関数内のローカル変数aの参照先を変更するだけであり、a0の内容を変えるわけではない)

#リストを関数の引数として、リストの参照を行う。
#appendなどのリストの内容を変更する操作を行うと、関数外でもその変更が反映される。