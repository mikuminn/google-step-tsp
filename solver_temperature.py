#!/usr/bin/env python3

import sys
import math
import random

from common import print_tour, read_input


def distance(city1, city2):
    return math.sqrt((city1[0] - city2[0]) ** 2 + (city1[1] - city2[1]) ** 2)


def solve(cities):
    N = len(cities)

    dist = [[0] * N for i in range(N)]
    for i in range(N):
        for j in range(i, N):
            dist[i][j] = dist[j][i] = distance(cities[i], cities[j])

    #　初期解をランダムに生成
    current_tour = random.sample(range(N), N)
    current_dist = sum(dist[current_tour[i]][current_tour[(i + 1) % N]] for i in range(N)) # 巡回路の長さを計算

    # 最初の温度と冷却率を設定
    initial_temperature = 1000 # 初期の温度 (高いほど探索範囲が広がる)
    iteration_number = 0  # 繰り返し回数

    # 温度が十分低くなるまでループを繰り返す
    while iteration_number < 10000:

        iteration_number += 1
        temperature = initial_temperature / (iteration_number + 1)  # 逆時間比例冷却

        # 現在の巡回路から2つの都市の順序を入れ替える
        new_tour = current_tour.copy()
        i, j = random.sample(range(N), 2) # 2つの都市をランダムに選ぶ
        new_tour[i], new_tour[j] = new_tour[j], new_tour[i] # 順序を入れ替える

        # 新しい巡回路の長さを計算
        new_dist = sum(dist[new_tour[i]][new_tour[(i + 1) % N]] for i in range(N))

        # 近傍解が優れている（長さが短い）場合、または温度による確率で採用する
        if new_dist < current_dist or random.random() < math.exp((current_dist - new_dist) / temperature):
            current_tour, current_dist = new_tour, new_dist

    return current_tour


if __name__ == '__main__':
    assert len(sys.argv) > 1
    tour = solve(read_input(sys.argv[1]))
    print_tour(tour)
