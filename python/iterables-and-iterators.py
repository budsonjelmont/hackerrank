#https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true
from itertools import combinations

if __name__ == '__main__':
    n = input()
    line = input()
    k = int(input())
    letters = line.split(' ')
    combos = combinations(letters,k)
    hits = 0
    ncombos = 0
    for c in combos:
        hits = hits + 1 if 'a' in c else hits
        ncombos += 1
    prob = hits/ncombos
    print(f'{prob:.3f}')