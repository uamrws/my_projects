import gc
import os
import sys
import time

from functools import lru_cache


def change_money(total, ans):
    if total < 0:
        return False
    if total == 0:
        return True
    for i in range(2, 3, 5):
        change_money(total - i, ans)


if __name__ == '__main__':
    ans = []
    change_money(10, ans)
    print(ans)
    22222
    2233
    235
    55
