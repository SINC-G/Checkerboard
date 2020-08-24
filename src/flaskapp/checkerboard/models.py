#!/usr/bin/env python
# -*- encoding: utf-8 -*-

"""
1. 随机生成64格棋盘（0，1）
2. 棋子按0...63进行编号
3. 计算正面朝上棋子的序号的异或
4. 翻一枚硬币（翻转比特），这枚硬币是
5. 计算最终呈现再棋盘的异或，得到key位置

@File    :   cb_quize.py
@Time    :   2020/08/23 16:24:33
@Author  :   snc 
"""

import random


def random_checkerboard():
    checkboard = list()
    for i in range(8):
        checkboard.append([random.randint(0, 1) for i in range(8)])
    return checkboard


def random_key():
    key = random.randint(0, 63)
    return key


def flip_coin(checkboard, key):
    # 额，元组不好翻啊，也不好进行索引啊，看看numpy好不好处理
    flip = 0
    for i in range(64):
        if sequence(checkboard, i)[0] == 1:
            flip ^= i

    flip ^= key
    a, b = (sequence(checkboard, flip)[1], sequence(checkboard, flip)[2])
    checkboard[a][b] = int(not checkboard[a][b])

    return flip


def sequence(checkboard, seq):
    """ 0,63对硬币标号 """
    if seq >= 8:
        b = seq % 8
        k = int((seq-b)/8)
        return checkboard[k-1][b], k-1, b
    else:
        return checkboard[0][seq], 0, seq


def solve(checkboard):
    key = 0
    for i in range(64):
        if sequence(checkboard, i)[0] == 1:
            key ^= i

    return key


def main():
    checkboard = random_checkerboard()
    key = random_key()
    flip = flip_coin(checkboard, key)
    print(flip)
    key_s = solve(checkboard)
    if key_s == key:
        print("验证成功！")
    else:
        print("验证失败！")
    print(key)
    print(checkboard)


if __name__ == "__main__":
    main()
