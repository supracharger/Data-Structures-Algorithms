# Uses python3
import sys

def get_change(m):
    coins = m // 10
    remain = m % 10
    coins += remain // 5
    coins += remain % 5
    return coins

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
