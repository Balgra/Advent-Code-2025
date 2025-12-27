import sys
from itertools import combinations
from z3 import Optimize, Int, Sum, sat
import file_reader


def find_min_pushes(target, buttons):
    for i in range(1, len(buttons) + 1):
        for comb in combinations(buttons, i):
            result = 0
            for c in comb:
                result ^= c
            if result == target:
                return i


def find_min_pushes2(targets, buttons):
    opt = Optimize()
    x = [Int(f"x{i}") for i in range(len(buttons))]
    for xi in x:
        opt.add(xi >= 0)

    for i, target in enumerate(targets):
        coef = [int(i in button) for button in buttons]
        opt.add(Sum(xi * c for c, xi in zip(coef, x)) == target)

    opt.minimize(Sum(x))

    if opt.check() == sat:
        m = opt.model()
        return sum(m[xi].as_long() for xi in x)


lines = file_reader.input_reader()

rez1 = 0
rez2 = 0
for line in lines:
    target_s, *buttons_s, power_s = line.split()
    target = int(target_s.strip("[]")[::-1].replace("#", "1").replace(".", "0"), 2)
    buttons = [
        sum(pow(2, int(b)) for b in button.strip("()").split(","))
        for button in buttons_s
    ]

    rez1 += find_min_pushes(target, buttons)

    buttons2 = [list(map(int, b.strip("()").split(","))) for b in buttons_s]
    target2 = list(map(int, power_s.strip("{}").split(",")))
    
    rez2 += find_min_pushes2(target2, buttons2)

print(f"Part 1: {rez1}")

print(f"Part 2: {rez2}")

# That's the right answer! You are one gold star closer to decorating the North Pole.

# That's the right answer! You are one gold star closer to decorating the North Pole. You have completed Day 10!

