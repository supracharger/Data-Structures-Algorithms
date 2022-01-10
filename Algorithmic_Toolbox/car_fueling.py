# python3
import sys

def compute_min_refills(distance, tank, stops):
    # write your code here
    refills, fillsize = 0, tank
    stops.insert(0, 0)
    stops.append(distance)
    for i in range(len(stops)-1):
        nextDest = stops[i+1] - stops[i]
        if nextDest > fillsize:
            return -1
        elif tank-nextDest < 0 and i > 0:
            refills += 1
            tank = fillsize
        tank -= nextDest
    return refills

if __name__ == '__main__':
    d, m, _, *stops = map(int, sys.stdin.read().split())
    #d, m, stops = 950, 400, [200,375,550,750]
    #d, m, stops  = 10, 3, [1,2,5,9]
    #d, m, stops  = 200, 250, [100,150]
    #d, m, stops  = 500, 200, [100,200,300,400] # 2 # [0*, 100,200,300,400, 500*]
    print(compute_min_refills(d, m, stops))
